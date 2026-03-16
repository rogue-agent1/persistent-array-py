"""Persistent Array — immutable array with O(log n) updates."""
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo == hi: return Node(val=arr[lo])
    mid = (lo + hi) // 2
    return Node(left=build(arr, lo, mid), right=build(arr, mid+1, hi))

def get(root, idx, lo=0, hi=None):
    if hi is None: hi = root_size[0] - 1
    if lo == hi: return root.val
    mid = (lo + hi) // 2
    if idx <= mid: return get(root.left, idx, lo, mid)
    return get(root.right, idx, mid+1, hi)

def update(root, idx, val, lo=0, hi=None):
    if hi is None: hi = root_size[0] - 1
    if lo == hi: return Node(val=val)
    mid = (lo + hi) // 2
    if idx <= mid: return Node(left=update(root.left, idx, val, lo, mid), right=root.right)
    return Node(left=root.left, right=update(root.right, idx, val, mid+1, hi))

root_size = [0]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    root_size[0] = len(arr)
    v0 = build(arr)
    assert get(v0, 2) == 3
    v1 = update(v0, 2, 99)
    assert get(v0, 2) == 3  # old version unchanged
    assert get(v1, 2) == 99  # new version updated
    v2 = update(v1, 0, 42)
    assert get(v0, 0) == 1
    assert get(v2, 0) == 42
    assert get(v2, 2) == 99
    print("Persistent array: 3 versions coexist correctly")
    print("All tests passed!")
