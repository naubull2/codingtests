class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n

    def find(self, index):
        value = self.data[index]
        if value < 0: # root have negative value
            return index

        # other nodes will have its parent (root) value
        return self.data[index]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # merge will only compare root nodes, not current nodes
        if self.data[x] < self.data[y]:
            self.data[x] += self.data[y]
            self.data[y] = x
        else:
            self.data[y] += self.data[x]
            self.data[x] = y

        self.size -= 1


disjoint = DisjointSet(10)

disjoint.union(0, 1)
disjoint.union(1, 2)
disjoint.union(0, 3)
disjoint.union(4, 5)
disjoint.union(5, 6)
disjoint.union(6, 7)
disjoint.union(8, 9)

print(disjoint.data)
print(disjoint.size)
print()

for i in range(10):
    print(disjoint.find(i))
