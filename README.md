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

保存先については
Leetcode: Workspace Folder
を
/workspaces/[リポジトリ名]にする


たまに更新されるのでそのたびにsessionIdを更新する

Gitコミット署名しよう
https://zenn.dev/kawarimidoll/scraps/74779919683dad