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
    ListView:データ一覧をリストとして表示することに適したテンプレート
    DetailView:データの中身を表示することに適したテンプレート
U:UpdateView
D:DeleteView

djangoのhtml
{% %} 複雑な処理
{{ }}　データ

## day3
DetailViewの追加
⇒モデルの中から任意の一つを表示する
⇒主キー(今回はID)をurlsで指定してあげる

Bootstrap(version注意)
フロントのフレームワーク
CSSファイルが用意されている
Starter templateｗコピペしてくる
⇒そこに付け加える形で編集していく

base.htmlの使いまわし
どのhtmlファイルにも使う構文(枠組み)を一つにまとめておく
枠組みは以下のように分けられる
Block header
Block content
Block slidebar
Block footer

html内のobjectについて
object は、～View で取得された1つのモデルインスタンス。
テンプレート内で object.フィールド名 で値を表示。

