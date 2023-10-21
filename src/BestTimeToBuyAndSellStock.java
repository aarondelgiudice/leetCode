public class BestTimeToBuyAndSellStock {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 7, 1, 5, 3, 6, 4 }, 5 },
                new Object[] { new int[] { 7, 6, 4, 3, 1 }, 0 }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] prices = (int[]) testCaseArray[0];
            int expected = (int) testCaseArray[1];
            int actual = solution(prices);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("containsDuplicate(%s) == %s, expected %s", prices, actual, expected));
            }
        }
    };

    public static int solution(int[] prices) {
        // // edge cases
        // if (prices.length <= 1 || prices == null) {
        // return 0;
        // }

        // // two pointers & current profit
        // int slow = 0;
        // int fast = 1;
        // int maxProfit = Math.max(0, prices[fast] - prices[slow]);

        // // loop over array -> O(n)
        // while (fast < prices.length - 1) {
        // if (prices[fast] < prices[slow]) {
        // // buy price (slow) is decreasing -> update slow
        // slow = fast;
        // }

        // // update sell price (fast)
        // fast += 1;

        // // check current profit vs. current max profit
        // int profit = prices[fast] - prices[slow];
        // maxProfit = Math.max(profit, maxProfit);
        // }

        // return maxProfit;

        // O(n) time, O(1) space
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            }

            else {
                int profit = price - minPrice;
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }

        return maxProfit;
    }
}