# Flask API for predicting the GDP of a country

A Flask application that uses a regression model trained on the [IMF WEO data](https://www.imf.org/~/media/Files/Publications/WEO/WEO-Database/2020/02/WEOOct2020all.ashx) to make GDP predictions. The [notebook](notebook/gdp.ipynb) used to train the model is also included.

### Dependencies
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Pandas](https://pandas.pydata.org/)
- [Poetry](https://python-poetry.org/)

### Installation and setup
Install dependencies with Poetry.

```shell
poetry install
```

Activate the virtual environment

```shell
poetry shell
```

Run the Flask server
```shell
flask --app api/main run
```

### Endpoints
#### / (POST)

Returns a field showing the predicted GDP per capita.

The endpoint expects a JSON request similar to the one shown below. Note that all fields are mandatory:
```json
{
    "consumer_price_index": 39.685,
    "continent": "Australia",
    "current_account_balance": -10.668,
    "employment": 7.666,
    "general_governemnt_structural_balance": -18.328,
    "gross_nation_savings": 20.897,
    "implied_ppp_conversion_rate": 10.883,
    "population": 17.719
}
```

Sample output:
```json
{
    "GDPPC": 21454.89110999999
}
```

### Running tests

We use `unittest` to run tests.
```shell
python api/tests.py
```
