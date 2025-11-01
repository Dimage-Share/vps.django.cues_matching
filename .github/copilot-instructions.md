# 開発環境

Python 3.10 以上
Django 4.2 以上
その他必要なパッケージは、requirements.txt に記載する。

# Github Copilot プロンプト出力

-   今回の開発は、私にとって初めての Django 開発である。そのため、Django 独自の用語や概念の簡潔な説明を含めること。
-   日本語で出力する。
-   出力するコードは、Django フレームワークに準拠する。
-   出力するコードは、PEP8 規約に準拠する。
-   出力するコードは、可能な限り最新のベストプラクティスに従う。
-   出力するコードは、セキュリティを考慮する。
-   出力するコードは、パフォーマンスを考慮する。
-   出力するコードは、可読性を考慮する。
-   出力するコードは、保守性を考慮する。
-   出力するコードは、再利用性を考慮する。
-   出力するコードは、テスト可能性を考慮する。
-   出力するコードは、国際化（i18n）を考慮する。
-   出力するコードは、アクセシビリティ（a11y）を考慮する。

# ページデザイン

## レイアウト／デザイン方針

-   フルブリードを基本とする。
-   コンテンツの可読性を最優先する。
-   レスポンシブデザインを採用し、モバイルファーストで設計する。
-   カラースキームは、落ち着いたトーンを基調とし、アクセントカラーを効果的に使用する。
-   フォントは、読みやすさを重視し、Web セーフフォントを選択する。
-   画像やアイコンは、高解像度で最適化されたものを使用し、ページのパフォーマンスに配慮する。

### ファイル構成

-   CSS ファイルは、/static/css/ 以下に保存する。
-   画像ファイルは、/static/images/ 以下に保存する。
-   JavaScript ファイルは、/static/js/ 以下に保存する。
-   テンプレートファイルは、/templates/ 以下に保存する。

# コード規約

## コメント文

-   不要です。
-   どうしても必要な場合は、簡潔な英語で記述してください。

## 命名規則

-   ファイル名、変数名、関数名は簡潔な英語で記述してください。
-   ファイル名の区切りは、アンダーバー(\_)を使用します。
-   クラス名およびメソッド名は、キャメルケースを使用します。
-   定数名は、すべて大文字で記述し、単語の区切りにはアンダーバー(\_)を使用します。
-   クラス名は名詞、メソッド名は動詞で命名して、{class_name}.{method_name}で意味が通じるようにします。
-   テストコードは、test/ に配置し、prefix に "test-{2 桁の連番}-" を付与する。

## ログ

-   ログは、logging および colorama を使用して出力します。
-   ログ設定は、log.config (json 形式) に記載し、それを読み込んで使用する。
-   ログファイルは、/var/log/ 以下に保存する。
-   ログレベルは、DEBUG, INFO, WARNING, ERROR, CRITICAL を使用します。
-   ログメッセージは簡潔な英語で記述します。
-   ログのフォーマットは、`yyyy-MM-dd HH:mm:ss [ %(levelname)s-5 ] %(message)s` とします。
-   ログレベル毎の役割は、以下の通りです。
    -   DEBUG: 開発者が問題の切り分けに使用する情報。
    -   INFO: ユーザに通知すべき正常動作の情報。各機能ブロックの開始／終了など。
    -   WARNING: 警告。将来的に問題になる可能性があることを示す。
    -   ERROR: エラー。システムは継続動作するものの、内部的に何らかの異常が発生した場合。(例：例外発生、処理前の条件チェック NG など)
    -   CRITICAL: 深刻なエラー。システム全体の停止や重大な障害を示す場合。

# リモート環境

リモート環境は、以下の VPS サーバを使用する。

-   XServer VPS
    -   OS: Ubuntu 24.04 LTS
    -   CPU: 4 コア
    -   メモリ: 6 GB
    -   ストレージ: 150 GB SSD
    -   IP アドレス: 162.43.92.97
    -   ホスト名: vps-dstroke
    -   標準ホスト名: x162-43-92-97.static.xvps.ne.jp
    -   逆引きホスト名: x162-43-92-97.static.xvps.ne.jp
    -   収容ホスト: host02-26

# ソース管理

Github を使用して管理する。

-   リポジトリ名: vps.django.cues_matching

# Django モジュール

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
