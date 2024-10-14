<template>
  <!-- <h3>app.vue strat</h3> -->
  <nav>
    <!-- <a href="/">home</a> -->
    <router-link :to="{name: 'login'}">login</router-link> |
    <router-link :to="{name: 'test'}">test</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/signup">Signup</router-link> |
    <router-link to="/create">create</router-link> |
    <a @click="this.logout()">logout</a>
  </nav>
  <router-view/>
  <!-- <h3>app.vue end</h3> -->
</template>

<script>
export default {
  name: 'App',
  methods:{
    logout(){
      localStorage.clear()
      this.$router.push({name: 'login'})
    }
  }
}
</script>

<style>
#app123 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
