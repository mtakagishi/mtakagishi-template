#!/bin/bash
set -euo pipefail # シェルスクリプトのエラーハンドリング

# 言語ごとにsphinx-buildを実行するループ
for lang in ja en es de zh ar hi eo; do
    sphinx-build -b html docs docs/_build/html/${lang} -D language=${lang}
done

# 必要なファイルをコピーする
cp index.html docs/_build/html/
cp robots.txt docs/_build/html/
cp ads.txt docs/_build/html/
cp docs/_build/html/ja/sitemap.xml docs/_build/html/
