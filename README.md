メロディはフレーズ単位で見ると3〜5音程度でできていることが多い

そこで、4音をランダムに選び出す

偏りはある（臨時記号は選出されにくい）

移動ドを想定

```
$ python3 app.py            # 偏りのあるランダムで、メジャー、4音を提示する。log.txtに書き足す。
$ python3 app.py True       # メジャーの音が多めの実行
$ python3 app.py False      # マイナーの音が多めの実行
$ python3 app.py True 5     # 5個の音を提示する
$ python3 sample.py         # 25回app.pyを実行する
```