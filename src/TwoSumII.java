import java.util.Arrays;

public class TwoSumII {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 2, 7, 11, 15 }, 9, new int[] { 1, 2 } },
                new Object[] { new int[] { 2, 3, 4 }, 6, new int[] { 1, 3 } },
                new Object[] { new int[] { -1, 0 }, -1, new int[] { 1, 2 } }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] numbers = (int[]) testCaseArray[0];
            int target = (int) testCaseArray[1];
            int[] expected = (int[]) testCaseArray[2];
            int[] actual = solution(numbers, target);

            if (!Arrays.equals(actual, expected)) {
                throw new AssertionError(
                        String.format("solution(%s, %s) == %s, expected %s", numbers.toString(),
                                target,
                                actual.toString(), expected.toString()));

            }
        }
    }

    private static int[] solution(int[] numbers, int target) {
        // initialize left and right pointers
        int left = 0;
        int right = numbers.length - 1;

        // loop until left and right pointers meet
        while (left < right) {
            // sum of left and right pointers
            int sum = numbers[left] + numbers[right];

            // check if sum is equal to target
            if (sum == target) {
                // return {left index position, and right index position}
                return new int[] { left + 1, right + 1 };
            }

            // check if sum is less than target
            else if (sum < target) {
                // increment left pointer
                left += 1;
            }

            // check if sum is greater than target
            else { // sum > target
                   // decrement right pointer
                right -= 1;
            }
        }

        return new int[] { -1, -1 }; // no solution found
    }
}