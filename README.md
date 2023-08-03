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


gpg: key 5724AA0E4BC6A5E8 marked as ultimately trusted
gpg: directory '/home/vscode/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/vscode/.gnupg/openpgp-revocs.d/988F9D8EF7918FF56FEE5F1D5724AA0E4BC6A5E8.rev'
public and secret key created and signed.

pub   rsa4096 2023-08-03 [SC]
      988F9D8EF7918FF56FEE5F1D5724AA0E4BC6A5E8
uid                      megablacklabel <megablacklabel@gmail.com>
sub   rsa4096 2023-08-03 [E]


❯ git config --global gpg.program `which gpg`
❯ git config --global commit.gpgsign true
❯ git config --global user.signingkey "988F9D8EF7918FF56FEE5F1D5724AA0E4BC6A5E8"
❯ git config --get-regexp 'gpg|sign'