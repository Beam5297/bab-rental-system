from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "ระบบห้องเช่า BAB พร้อมใช้งานแล้ว!"

if __name__ == '__main__':
    app.run(debug=True)
