<template>
    <div class="create_page">
        <form>
            <input type="text" v-model="this.name" placeholder="name"><br>
            <button type="button" @click.prevent="this.post()">create</button>
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
            token: null
        }
    },
    created(){
        this.token = localStorage.getItem('authToken')
        if(this.token == null){
            this.$router.push({name: 'login'})
        }
    },
    methods:{
        post(){
            axios.post('http://localhost:5000/version3',
                {
                    'key_name': this.name
                },
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
        }
    }
}
</script>