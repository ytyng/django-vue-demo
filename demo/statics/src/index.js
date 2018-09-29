import Vue from 'vue';
import template from './template.html';
import './style.scss';
import myItems from './components/items.vue';

const app = new Vue({
  el: '#demo-items',
  template,
  data: {
    items: [],
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
  },
});
