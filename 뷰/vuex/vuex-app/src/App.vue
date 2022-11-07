<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h3>입력된 메시지의 길이는 {{messageLength}}</h3>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>

export default {
  name: 'App',
  computed: {
    message() {
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    },
  },
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage',newMessage)
      this.inputData = null
    }
  },

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
</style>
