---
scope: python
tags: [style, typing, lint]
priority: 20
applies_to: ["**/*.py", "pyproject.toml"]
version: "0.2.0"
inherits: [".github/copilot-instructions/copilot-instructions.global.md"]
---

# Copilot Instructions — Python

-   公開関数には型注釈を付ける（Optional は typing.Optional 推奨）。
-   コード整形は black + ruff をベースにし、生成コードは別ディレクトリに分離する。
-   Django の ORM を使う場合は N+1 を防ぐため select_related / prefetch_related を提案する。
-   テストでは pytest を標準とし、fixture の利用を推奨する。
-   セキュリティに関する案は「環境変数で秘匿」「パラメタライズドクエリ」を必ず含める。
-   必要なパッケージは、requirements.txt に記載すること。
-   コメント文は不要。やむを得ず記載する場合は、簡潔な英語で記述すること。
-   ファイル名、変数名、メソッド名は簡潔な英語で記述する。
-   ファイル名の区切りは、アンダーバー(\_)を使用する。
-   クラス名およびメソッド名は、キャメルケースを使用する。
-   定数名は、すべて大文字で記述し、単語の区切りにはアンダーバー(\_)を使用する。
-   クラス名は名詞、メソッド名は動詞で命名して、{class_name}.{method_name}で意味が通じるようにする。 -テストコードは、test/ に配置し、prefix に "test-{2 桁の連番}-" を付与する。

# ログ

-   ログは、logging および colorama を使用して出力する。
-   ログ設定は、log.config (json 形式) に記載し、それを読み込んで使用する。
-   ログファイルは、/var/log/ 以下に保存する。
-   ログレベルは、DEBUG, INFO, WARNING, ERROR, CRITICAL を使用する。
-   ログメッセージは簡潔な英語で記述する。
-   ログのフォーマットは、`yyyy-MM-dd HH:mm:ss [ %(levelname)s-5 ] %(message)s` とする。
-   ログレベル毎の役割は、以下の通り。
    -   DEBUG: 開発者が問題の切り分けに使用する情報。
    -   INFO: ユーザに通知すべき正常動作の情報。各機能ブロックの開始／終了など。
    -   WARNING: 警告。将来的に問題になる可能性があることを示す。
    -   ERROR: エラー。システムは継続動作するものの、内部的に何らかの異常が発生した場合。(例：例外発生、処理前の条件チェック NG など)
    -   CRITICAL: 深刻なエラー。システム全体の停止や重大な障害を示す場合。
