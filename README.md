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
  * poetry run sphinx-build docs docs/_build
* 確認用にsphinx-autobuild で動作確認できるように修正
  * poetry add --dev sphinx-autobuild
  * poetry run sphinx-autobuild docs docs/_build
  * sphinx-autobuild.bat を作成
* netlifyにデプロイするための整備
  * runtime.txt、requirement.txt、netlify.toml
  * netlifyにてgithubと連携
  * サイト確認
    * https://mtakagishi-template.netlify.app/
* pydata_sphinx_theme を適用
  * conf.pyを修正
    * 
