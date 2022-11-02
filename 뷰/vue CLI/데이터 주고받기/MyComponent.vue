<template>
  <div class="border">
    <h1>
      쌔로운 컴포넌트!
    </h1>
    <MyComponentItem 
      static-props="이 프롭은 상위에서 내려왔습니다."
      :dynamic-props="dynamicProps"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name:'MyComponent',
  components: {
    MyComponentItem,
  },
  data: function() {
    return {
      dynamicProps: '이건 동적 데이터라니까'
    }
  },
  methods : {
    parentGetEvent: function (childData) {
      console.log('용돈 없어!!')
      console.log((childData))
    },
    getDynamicData: function(input) {
      console.log(`사용자 입력 값은 ${input}입니다`)
    }
  }

}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>