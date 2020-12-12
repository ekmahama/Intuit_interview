def LCA(root, p, q):
    if not root:
        return None

    if root.val == q.val or root.val == p.val:
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left:
        return right
    if right:
        return left

    return root


def LCA_BST(root, p, q):
    if p.val < root.val and q.val < root.val:
        return LCA_BST(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return LCA_BST(root.right, p, q)
    return root
