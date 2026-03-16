#!/usr/bin/env python3
"""Persistent array — immutable versioned array via fat nodes."""

class PersistentArray:
    def __init__(self, data=None):
        self._data = list(data) if data else []
        self._history = [list(self._data)]
    def set(self, idx, val):
        new = list(self._data); new[idx] = val
        self._data = new; self._history.append(list(new))
        return len(self._history) - 1
    def get(self, idx, version=None):
        v = self._history[version] if version is not None else self._data
        return v[idx]
    def version(self): return len(self._history) - 1
    def snapshot(self, ver): return list(self._history[ver])

def main():
    a = PersistentArray([1,2,3,4,5])
    print(f"v0: {a.snapshot(0)}")
    v1 = a.set(2, 99)
    print(f"v{v1}: {a.snapshot(v1)}")
    print(f"v0[2] = {a.get(2, 0)}, v{v1}[2] = {a.get(2, v1)}")

if __name__ == "__main__": main()
