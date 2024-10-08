<template>
    <!-- <div class="test-view">
        <p>test page created by me</p>
    </div> -->
    <p>test page created by me</p>
    <h1>somethig: {{ text }}</h1>
    <button @click="send_request_to_backend()">click me</button>
</template>
<script>
import axios from 'axios';
export default {
    name: 'TestView',
    data(){
        return {
            text: null
        }
    },
    created(){
        console.log("in created");
        this.send_request_to_backend();
    },
    methods:{
        test(){
            console.log('test')
        },
        send_request_to_backend(){
            console.log('send_request_to_backend')


            axios.get('http://localhost:5000/api/test')
            .then(response=>{
                console.log(response)
                this.text = response.data.status
            })
            .catch(error=>{
                console.log("error component", error)
            })
        }
    }
}
</script>