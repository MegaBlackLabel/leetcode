# leetcode

拡張機能 Leetcodeインストール後、一度起動する。

起動後に~/.lc/leetcodeが作成されているのを確認する

user.json ファイルを作成する

以下のJSONを追加。初回時のみいったんvscodeを再起動。

```
{
  "login": "[username]",
  "loginCSRF": "",
  "sessionCSRF": "[copied from csrftoken]",
  "sessionId": "[copied from LEETCODE_SESSION]"
}
```

たまに更新されるのでそのたびにsessionIdを更新する