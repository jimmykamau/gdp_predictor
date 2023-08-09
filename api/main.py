from flask import Flask, request, jsonify
import joblib
import pandas as pd
from marshmallow import ValidationError
import traceback

from api.schema import PredictRequestSchema

app = Flask(__name__)

model_columns = joblib.load("notebook/models/required_columns.pkl")
model = joblib.load("notebook/models/gdp_predictor.pkl")


@app.route("/", methods=["POST"])
def predict():
    schema = PredictRequestSchema()

    try:
        body = schema.load(request.json)
        dataframe_format = dict(
            BCA=[body["current_account_balance"]],
            PPPEX=[body["implied_ppp_conversion_rate"]],
            LE=[body["employment"]],
            LUR=[body["unemployment_rate"]],
            PCPI=[body["average_consumer_price_inflation_index"]],
            Continent=[body["continent"]],
            LP=[body["population"]],
            NGSD_NGDP=[body["gross_nation_savings"]],
        )
        query = pd.get_dummies(pd.DataFrame(dataframe_format))
        query = query.reindex(columns=model_columns, fill_value=0)
        prediction = model.predict(query)

        return jsonify({"GDPPC": prediction.tolist()[0]}), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
    except Exception as e:
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500
