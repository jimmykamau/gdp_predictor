from marshmallow import Schema, fields


class PredictRequestSchema(Schema):
    current_account_balance = fields.Float(required=True)
    average_consumer_price_inflation_index = fields.Float(required=True)
    employment = fields.Float(required=True)
    implied_ppp_conversion_rate = fields.Float(required=True)
    unemployment_rate = fields.Float(required=True)
    continent = fields.String(required=True)
    population = fields.Float(required=True)
    gross_nation_savings = fields.Float(required=True)
