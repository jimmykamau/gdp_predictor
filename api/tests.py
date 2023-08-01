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
            "consumer_price_index": 39.685,
            "continent": "Australia",
            "current_account_balance": -10.668,
            "employment": 7.666,
            "general_governemnt_structural_balance": -18.328,
            "gross_nation_savings": 20.897,
            "implied_ppp_conversion_rate": 10.883,
            "population": 17.719,
        }
        response = self.client.post("/", json=request_body)
        assert response.status_code == 200
        assert response.json.get("GDPPC", False)


if __name__ == "__main__":
    unittest.main()
