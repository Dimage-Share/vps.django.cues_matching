import subprocess
import webbrowser
import time

if __name__ == "__main__":
    # Djangoサーバーをバックグラウンドで起動
    proc = subprocess.Popen(
        ["python", "manage.py", "runserver", "127.0.0.1:8000"], cwd="cues")
    # サーバー起動まで少し待つ
    time.sleep(2)
    # ブラウザで開く
    webbrowser.open("http://127.0.0.1:8000")
    # サーバープロセスを待機
    proc.wait()
