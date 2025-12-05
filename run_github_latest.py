from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "سرور فعال است!"

@app.route("/signal")
def signal():
    try:
        # پوشه پروژه‌ی گیتهاب مثلا /home/user/leilabot
        repo_dir = "/home/YOUR_USER/YOUR_REPO"
        # با git pull جدیدترین کد را می‌گیرد
        proc = subprocess.run("git pull", cwd=repo_dir, shell=True, capture_output=True)
        # اجرای فایل اصلی (korosh.py)
        result = subprocess.run("python korosh.py --once", cwd=repo_dir, shell=True, capture_output=True)
        return f"گیت پول شد و اجرا:\n{result.stdout.decode('utf-8')}"
    except Exception as e:
        return f"خطا: {str(e)}"
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)