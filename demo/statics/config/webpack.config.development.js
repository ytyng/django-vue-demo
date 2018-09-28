const merge = require('webpack-merge');
const baseConfig = require('./webpack.config.base.js');

module.exports = merge(baseConfig, {
  mode: 'development',
  devtool: 'source-map',
  resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js',
        'vuex$': 'vuex/dist/vuex.esm.js',
      },
      extensions: ['*', '.js', '.vue', '.json']
  },
});
