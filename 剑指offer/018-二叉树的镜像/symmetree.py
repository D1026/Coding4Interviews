class TreeNode:
    def __init__(self, x, lc=None, rc=None):
        self.val = x
        self.lc = lc
        self.rc = rc

def symmetry(root):
    if not root:
        return root
    if not root.lc and not root.rc:
        return root
    else:
        root.lc, root.rc = root.rc, root.lc
        symmetry(root.lc)
        symmetry(root.rc)
        return root