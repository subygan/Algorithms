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


int check(TreeNode *node, bool& balanced) {

    if (node == NULL || !balanced) return 0;

    int lh = check(node->left,balanced);
    int rh = check(node->right,balanced);

    if (abs(lh-rh) >1) balanced = false;

    return max(lh,rh)+1;
}

bool isBalanced(TreeNode* root) {
    bool result = true;
    check(root,result);
    return result;
}

int main(){

}

// https://leetcode.com/problems/balanced-binary-tree/
// easy