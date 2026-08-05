from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("employee_attrition_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = request.form["age"]
    salary = request.form["salary"]
    years = request.form["years"]

    data = [[age, salary, years]]

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Employee may Leave"
    else:
        result = "Employee will Stay"

    return result

if __name__ == "__main__":
    app.run(debug=True)