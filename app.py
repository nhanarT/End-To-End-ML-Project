from flask import Flask, request, render_template

import numpy as np
from ml_project.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/inference", methods=["POST"])
def inference():
    distance_from_home = float(request.form["distance_from_home"])
    distance_from_last_transaction = float(
        request.form["distance_from_last_transaction"]
    )
    ratio_to_median_purchase_price = float(
        request.form["ratio_to_median_purchase_price"]
    )
    repeat_retailer = float(request.form["repeat_retailer"])
    used_chip = float(request.form["used_chip"])
    used_pin_number = float(request.form["used_pin_number"])
    online_order = float(request.form["online_order"])

    data = [
        distance_from_home,
        distance_from_last_transaction,
        ratio_to_median_purchase_price,
        repeat_retailer,
        used_chip,
        used_pin_number,
        online_order,
    ]
    data = np.array(data).reshape(1,7)

    prediction_pipeline = PredictionPipeline()
    prediction = prediction_pipeline.predict(data)[0]

    return f"Fraud = {prediction}"


if __name__ == "__main__":
    app.run(port=9090, debug=True)
