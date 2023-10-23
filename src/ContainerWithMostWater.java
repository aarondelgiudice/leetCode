public class ContainerWithMostWater {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 1, 8, 6, 2, 5, 4, 8, 3, 7 }, 49 },
                new Object[] { new int[] { 1, 1 }, 1 },
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] height = (int[]) testCaseArray[0];
            int expected = (int) testCaseArray[1];
            int actual = solution(height);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("solution(%s) == %s, expected %s", height, actual, expected));
            }
        }
    }

    private static int solution(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxWater = 0;
        int curWater = 0;

        while (left < right) {
            curWater = (right - left) * Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, curWater);

            if (height[left] < height[right]) {
                left += 1;
            } else { // height[left] > height[right]
                right -= 1;
            }
        }

        return maxWater;
    }
}