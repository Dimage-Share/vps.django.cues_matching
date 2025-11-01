# Copilot Instructions — 運用ガイド

-   配置: `.github/copilot-instructions/` に instruction ファイルと `manifest.yaml` を置く。
-   新規ファイル: `copilot-instructions.<scope>.<name>.md` 形式で作成し manifest に追記する。
-   適用ルール: global→language→framework→project の順で適用、priority が高いものが末端ルール。
-   変更: すべて PR にてレビュー、manifest の更新を忘れないこと。
-   CI: manifest スキーマ検証（YAML schema）とリンクチェック推奨。
