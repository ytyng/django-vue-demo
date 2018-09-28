# django-vue-handson

## 用語解説
- node(node.js) ...サーバサイドで動くJavaScriptもしくはJavaScript実行環境のこと

cf.[Node.js を5分で大雑把に理解する](https://qiita.com/hshimo/items/1ecb7ed1b567aacbe559)
- npm ...node上で使えるJavaScriptパッケージ管理ツール

cf.[npm入門](https://qiita.com/maitake9116/items/7825d90c09f3e2f87dea)

| 言語 | パッケージ管理 | 管理ファイル |
|:----:|:--------------:|:------------:|
| python | pip | requirements.txt |
| node(js) | npm | package.json |

## 環境構築
#### 推奨環境
- python3.5以上
- pip 18.0 (pip -V)
- node v10.4.1
- npm 6.4.1
#### project clone
- git clone git@github.com:MasatoraSakikoyama/django-vue-demo.git
- cd django-vue-demo
#### python
- python -V
- pyenv versions
- (pyenv install 3.5.x or 3.5.x)
- pyenv local 3.5.x or 3.6.x
#### 仮想環境
- pyvenv .venv
- . ./.venb/bin/activate
#### pythonライブラリ
- pip install upgrade pip
- pip install -r requirements.txt
#### node
- node -V
- npm install -g n
- sudo n stable
#### npm
- npm -v
- npm update -g npm
#### nodeライブラリ
- cd statics
- npm install

## 注意事項
- 簡便化のためdjangoのcsrf middlewareを殺しているのでproductにそのまま適用しないこと。
