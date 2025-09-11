# django_todo

仮想環境の作成
python -m venv venv
source venv/Scripts/activate　で仮想環境内に入る
deactivate で出る

今回は初期設定で以下のコマンドを使う
"django-admin startproject todoproject ."
"."を入れると階層が一個減る

"python manage.py startapp todo"でアプリケーションの作成

settings.pyでtemplatesの設定とappの記載
manage.pyの階層でtemplatesファイルを作成

.gitignoreの設定

urls.pyにappとの接続パスを記載