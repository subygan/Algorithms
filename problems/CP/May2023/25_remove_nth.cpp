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

ListNode create(vector<int> v) {
    ListNode h = ListNode(123);
    ListNode *head = &h;
    for (int i: v) {
        ListNode h = ListNode(i, head);
        head->next = &h;
    }
    return h;
}

ListNode *removeNthFromEnd(ListNode *head, int n) {

    ListNode *start = new ListNode();
    start->next = head;

    ListNode *f = start;
    ListNode *s = start;

    for (int i=0;i<n;++i) f = f->next;

    while (f->next != NULL) {
        s = s->next;
        f = f->next;
    }

    s->next = s->next->next;
    return start->next;
}

int main() {

    ListNode lnode = create(vector<int>({1, 2, 3}));
    ListNode * head = &lnode;
    while (head) {
        cout<<head->val;
        head = head->next;
    }

}

// https://leetcode.com/problems/remove-nth-node-from-end-of-list
// medium