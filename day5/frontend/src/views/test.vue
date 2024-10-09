<template>
    <!-- <div class="test-view">
        <p>test page created by me</p>
    </div> -->
    <p>test page created by me</p>
    <h1>somethig: {{ text }}</h1>
    <button @click="send_request_to_backend()">click me</button>

    <h1>token: {{ token }}</h1>
    <h1>role: {{ role }}</h1>
    <h2>users</h2>
    <table>
        <thead>
            <tr><th>user id</th>
            <th>email</th>
            <th>status</th>
            <th>action</th></tr>
            
        </thead>
        <tbody>
            <tr v-for="user in users" >
                <td>{{user.id}}</td>
                <td>{{user.email}}</td>
                <td>{{user.status}}</td>
                <td>
                    <button @click="this.switch(user.id)">test</button>
                </td>
            </tr>
        </tbody>
    </table>
    <h2>data</h2>
    <table>
        <thead>
            <tr><th>id</th>
            <th>name</th>
            <th>name1</th>
            <th>action</th></tr>
            
        </thead>
        <tbody>
            <tr v-for="user in data" >
                <td>{{user.id}}</td>
                <td>{{user.name}}</td>
                <td>{{user.name1}}</td>
                <td>
                    <button @click="this.delete(user.id)">delete</button>
                    <!-- <button @click="this.delete(user.id)">delete</button> -->
                </td>
            </tr>
        </tbody>
    </table>
</template>
<script>
import axios from 'axios';
export default {
    name: 'TestView',
    data(){
        return {
            text: null,
            token: null,
            role: null,
            users: null,
            data: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        if (this.token == null){
            this.$router.push({name: 'login'})
        }
        console.log("in created");
        this.send_request_to_backend();
        this.role = localStorage.getItem('role')
    },
    methods:{
        test(){
            console.log('test')
        },
        switch(id){
            axios.post('http://localhost:5000/switchuser',
            {
                user_id: id
            },
            {headers: {
                'Authorization': this.token,
            }},
        )
            .then(response=>{
                console.log("response", response)
                if(response.status == 201){
                    this.send_request_to_backend()
                }                
            })
            .catch(error=>{
                console.log("error component", error)
            })
        },
        send_request_to_backend(){
            this.text = null
            console.log('send_request_to_backend')


            axios.get('http://localhost:5000/api/test')
            .then(response=>{
                console.log(response)
                this.text = response.data.status
                this.users = response.data.users
            })
            .catch(error=>{
                console.log("error component", error)
            })
            axios.get('http://localhost:5000/version1')
            .then(response=>{
                console.log(response)
                this.data = response.data.json
            })
            .catch(error=>{
                console.log("error component", error)
            })
        },
        delete(id){
            axios.delete('http://localhost:5000/version3',
            {
                id: id
            },
            {headers: {
                'Authorization': this.token,
            }},
            )
            .then(response=>{
                console.log(response)
                if(response.status == 201){
                    this.send_request_to_backend()
                }
            })
            .catch(error=>{
                console.log(error)
            })
        }
    }
}
</script>