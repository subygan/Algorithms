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


vector<int> inorderTraversal(TreeNode* root) {

    if (root==NULL) return {};
    vector<int> res = inorderTraversal(root->left);
    res.push_back(root->val);
    for (auto i: inorderTraversal(root->right)) res.push_back(i);

    return res;
}

int main(){

}
// https://leetcode.com/problems/binary-tree-inorder-traversal/
// easy