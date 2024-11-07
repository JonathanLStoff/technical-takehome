<template>
  <img alt="ARETUM logo" src="./assets/ARETUM+Logo_Final.png">
  <CounterComponent/>
</template>




<script>
import CounterComponent from './components/Counter.vue'

export default {
  name: 'App',
  components: {
    CounterComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
img {
  width: 250px;
  height: 200px;
  margin: 0 auto;
  display: block;
  justify-content: center;
}
</style>
