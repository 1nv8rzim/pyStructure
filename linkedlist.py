class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

    def __str__(self):
        return f'Node({self.value},{self.rest})'

    def __repr__(self):
        return str(self)


class LList:
    def __init__(self, *args):
        self.root = None
        self.size = 0
        for arg in args:
            self.add(arg)

    def add(self, element, index=0):
        if not index:
            self.root = Node(element, self.root)
            self.size += 1
        else:
            try:
                self.root = self.adder(
                    self, element, self.root, index if index > 0 else index + len(self))
            except:
                IndexError(f'Cannot reach index {index}')

    def adder(self, element, reference, index):
        if index < 0:
            raise IndexError()
        if not index:
            self.size += 1
            return Node(element, reference)
        if reference is None:
            raise IndexError()
        return self.adder(element, reference.rest, index - 1)

    def __len__(self):
        return self.size
