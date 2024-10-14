<template>
    <h2>search</h2>
    <input type="text" v-model="search" placeholder="search">
    <button @click="this.search_req()">search</button>
    <div v-if="data != null">
        <h3>data found</h3>
    </div>
</template>
<script>
import axios from 'axios';

export default{
    data(){
        return{
            search: null,
            data: null,
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
        search_req(){
            axios.post()
        }    
    }
}
</script>