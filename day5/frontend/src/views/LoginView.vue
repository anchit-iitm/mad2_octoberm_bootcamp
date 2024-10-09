<template>
    <h1>login</h1>
    <form>
        <input type="email" name="" id="" placeholder="email" v-model="this.email" required><br><br>
        <input type="text" name="" id="" placeholder="password" v-model="this.password" required><br><br>
        <button @click.prevent="this.login()">login</button> <br>
        {{ this.message }}
        <!-- {{ this.token }} -->
    </form>
</template>

<script>
import axios from 'axios';
export default{
    name: 'LoginView',
    data(){
        return{
            email: null,
            password: null,
            message: null,
            token: null
        }
    },
    methods:{
        login(){
            console.log('login')
            if(this.email == null){
                console.log('email cant be null')
                this.message = 'email cant be null'
                return
            }
            if(this.password == null){
                console.log('password cant be null')
                this.message = 'password cant be null'
                return
            }
            console.log(this.email)
            console.log(this.password)
            axios.post('http://localhost:5000/signin',
            {
                email: this.email,
                password: this.password
            }
        )
        .then(response=>{
            console.log("response", response)
            this.message = response.data.status
            this.token = response.data.authToken
            if (response.data.status == 'login successful'){
                localStorage.setItem('authToken', response.data.authToken)
                localStorage.setItem('role', response.data.role)
                if(localStorage.getItem('role') == 'admin'){
                    this.$router.push({name: 'test'})
                // this.$router.push({name: 'test'})
            }}
        })
        .catch(error=>{
            console.log("error component", error)
            this.message = error.response.data
        })
        this.email = null
        this.password = null
    }
    }
}
</script>