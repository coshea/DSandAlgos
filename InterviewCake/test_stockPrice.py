from unittest import TestCase
from StockPrice import StockPrice


class TestStockPrice(TestCase):
    def test_get_max_profit_given_example(self):
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        expected_result = 6

        pricer = StockPrice()
        result = pricer.get_max_profit(stock_prices_yesterday)

        self.assertEqual(expected_result, result)

    def test_get_max_profit_same_prices(self):
        stock_prices_yesterday = [10, 10, 10, 10, 10, 10]
        expected_result = 0

        pricer = StockPrice()
        result = pricer.get_max_profit(stock_prices_yesterday)

        self.assertEqual(expected_result, result)



    def test_get_max_profit_all_negative(self):
        stock_prices_yesterday = [10, 9, 8, 6, 4, 1]
        expected_result = -1

        pricer = StockPrice()
        result = pricer.get_max_profit(stock_prices_yesterday)

        self.assertEqual(expected_result, result)

