#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

    int carry = 0;
    ListNode* h = new ListNode();
    ListNode* m = h;
    while (l1 || l2 || carry){

        int sum = carry;
        if (l1 != NULL){
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2 != NULL){
            sum += l2->val;
            l2 = l2->next;
        }

        ListNode* temp = new ListNode(sum%10);
        carry = sum/10;
        m->next = temp;
        m = m->next;
    }
    return h->next;
}

int main(){

}


// https://leetcode.com/problems/add-two-numbers
// medium