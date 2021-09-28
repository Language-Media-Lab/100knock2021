# 言語処理100本ノック 2021年度
言語メディア研2021年度新入生向け勉強会として、言語処理100本ノックに取り組みます。  
教材URL: https://nlp100.github.io/ja/  

毎週全員1章分（10問）解いてください。(※ただし2章は除く)  
勉強会のときに毎週1人1章分、自分のコードを説明してもらいます。  

# usage
初回はこのレポジトリを clone してください。  
```
$ git clone https://github.com/Language-Media-Lab/100knock2021.git
```
  
各Chapterのはじめでは、各Chapterのディレクトリへ移動し、ブランチを切って、自分用の作業用ブランチで作業してください。  
ブランチの名前は自分の名前にしてください(例：北大太郎の場合、hokudai_taro)
```
# 取り組むChapterへ移動
$ cd chapter1
#新規ブランチ作成
$ git branch hokudai_taro
#作成したブランチに切り替え
$ git checkout hokudai_taro
```

コードを書いたら自身のブランチの remote repository に push してください。  
- ~Pythonで書いた場合、ファイル名はすべて二桁の数字にしてください（例: knock00.py）~
- ~google colab等で書いた場合、ファイル名は各Chapterの数字にしてください。（例: chapter01.ipynb）~  

**2021/09/28追記**
- Pythonで書いた場合、ファイル名はすべて二桁の数字 & 自分の名前を入れてください（例: knock00_taro.py）
- google colab等で書いた場合、ファイル名は各Chapterの数字 & 自分の名前を入れてください。（例: chapter01_taro.ipynb）
```
$ git add ./knockXX.py
$ git commit -m 'your message'
$ git push origin hokudai_taro
```
毎週1章分の担当者が書いたコードのレビューを行い、問題がなければ、mainへマージされます。  
**毎週各章のマージまで終わらせて，その日の勉強会を終わらせてください**

# 注意事項
わからないところはSlack等で**積極的に** TA か研究室の人に聞いてください。     

# メモ・相談事項
- ファイル形式は.pyもしくは.ipynbが考えられるが、統一する? それとも混合でok?→混合でok
- 2021年度のチュートリアルでは各担当者のマージまではできませんでした（ファイル名が全員同名だったのでコンフリクトしてしまった）  
- →来年度はファイル名の末尾に自分の名前を入れるようにすると，コンフリクトが発生しないと思います
- 現在はmainブランチに山本さんのファイルがマージされています
