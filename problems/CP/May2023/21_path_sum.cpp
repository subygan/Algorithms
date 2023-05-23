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

bool check(TreeNode *root, int targetSum, int curSum) {
}

bool hasPathSum(TreeNode *root, int targetSum) {

    if (root == NULL) return false;
    if (root->left == NULL && root->right == NULL && root->val == targetSum) return true;

    return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
}

int main() {

}

//