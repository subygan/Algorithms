#include <iostream>
#include <vector>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


TreeNode * makeBst(vector<int> &nums, int start, int end ) {
    if (start>end) return NULL;
    int mid = (start + end)/2;
    TreeNode * root = new TreeNode(nums[mid]);

    root->left = makeBst(nums,start, mid-1);
    root->right = makeBst(nums,mid+1, end);
    return root;
}

TreeNode *sortedArrayToBST(vector<int> &nums) {
    return makeBst(nums, 0, nums.size()-1);
}


int main() {

    vector<int> leftVec = {-10, -3, 0, 5, 9};
    TreeNode *t = sortedArrayToBST(leftVec);
//    cout<<t->val<<" "<<t->right->val<<" "<<t->left->val<<" ";
//    cout<<t->val<<" "<<t->right<<" "<<t->left<<" ";


//    vector<int> v = inorderTraversal(sortedArrayToBST(leftVec));
//    for_each(v.begin(), v.end(),[](int number){cout << number << ";";});
//    cout<<endl<<"------------";
}

// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
// easy