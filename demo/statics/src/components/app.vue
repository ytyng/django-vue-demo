<template>
  <div>
    <my-items :items='items' />
  </div>
</template>

<script>
  import myItems from './items.vue';

  export default {
    name: 'app',
    data() {
      return {
        'items': [],
      }
    },
    components: {
      myItems,
    },
    created() {
      fetch('/items/api/items')
        .then((response) => {
          return response.json();
        }).then((data) => {
        this.items = data.result;
      });
    }
  }
</script>

<style lang="scss" scoped>
</style>
