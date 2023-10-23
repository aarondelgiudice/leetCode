public class ReverseLinkedList {
    public static void main(String[] args) {
        // test cases
        Object[] testCases = new Object[] {
                new Object[] { new int[] { 1, 2, 3, 4, 5 }, new int[] { 5, 4, 3, 2, 1 } },
                new Object[] { new int[] { 1, 2 }, new int[] { 2, 1 } },
                new Object[] { new int[] { 1 }, new int[] { 1 } }
        };

        for (Object testCase : testCases) {
            Object[] testCaseArray = (Object[]) testCase;
            int[] nums = (int[]) testCaseArray[0];
            int[] expected = (int[]) testCaseArray[1];
            ListNode head = ListNode.createLinkedList(nums);
            ListNode actual = solution(head);

            if (!ListNode.compareLinkedLists(actual, expected)) {
                throw new AssertionError(
                        String.format("solution(%s) == %s, expected %s", head, actual, expected));
            }
        }
    }

    public static ListNode solution(ListNode head) {
        // recursive solution
        return recursion(head, null);

        // // iterative solution
        // // initialize previous pointer as null
        // ListNode prv = null;
        // // initialize current as the current head
        // ListNode cur = head;

        // // loop until current points to null
        // while (cur != null) {
        // // reverse direction, prv->cur->cur.next to prv<-cur<-cur.next
        // // initialize temp as the next pointer of current
        // ListNode tmp = cur.next;
        // // update current.next to point to previous
        // cur.next = prv;
        // // update previous to point to current
        // prv = cur;
        // // update current to point to tmp (originally current.next)
        // cur = tmp;
        // }
        // return prv; // return new head of linked list
    }

    private static ListNode recursion(ListNode head, ListNode newHead) {
        // base case
        if (head == null) {
            return newHead;
        } else {
            ListNode next = head.next;
            head.next = newHead;
            return recursion(next, head);
        }
    }
}