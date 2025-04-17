from flask import Flask, render_template, request
from gpt_utils import generate_kanpo_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")  # ← 今作ったHTMLを home.html として保存

@app.route("/form")
def form():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    data = {
        "age": request.form.get("age"),
        "gender": request.form.get("gender"),
        "main_complaint": request.form.get("main_complaint"),
        "symptoms": request.form.getlist("symptoms"),
        "other_symptoms": request.form.get("other_symptoms"),
        "tongue": request.form.getlist("tongue"),
        "other_tongue": request.form.get("other_tongue"),
        "abdomen": request.form.getlist("abdomen"),
        "other_abdomen": request.form.get("other_abdomen")
        "period": request.form.get("period")
    }

    result_text = generate_kanpo_response(data)
    return render_template("result.html", result=result_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
