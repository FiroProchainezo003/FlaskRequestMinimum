# Flask Request最小サンプル

## プロジェクトについて

このプロジェクトはFlaskで `form` から `request` を受け取るための最小サンプルです。<br>
text, radio, checkbox, fileに対応しています。


## プロジェクトの取得方法

クローンしてください。
```
git clone https://github.com/FiroProchainezo003/FlaskRequestMinimum
```

## 実行方法

### windows

```
# Cloneしたフォルダで
$ python3 -m vevn venv
$ venv\Scripts\activate
$ python app.py
```

1. ブラウザから `http://localhost:5000/upload` にアクセス
2. フォームを入力し、addボタンを押す。<br>
   入力内容がある場合、ページ上に内容が表示されます。

### linux

```
# Cloneしたフォルダで
$ python3 -m vevn venv
$ source venv/Scripts/activate
$ python app.py
```

1. ブラウザから `http://localhost:5000/upload` にアクセス
2. フォームを入力し、addボタンを押す。<br>
   入力内容がある場合、ページ上に内容が表示されます。

## pythonバージョン

```
$ flask --version
Python 3.8.3
Flask 1.1.2
Werkzeug 1.0.1
```

## Flaskがサポートしているバージョン

[Flask - 1.1.x Installation](https://flask.palletsprojects.com/en/1.1.x/installation/)

