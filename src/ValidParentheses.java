import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { "()", true },
                new Object[] { "()[]{}", true },
                new Object[] { "(]", false },
                new Object[] { "([)]", false },
                new Object[] { "{[]}", true }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            String s = (String) testCaseArray[0];
            boolean expected = (boolean) testCaseArray[1];
            boolean actual = solution(s);

            if (actual != expected) {
                throw new AssertionError(
                        String.format("solution(%s) == %s, expected %s", s, actual, expected));
            }
        }
    }

    public static boolean solution(String s) {
        Stack<Character> stack = new Stack<Character>();

        // map open paren to closing paren
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        // loop through each character in the string
        // check if the character if the character is an open parentheses ("({[")
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                // push corresponding closing parentheses character to stack
                stack.push(map.get(c));
            }
            // else, character is a closing parentheses ("]})")
            else {
                // check if stack is empty, closing paren + empty stack -> invalid
                // check if last char in stack == current char, if not -> invalid
                if (stack.isEmpty() || stack.pop() != c) {
                    return false; // invalid
                }
            }
        }

        // valid -> if stack is empty i.e. all open parentheses have been closed (popper
        // from stack), return true
        return stack.isEmpty();
    }
}