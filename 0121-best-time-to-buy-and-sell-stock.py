class Solution:
    def maxProfit(self, prices):
        """
        :type prices: list[int]
        :rtype: int
        """

        max_profit = 0
        for day_buy in range(1, len(prices) + 1):
            for day_sell in range(day_buy, len(prices) + 1):
                index_buy = day_buy - 1
                index_sell = day_sell - 1

                profit = prices[index_sell] - prices[index_buy]
                max_profit = max(max_profit, profit)

        return max_profit


def main():
    sol = Solution()

    prices_a = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices_a))

    prices_b = [7,6,4,3,1]
    print(sol.maxProfit(prices_b))


if __name__ == '__main__':
    main()
