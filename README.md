# django_todo

## day1
仮想環境の作成
python -m venv venv
"source venv/Scripts/activate"　で仮想環境内に入る
deactivate で出る

今回は初期設定で以下のコマンドを使う
"django-admin startproject todoproject ."
"."を入れると階層が一個減る

"python manage.py startapp todo"でアプリケーションの作成

settings.pyでtemplatesの設定とappの記載
manage.pyの階層でtemplatesファイルを作成

.gitignoreの設定

urls.pyにappとの接続パスを記載

## day2
models.pyの追加
⇒DBとの接続

modelsに加えた修正のpythonファイル(migration)を作成⇒履歴を残すため
"python manage.py makemigrations"
作成したファイルを実行しDBに反映
"python manage.py migrate"

管理者画面の作成
urls.pyのadminの画面
ターミナル上でユーザーを設定できる
"python manage.py createsuperuser"

管理者画面のDBにmodelsに加えたものを反映させる
admin.pyに文言追加

DBでの表示名を変更する
models.pyを編集

CRUDとdjango
C:CreateView
R:ListView DetailView ← Read（情報を読み取る）
U:UpdateView
D:DeleteView

djangoのhtml
{% %} 複雑な処理
{{ }}　データ
