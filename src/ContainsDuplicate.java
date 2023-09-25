import java.util.Set;
import java.util.HashSet;

public class ContainsDuplicate {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 1, 2, 3, 1 }, true },
                new Object[] { new int[] { 1, 2, 3, 4 }, false },
                new Object[] { new int[] { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 }, true }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] nums = (int[]) testCaseArray[0];
            boolean expected = (boolean) testCaseArray[1];
            boolean actual = solution(nums);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("containsDuplicate(%s) == %s, expected %s", nums, actual, expected));
            }
        }
    }

    public static boolean solution(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();

        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            } else {
                set.add(num);
            }
        }
        return false;
    }
}