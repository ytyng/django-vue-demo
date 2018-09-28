const path = require('path');

module.exports = {
  mode: 'development',
  devtool: 'source-map',
  context: path.resolve(__dirname, './src'),
  entry: './index.js',
  output: {
    path: path.resolve(__dirname, './dist'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.scss/,
        use: [
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              url: false,
            },
          },
          {
            loader: 'sass-loader',
            options: {
              sourceMap: true,
            },
          },
        ],
      },
      {
        test: /\.html/,
        loader: 'html-loader',
      },
    ],
  },
  resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js',
        'vuex$': 'vuex/dist/vuex.esm.js',
      },
      extensions: ['*', '.js', '.vue', '.json']
  },
};
