<template>
    <!-- <div class="test-view">
        <p>test page created by me</p>
    </div> -->
    <input type="text" placeholder="search field" v-model="this.search_field">
    <button @click="search_fn()">search</button>
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
        <!-- <table v-if="this.filtered_data==null"> -->
        <thead>
            <tr><th>id</th>
            <th>name</th>
            <th>desc</th>
            <th>created at</th>
            <th>created by</th>
            <th>status</th>
            <th>delete</th>
            <th>action</th></tr>
            
        </thead>
        <tbody>
            <tr v-for="user in data">
                <td>{{user.id}}</td>
                <td>{{user.name}}</td>
                <td>{{user.description}}</td>
                <td>{{user.created_at}}</td>
                <td>{{user.created_by}}</td>
                <td>{{user.status}}</td>
                <td>{{user.delete}}</td>
                <td v-if="user.delete == false">
                    <button @click="this.delete(user.id)">delete</button>
                    <button><router-link :to="{'name': 'update', params:{'id': user.id}}">update</router-link></button>
                </td>
            </tr>
        </tbody>
    </table>
        <table v-if="this.filtered_data != null">
        <thead>
            <h3>searched data</h3>
            <tr><th>id</th>
            <th>name</th>
            <th>desc</th>
            <th>created at</th>
            <th>created by</th>
            <th>status</th>
            <th>delete</th>
            <th>action</th></tr>
            
        </thead>
        <tbody>
            <tr v-for="user in filtered_data">
                <td>{{user.id}}</td>
                <td>{{user.name}}</td>
                <td>{{user.description}}</td>
                <td>{{user.created_at}}</td>
                <td>{{user.created_by}}</td>
                <td>{{user.status}}</td>
                <td>{{user.delete}}</td>
                <td v-if="user.delete == false">
                    <button @click="this.delete(user.id)">delete</button>
                    <button><router-link :to="{'name': 'update', params:{'id': user.id}}">update</router-link></button>
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
            data: null,
            search_field: null,
            filtered_data: null
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


            axios.get('http://localhost:5000/api/test', {headers: {
                'Authorization': this.token,
            }})
            .then(response=>{
                console.log(response)
                this.text = response.data.status
                this.users = response.data.users
            })
            .catch(error=>{
                console.log("error component", error)
            })
            axios.get('http://localhost:5000/api/category', {headers: {
                'Authorization': this.token,
            }})
            .then(response=>{
                console.log(response)
                this.data = response.data.data
            })
            .catch(error=>{
                console.log("error component", error)
            })
        },
        delete(id){
            axios.delete(`http://localhost:5000/api/category/${id}`,
            {headers: {
                'Authorization': this.token,
            }},
            {
                id: id
            }
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
        },
        search_fn(){
            // filtered the data var, based on the search_field, the result is stored in filtered_data var
        }
    }
}
</script>