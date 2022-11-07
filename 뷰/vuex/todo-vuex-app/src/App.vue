<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>All Todos: {{allTodosCount}}</h2>
    <h2>Compelted Todo: {{completedTodosCount}}</h2>
    <h2>UnCompelted Todo: {{uncompletedTodosCount}}</h2>
    <TodoList/>
    <TodoForm/>
    <!-- <button @click="loadTodos">Todo 불러오기</button> -->
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
import createPersistedState from 'vuex-persistedstate'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  computed:{
    allTodosCount() {
      return this.$store.getters.allTodosCount
    },
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount() {
      return this.$store.getters.unCompletedTodosCount
    }
  },
  methods :{
    // loadTodos() {
    //   this.$store.dispatch('loadTodos')
    // }
  },
  plugins: [
    createPersistedState(),
  ]
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
