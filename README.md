# Flask API for predicting the GDP of a country

A Flask application that uses a regression model trained on the [IMF WEO data](https://www.imf.org/~/media/Files/Publications/WEO/WEO-Database/2020/02/WEOOct2020all.ashx) to make GDP per capita predictions. The [notebook](notebook/gdp.ipynb) used to train the model is also included.

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
    "average_consumer_price_inflation_index": 85.95,
    "continent": "Australia",
    "current_account_balance": -10.668,
    "employment": 7.666,
    "implied_ppp_conversion_rate": 17.023,
    "gross_nation_savings": 20.897,
    "unemployment_rate": 5.392,
    "population": 17.719
}
```

Sample output:
```json
{
    "GDPPC": 5051.844959999995
}
```

### Running tests

We use `unittest` to run tests.
```shell
python api/tests.py
```
