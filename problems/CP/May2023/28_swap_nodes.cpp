#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *swapPairs(ListNode *head) {

    ListNode *h = head;
    ListNode *dupHead = new ListNode(-1);
    ListNode *dupTail = new ListNode(-1);
    dupHead->next = head;

    while (h->next) head = head->next;
    head->next = dupTail;

    ListNode *prev = h, *cur = h->next, *next = h->next;

    while (next && next->val != -1) {
        ListNode *nextCur = next->next;

        prev->next = next;
        cur->next = nextCur;
        next->next = cur;

        prev = cur;
        cur = nextCur;
        next = cur->next;
    }

    ListNode *chTail = h;
    //chopping the tail
    while (chTail->next->val != -1) chTail = chTail->next;
    chTail->next = NULL;




    return h->next;
}

int main() {

}

// https://leetcode.com/problems/swap-nodes-in-pairs
// medium