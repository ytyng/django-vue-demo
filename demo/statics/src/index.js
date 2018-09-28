import Vue from 'vue';
import Axios from 'axios';
import template from './template.html';
import './style.scss';
import myItems from './components/items';

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
    Axios.get('/items/api/items')
      .then((response) => {
        this.items = response.data.result
      })
      .catch((error) => {});
  },
});
