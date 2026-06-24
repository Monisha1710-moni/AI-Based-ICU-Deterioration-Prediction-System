from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

# Features used by the model
FEATURES = ["Age", "Glucose", "HR", "Temp", "SysABP", "RespRate"]

FIELD_MAP = {
    "age": "Age",
    "glucose": "Glucose",
    "hr": "HR",
    "temp": "Temp",
    "sysabp": "SysABP",
    "resprate": "RespRate"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    values = {}
    errors = []

    for form_key, column_name in FIELD_MAP.items():

        raw = request.form.get(form_key, "").strip()

        if raw == "":
            errors.append(f"{column_name} is required.")
            continue

        try:
            values[column_name] = float(raw)

        except ValueError:
            errors.append(f"{column_name} must be a number.")

    if errors:
        return render_template(
            "index.html",
            error=" ".join(errors),
            form_values=request.form
        )

    data = pd.DataFrame([values], columns=FEATURES)

    try:
        result = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1]

        print("Prediction =",result)
        print("Probability =",probability)
        print("Input Data:")
        print(data)

    except Exception:
        return render_template(
            "index.html",
            error="The model could not process these values. Please check your inputs and try again.",
            form_values=request.form
        )

    if result == 1:
        prediction = f"⚠️ High Risk of ICU Deterioration"
        confidence = probability * 100
        risk_level = "High Risk"

    else:
        prediction = f"✅ Low Risk of ICU Deterioration"
        confidence = (1 - probability) * 100
        risk_level = "Low Risk"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=f"{confidence:.2f}",
        risk_level=risk_level,
        form_values=request.form
    )


if __name__ == "__main__":
    app.run(debug=True)