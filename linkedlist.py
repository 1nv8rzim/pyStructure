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

    def remove(self, index=0):
        if not index:
            if self.root is None:
                raise IndexError('Cannot remove index that does not exist')
            self.root = self.root.rest
        else:
            self.root = self.remover(index, self.root)

    def remover(self, index, reference):
        if index < 0:
            raise IndexError()
        if not index:
            if reference is None:
                raise IndexError()
            self.size -= 1
            return reference.rest
        if reference is None:
            raise IndexError()
        return self.remover(index - 1, reference.rest)

    def __str__(self):
        reference = self.root
        temp = []
        while reference is not None:
            temp.append(reference.value)
            reference = reference.rest
        return str(temp)

    def __repr__(self):
        return 'LList({})'.format(str(self)[1:-1])

    def contains(self, element):
        for i in self:
            if self == element:
                return True
        return False

    def __iter__(self):
        reference = self.root
        temp = []
        while reference is not None:
            temp.append(reference.value)
            reference = reference.rest
        return iter(temp)

    def __eq__(self, element):
        if not isinstance(element, LList):
            return False
        if len(element) != len(self):
            return False
        for i, j in zip(self, element):
            if i != j:
                return False
        return True

    def __ne__(self, element):
        return not self == element
