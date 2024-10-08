<template>
  <h3>app.vue strat</h3>
  <nav>
    <!-- <a href="/">home</a> -->
    <router-link to="/">Home1234</router-link> |
    <router-link :to="{name: 'test'}">test</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
  <h3>app.vue end</h3>
</template>

<script>
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
