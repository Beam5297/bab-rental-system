from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "ระบบห้องเช่า BAB พร้อมใช้งานแล้ว!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ใช้ PORT จาก Render หรือ fallback 5000
    app.run(host='0.0.0.0', port=port)
