---
scope: project
tags: [project-specific]
priority: 40
applies_to: ["cues/**"]
version: "0.1.0"
inherits: [".github/copilot-instructions/copilot-instructions.django.md"]
---

# Copilot Instructions — cues

-   このプロジェクトでは API は DRF を使用し、Response は常に serializer で整形する。
-   画像は最大 4 枚まで、アップロード時にサムネイル生成を行う。
-   CI は GitHub Actions を用い、テスト・lint・build を分離したジョブで実行する。
-   設定は環境ごとに .env ファイルを切り替えること（.env.template を必ず更新する）。

# Github Copilot プロンプト出力

-   今回の開発は、私にとって初めての Django 開発である。
-   そのため、Django 独自の用語や概念の簡潔な説明を含めること。

# リモート環境

リモート環境は、以下の VPS サーバを使用する。

XServer VPS
`OS` Ubuntu 24.04 LTS
`CPU` 4 コア
`メモリ` 6 GB
`ストレージ` 150 GB SSD
`IPアドレス` 162.43.92.97
`ホスト名` vps-dstroke
`標準ホスト名` x162-43-92-97.static.xvps.ne.jp
`逆引きホスト名` x162-43-92-97.static.xvps.ne.jp
`収容ホスト` host02-26

# テスト要件

## 単体テスト

**`カバレッジ目標`** >= 80%
**`テストフレームワーク`** pytest
**`自動化`** CI/CD パイプライン

## 結合テスト

**`カバレッジ目標`** >= 70%
**`テストフレームワーク`** pytest + playwright
**`自動化`** CI/CD パイプライン

## システムテスト

**`カバレッジ目標`** >= 60%
**`テストフレームワーク`** pytest + playwright
**`自動化`** CI/CD パイプライン

## パフォーマンステスト

**`ツール`** JMeter
**`シナリオ`** 主要なユーザ操作をシミュレート
**`レスポンスタイム`** 95 パーセンタイルで 2s 以下
**`同時接続数`** Max1000 ユーザ
**`自動化`** CI/CD パイプライン

## セキュリティテスト

**`ツール`** OWASP ZAP
**`スキャン頻度`** >= 1 回/月
**`脆弱性対応`** 発見次第、速やかに対応
**`自動化`** CI/CD パイプライン
