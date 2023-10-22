public class BinarySearch {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { -1, 0, 3, 5, 9, 12 }, 9, 4 },
                new Object[] { new int[] { -1, 0, 3, 5, 9, 12 }, 2, -1 }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] nums = (int[]) testCaseArray[0];
            int target = (int) testCaseArray[1];
            int expected = (int) testCaseArray[2];
            int actual = solution(nums, target);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("solution(%s, %s) == %s, expected %s", nums, target, actual, expected));
            }
        }
    }

    public static int solution(int[] nums, int target) {
        return recursiveSearch(nums, target, 0, nums.length - 1);
    }

    private static int recursiveSearch(int[] nums, int target, int low, int high) {
        if (low > high) {
            return -1;
        }

        int mid = low + (high - low) / 2;

        if (nums[mid] == target) {
            return mid;
        }

        else if (nums[mid] > target) {
            return recursiveSearch(nums, target, low, mid - 1);
        }

        else { // nums[mid] < target
            return recursiveSearch(nums, target, mid + 1, high);
        }
    }
}