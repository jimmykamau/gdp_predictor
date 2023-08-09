import unittest
import sys

sys.path.append(".")

from main import app


class PredictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self) -> None:
        self.ctx.pop()

    def test_post_predict(self):
        request_body = {
            "average_consumer_price_inflation_index": 85.95,
            "continent": "Australia",
            "current_account_balance": -10.668,
            "employment": 7.666,
            "implied_ppp_conversion_rate": 17.023,
            "gross_nation_savings": 20.897,
            "unemployment_rate": 5.392,
            "population": 17.719
        }
        response = self.client.post("/", json=request_body)
        assert response.status_code == 200
        assert response.json.get("GDPPC", False)


if __name__ == "__main__":
    unittest.main()
