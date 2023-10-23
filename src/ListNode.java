// Definition for singly-linked list.
public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    // helper methods
    public static String toString(ListNode head) {
        StringBuilder sb = new StringBuilder();
        ListNode curr = head;

        while (curr != null) {
            sb.append(curr.val);
            sb.append("->");
            curr = curr.next;
        }

        sb.append("null");
        return sb.toString();
    }

    public static ListNode createLinkedList(int[] nums) {
        ListNode head = new ListNode(nums[0]);
        ListNode curr = head;

        for (int i = 1; i < nums.length; i++) {
            curr.next = new ListNode(nums[i]);
            curr = curr.next;
        }

        return head;
    }

    public static boolean compareLinkedLists(ListNode head, int[] nums) {
        ListNode curr = head;

        for (int i = 0; i < nums.length; i++) {
            if (curr.val != nums[i]) {
                return false;
            }

            curr = curr.next;
        }

        return true;
    }
}