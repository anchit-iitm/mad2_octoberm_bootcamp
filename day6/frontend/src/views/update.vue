<template>
    <div class="create_page">
        <form>
            <input type="text" v-model="this.name" placeholder="name"><br>
            <input type="text" v-model="this.desc" placeholder="desc"><br>
            <button type="button" @click.prevent="this.put_req()">create</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';
export default{
    name: 'CreateView',
    data(){
        return{
            name: null,
            desc: null,
            token: null,
            id: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        if(this.token == null){
            this.$router.push({name: 'login'})
        }
        this.id = this.$route.params.id
        console.log(this.id);
        this.get_req()
        
    },
    methods:{
        put_req(){
            axios.put(`http://localhost:5000/api/category/${this.id}`,
                {'name': this.name, 'description': this.desc},
                {
                    headers: {'Authorization': this.token}
                }
            )
            .then(response=>{
                console.log(response)
                if(response.status == 201){
                    this.$router.push({name: 'test'})
                }
            })
            .catch(error=>{
                console.log(error)
            })
        },
        get_req(){
            axios.get(`http://localhost:5000/api/category/${this.id}`,
                {
                    headers: {'Authorization': this.token}
                }
            )
            .then(response=>{
                console.log(response)
                if(response.status == 200){
                    this.name = response.data.data.name
                    this.desc = response.data.data.description
                }
            })
            .catch(error=>{
                console.log(error)
            })
        }
    }
}
</script>