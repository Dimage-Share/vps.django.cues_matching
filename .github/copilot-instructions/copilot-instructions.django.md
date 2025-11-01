---
scope: django
tags: [framework, django, db]
priority: 30
applies_to: ["**/manage.py", "**/requirements.txt"]
version: "0.1.0"
inherits: [".github/copilot-instructions/copilot-instructions.python.md"]
---

# Copilot Instructions — Django Projects

-   モデル設計はシンプルに、フィールドは明示的にし、index・unique は必要な箇所のみに設定する。
-   管理画面カスタマイズは admin.ModelAdmin を使いすぎない（必要最小限）。
-   メディアは S3 など外部ストレージを想定、settings で明確に切替できるようにする。
-   マイグレーションには説明コメントを含め、スキーマ変更は段階的に行う。
-   クエリ重視箇所にはパフォーマンステストケースを作ることを提案する。

# ページデザイン --- 基本方針

フルブリードを基本とする。
コンテンツの可読性を最優先する。
レスポンシブデザインを採用し、モバイルファーストで設計する。
カラースキームは、落ち着いたトーンを基調とし、アクセントカラーを効果的に使用する。
フォントは、読みやすさを重視し、Web セーフフォントを選択する。
画像やアイコンは、高解像度で最適化されたものを使用し、ページのパフォーマンスに配慮する。

# ページデザイン --- レスポンシブ設計

**`スマートフォン`** 1136×640
**`タブレット`** 2000×1200
**`PC`** 1366×768

# ページデザイン --- モバイルファースト

タッチ操作を想定し、タッチターゲットのサイズを確保すること。
パフォーマンスを考慮し、画像圧縮と遅延読込を実装すること。
ナビゲーションを簡素化するため、シンプルなメニュー構造とすること。

## 国際化／ローカライズ (I18N/L10N)

本システムの UI は、日本語と英語に対応する。
日付／通貨形式は、世界の地域のローカル形式で表示すること。

# django モジュール

## 必須モジュール

以下のモジュールは必ず使用すること。
**`django-allauth`** 認証、登録、アカウント管理

```settings.py
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "email"
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
```

**`Pillow + django-versatileimagefield`** 画像処理
**`PostgreSQL全文検索 + django-filter`** 検索処理
**`django-machima`** フォーラム
**`DRF + django-rest-auth`** API 公開
**`Celery + Redis`** メール送信、重たい処理

```settings.py
CELERY_BROKER_URL = "redis://localhost:6379/0"
```

**`jazzmin`** 管理画面カスタマイズ

## おすすめモジュール

**`django-rest-auth`** DRF ベースの認証 API
**`django-two-factor-auth`** 2 要素認証
**`django-axes`** ブルートフォース攻撃防止
**`django-anymail`** メールサービス連携
**`django-versatileimagefield/sorl-thumbnail/easy-thumbnails`** サムネイル生成、クロップ、複数解像度の管理
**`django-cleanup`** 不要ファイルの自動削除
**`django-model-utils`** TimeStampedModel などの便利なモデル
**`django-choices/enumfields`** 選択肢フィールドの管理
**`django-taggit`** タグ付け
**`django-guardian`** オブジェクト単位の権限管理
**`Elasticsearch/OpenSearch`** 検索処理 (中規模向け)
**`django-filter`** リスト絞込み
**`django-machina`** フォーラムエンジン。カテゴリ、スレッド、投稿、権限管理が可能。比較的導入しやすい。
**`Spirit`** Django 用 CMS。モダンなフォーラムアプリ。柔軟なコンテンツ管理が可能。
**`django-postman/messages`** 内部のプライベートメッセージ機能。
**`django-channels + Redis`** リアルタイムチャット
**`django-notifications-hq, webpush`** プッシュ通知
**`django-rest-framework`** API 公開するなら必須。認証やシリアライザが充実。
**`drf-yasg/drf-spectacular`** OpenAPI(Swagger)ドキュメント生成
**`dj-stripe`** Strip Connect による決済機能
**`django-payments`** 複数の決済ゲートウェイ対応
**`django-admin`** 管理画面
**`jazzmin,django-grappelli,django-admin-interface,django-jet`** django-admin カスタマイズ
**`Google Analytics (django-analytical)`** アクセス解析
**`django-auditlog`** 操作ログ
**`Celery+Redis/RabbitMQ`** 非同期タスクキュー。メール送信、サムネ生成、通知配信、リコメンド処理（非同期）。
**`django-cacheops, django-redis`** Redis キャッシュ
**`django-ratelimit`** フォームや API のリクエスト制限
**`django-secure`** 設定チェック
**`django-recaptcha, django-simple-captcha`** スパム対策
**`django-debug-toolbar, django-extensions`** 開発用デバッグツール
**`factory_boy, pytest-django`** テスト支援ツール
**`crispy-forms`** フォームのカスタマイズ（フォームがきれいになる）
**`Sentry`** エラー監視
