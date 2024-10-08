<template>
  <div class="about">
    <h1>This is an about page</h1> 
    <HelloWorld msg="coming from the about page"/>
  </div>
</template>
<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
// import HelloWorld from '../components/HelloWorld.vue'

export default {
  components: {
    HelloWorld
  }
}
</script>