class StockPrice:
    def get_max_profit(self, stock_prices_yesterday):

        # make sure we have at least 2 prices
        if len(stock_prices_yesterday) < 2:
            raise IndexError('Getting a profit requires at least 2 prices')

        min_price = stock_prices_yesterday[0]
        max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

        for index, current_price in enumerate(stock_prices_yesterday):
            if index == 0:
                continue

            current_profit = current_price - min_price

            max_profit = max(max_profit, current_profit)
            min_price = min(min_price, current_price)

        return max_profit
