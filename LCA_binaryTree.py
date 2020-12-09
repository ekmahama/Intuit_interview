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
