# 変更点

### package.json
vue-loader のインストールについて追記

### webpack.config.js
vue-loader の設定を追加。
ちなみに
```javascript
plugins: [
  // make sure to include the plugin for the magic
  new VueLoaderPlugin()
],
```
が無いと動かない

### statics/src
templates, css を components/app.vue にコンポーネント化。
index.js は app.vue を呼ぶだけにした

### statics/src/components/items/
.vue にコンポーネント化

### demo/demo/urls.py
/ のURL の際、Django のビューを実行せず、static.serve で index.html をそのまま返すようにした。
本番なら、nginx から直接返すとよさそう。

### Ajax
fetch api にしてみた
(statics/src/components/app.vue)

# PyCharm File Watcher
ファイルウォッチャーで自動ビルドが可能。
```
Name: webpack build

File type: Any

Scope: 作る。
statics/src/ 以下の再帰的にウォッチする、という設定が作れる

Program: /usr/local/bin/npm
Arguments: run build
```
これで、Gulp みたいに使える

すでに、index.html は Django から切り離されているので、
Vue CLI でテストサーバ起動してウォッチさせてもいいと思う。