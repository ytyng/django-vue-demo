<template>
  <ul>
    <li v-for="item in items">
      {{ item.number }} {{ item.name }} {{ item.description }}
    </li>
  </ul>
</template>

<script>
  export default {
    name: 'my-items',
    props: ['items'],
  }
</script>

<style lang="scss" scoped>
</style>
