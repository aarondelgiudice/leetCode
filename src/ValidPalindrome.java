public class ValidPalindrome {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] {
                        "A man, a plan, a canal: Panama", true
                },
                new Object[] {
                        "race a car", false
                },
                new Object[] {
                        " ", true
                }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;

            String s = (String) testCaseArray[0];
            boolean expected = (boolean) testCaseArray[1];
            boolean actual = Solution(s);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("solution(%s) == %s, expected %s", s, actual, expected));
            }
        }
    }

    public static boolean Solution(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (!Character.isLetterOrDigit(s.charAt(left))) {
                left += 1;
            }

            else if (!Character.isLetterOrDigit(s.charAt(right))) {
                right -= 1;
            }

            else {
                if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                    return false;
                }

                else {
                    left += 1;
                    right -= 1;
                }
            }
        }
        return true;
    }
}