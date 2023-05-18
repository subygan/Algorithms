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

int minDepth(TreeNode* root) {

    if (root == NULL) return 0;

    int rh = minDepth(root->right);
    int lh = minDepth(root->left);
    if (rh == 0 || lh ==0) return lh + rh +1;

    return (lh >= rh) ? rh+1:lh+1;
}

TreeNode * makeBst(vector<int> &nums, int start, int end ) {
    if (start>end) return NULL;
    int mid = (start + end)/2;
    TreeNode * root = new TreeNode(nums[mid]);

    root->left = makeBst(nums,start, mid-1);
    root->right = makeBst(nums,mid+1, end);
    return root;
}

int main(){

//    vector<int> leftVec = {2,NULL,3,NULL,4,NULL,5,NULL,6};
    vector<int> leftVec = {3,9,20,NULL, NULL,15,7};
    TreeNode *t = makeBst(leftVec,0,leftVec.size());
    cout<<minDepth(t);
}

// https://leetcode.com/problems/balanced-binary-tree/
// easy