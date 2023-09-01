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

int maxDepth(TreeNode* root) {

    if (!root) return 1;

    return max(maxDepth(root->right)+1, maxDepth(root->left)+1);

}

int main(){

}

// https://leetcode.com/problems/maximum-depth-of-binary-tree/
// easy