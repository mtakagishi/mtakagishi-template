# mtakagishi-template

## リポジトリ内容
sphinxやthemeのバージョン変化に追随するための検証用

## やったことメモ
* .gitignoreにpoetry.lockを対象に変更
* poetry init　コマンドで pyproject.tomlを作成
* poetryセッティングを確認
  * poetry config --list
  * poetry config virtualenvs.in-project true
* poetry install で初期化
* pydata-sphinx-themeベースのsphinx環境準備
  * poetry add pydata-sphinx-theme
* sphinx初期化
  * mkdir docs
  * cd docs
  * poetry run sphinx-quickstart
* .gitignoresphinx設定を確認
  * docs/_build/ が除外されていればOK
* 初動確認
  * poetry shell
  * ./make.bat html