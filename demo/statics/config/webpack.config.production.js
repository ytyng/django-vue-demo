const merge = require('webpack-merge');
const baseConfig = require('./webpack.config.base.js');

module.exports = merge(baseConfig, {
  mode: 'production',
  resolve: {
      alias: {
        'vue$': 'vue/dist/vue.runtime.min.js',
        'vuex$': 'vuex/dist/vuex.min.js',
      },
      extensions: ['*', '.js', '.vue', '.json']
  },
});
