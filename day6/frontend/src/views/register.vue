<template>
    <h1>signup</h1>
    <form>
        <input type="email" name="" id="" placeholder="email" v-model="this.email" required><br><br>
        <input type="text" name="" id="" placeholder="password" v-model="this.password" required><br><br>
        <select v-model="this.role">
            <option value="manager">manager</option>
            <option value="customer">customer</option>
        </select>
        <button @click.prevent="this.signup()">Signup</button> <br>
        {{ this.message }}
        <!-- {{ this.token }} -->
    </form>
</template>

<script>
import axios from 'axios';
export default{
    name: 'registerView',
    data(){
        return{
            email: null,
            password: null,
            message: null,
            role: null
        }
    },
    methods:{
        signup(){
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
            if(this.role == null){
                console.log('role cant be null')
                this.message = 'role cant be null'
                return
            }
            console.log(this.email)
            console.log(this.password)
            axios.post('http://localhost:5000/signup',
            {
                email: this.email,
                password: this.password,
                role: this.role
            }
        )
        .then(response=>{
            console.log("response", response)
            this.message = response.data.status
            if (response.status == 201){
                this.$router.push({name: 'login'})
            }
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