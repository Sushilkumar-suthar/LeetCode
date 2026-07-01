
class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }

        return prev;
    }

    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr)
            return true;

        ListNode* slow = head;
        ListNode* fast = head;

        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* secondHalf = reverse(slow->next);

        ListNode* firstHalf = head;
        ListNode* temp = secondHalf;

        while (temp != nullptr) {
            if (firstHalf->val != temp->val) {
                reverse(secondHalf);
                return false;
            }
            firstHalf = firstHalf->next;
            temp = temp->next;
        }
        slow->next = reverse(secondHalf);

        return true;
    }
};