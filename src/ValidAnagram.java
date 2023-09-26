import java.util.HashMap;

public class ValidAnagram {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { "anagram", "nagaram", true },
                new Object[] { "rat", "car", false }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            String s = (String) testCaseArray[0];
            String t = (String) testCaseArray[1];
            boolean expected = (boolean) testCaseArray[testCaseArray.length - 1];
            boolean actual = Solution(s, t);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("solution(%s, %s) == %s, expected %s", s, t, actual, expected));
            }
        }
    }

    public static boolean Solution(String s, String t) {
        HashMap<Character, Integer> count = new HashMap<Character, Integer>();

        for (char x : s.toCharArray()) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        for (char x : t.toCharArray()) {
            count.put(x, count.getOrDefault(x, 0) - 1);
        }

        for (int val : count.values()) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
}