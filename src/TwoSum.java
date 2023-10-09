import java.util.HashMap;

public class TwoSum {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 2, 7, 11, 15 }, 9, new int[] { 0, 1 } },
                new Object[] { new int[] { 3, 2, 4 }, 6, new int[] { 1, 2 } },
                new Object[] { new int[] { 3, 3 }, 6, new int[] { 0, 1 } }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] nums = (int[]) testCaseArray[0];
            int target = (int) testCaseArray[1];
            int[] expected = (int[]) testCaseArray[2];

            int[] actual = solution(nums, target);

            if (actual[0] != expected[0] || actual[1] != expected[1]) {
                throw new AssertionError(
                        String.format("twoSum(%s, %s) == %s, expected %s", nums, target, actual, expected));
            }
        }
    }

    public static int[] solution(int[] nums, int target) {
        HashMap<Integer, Integer> results = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            // diff == target - nums[i] -> the value we want to find to solve for target
            int diff = target - nums[i];

            // check if curr is in results
            if (results.containsKey(diff)) {
                // return {curr index position, and nums index position}
                return new int[] { results.get(diff), i };
            }

            // add nums value : index position to results
            else {
                results.put(nums[i], i);
            }
        }

        // no solution found
        return new int[] { -1, -1 };
    }
}