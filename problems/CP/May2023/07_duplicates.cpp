#include <iostream>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* deleteDuplicates(ListNode* head) {

    ListNode* h = head;

    while(h!=NULL){
        if (h->next!=NULL && h->val == h->next->val) {
            ListNode* temp=h->next;
            h->next = h->next->next;

            temp->next = NULL;
            delete temp;
        } else {
            h = h->next;
        }

    }

    return head;
}

int main(){

    ListNode lv[3] = {ListNode(1),ListNode(2),ListNode(3)};

    ListNode *resutl = deleteDuplicates(lv);

    while(resutl){
        cout<<resutl->val<<endl;
        resutl = resutl->next;
    }
}

// https://leetcode.com/problems/remove-duplicates-from-sorted-list
// easy