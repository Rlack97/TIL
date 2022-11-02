<template>
  <div class="blackboard">
    <h4>
      아이템
    </h4>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input 
      type="text" 
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name:'MyComponentItem',
  props: {
    staticProps : String,
    dynamicProps : String
  },
  data: function () {
    return {
      childInputData: null,
    }
  },
  methods:{
    childToParent: function() {
      this.$emit('event-accured','wow')
    },
    childInput : function() {
      this.$emit('child-input', this.childInputData)
    }
  }
}
</script>

<style>
 .blackboard {
  border: dotted crimson 2px;
 }
</style>