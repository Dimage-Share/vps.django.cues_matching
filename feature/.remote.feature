Feature: デバッグ手順

    Scenario: リモート環境テスト
        Given ローカルテストが完了していること。
        Then ローカル側で "git push"を実施する。
        Then リモート側で "git pull"を実施する。
        Then リモート側で "sudo systemctl restart gunicorn"を実施する。
        Then リモート側で "sudo systemctl restart nginx"を実施する。
        Then ブラウザで "http://162.43.92.97/" にアクセスし、動作確認を行う。
