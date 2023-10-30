import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;

public class TopKFrequentElements {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 1, 1, 1, 2, 2, 3 }, 2, new int[] { 1, 2 } },
                new Object[] { new int[] { 1 }, 1, new int[] { 1 } }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] nums = (int[]) testCaseArray[0];
            int k = (int) testCaseArray[1];
            int[] expected = (int[]) testCaseArray[2];
            int[] actual = solution(nums, k);

            if (!Arrays.equals(expected, actual)) {
                throw new AssertionError(String.format("solution(%s, %s) == %s, expected %s",
                        Arrays.toString(nums), k, Arrays.toString(actual), Arrays.toString(expected)));
            }
        }
    }

    private static int[] solution(int[] nums, int k) {
        // count frequency of elements
        HashMap<Integer, Integer> counter = new HashMap<>();

        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        // create a max heap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> counter.get(b) - counter.get(a));

        for (int num : counter.keySet()) {
            maxHeap.add(num);
        }

        // write k most frequent elements to output
        int[] output = new int[k];

        for (int i = 0; i < k; i++) {
            output[i] = maxHeap.poll();
        }

        return output;

    }
}