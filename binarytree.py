class Node:
    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return f'Node({self.value}, {self.left}, {self.right})'

    def __repr__(self):
        return f'Node({self.value}, {self.left}, {self.right})'


class BTree:

    def __init__(self, kind, *args):
        if not isinstance(kind, type):
            raise TypeError(f'{kind} is not of type type')
        if not (hasattr(kind, '__lt__') and hasattr(kind, '__gt__') and hasattr(kind, '__gt__')):
            raise TypeError(f'{kind} cannot be compared')
        self.size = 0
        self.kind = kind
        self.root = None
        self.temp_tree = None
        for node in args:
            self.add(node)

    def add(self, element):
        if not isinstance(element, self.kind):
            raise TypeError(f'{element} is not of type {self.kind}')
        self.root = self.adder(element, self.root)

    def adder(self, element, reference, increment_size=True):
        if reference is None:
            if increment_size:
                self.size += 1
            reference = Node(element, None, None)
        elif reference.value < element:
            reference.right = self.adder(
                element, reference.right, increment_size)
        elif reference.value > element:
            reference.left = self.adder(
                element, reference.left, increment_size)
        return reference

    def remove(self, element):
        if not isinstance(element, self.kind):
            raise TypeError(f'{element} is not of type {self.kind}')
        self.root = self.remover(element, self.root)
        if not self.temp_tree is None:
            temp = BTree(self.kind)
            temp.root = self.temp_tree
            self.temp_tree = None
            for node in temp:
                self.root = self.adder(node, self.root, False)

    def remover(self, element, reference):
        if reference is None:
            return None
        elif reference.value < element:
            reference.right = self.remover(element, reference.right)
        elif reference.value > element:
            reference.left = self.remover(element, reference.left)
        elif reference.value == element:
            self.size -= 1
            if reference.right is None:
                self.temp_tree = reference.left
                reference = reference.right
            else:
                self.temp_tree = reference.right
                reference = reference.left
        return reference

    def prefix(self):
        return self.prefix_string()

    def prefix_string(self):
        def interior(reference=self.root):
            if reference is None:
                return []
            else:
                return [reference.value] + interior(reference.left) + interior(reference.right)
        return interior()

    def infix(self):
        return self.infix_list()

    def infix_list(self):
        def interior(reference=self.root):
            if reference is None:
                return []
            else:
                return [] + interior(reference.left) + [reference.value] + interior(reference.right)
        return interior()

    def postfix(self):
        return self.postfix_list()

    def postfix_list(self):
        def interior(reference=self.root):
            if reference is None:
                return []
            else:
                return [] + interior(reference.left) + interior(reference.right) + [reference.value]
        return interior()

    def contains(self, element):
        if not isinstance(element, self.kind):
            return False
        return self.container(element, self.root)

    def container(self, element, reference):
        if reference is None:
            return False
        elif element < reference.value:
            return self.container(element, reference.left)
        elif element > reference.value:
            return self.container(element, reference.right)
        return True

    def __str__(self):
        return self.infix_string()

    def __repr__(self):
        return 'BTree({}{})'.format(str(self.kind).split("'")[1], ', ' + str(self.infix_list())[1:-1] if len(self) else '')

    def __iter__(self):
        return iter(self.prefix_string())

    def __len__(self):
        return self.size

    def __eq__(self, element):
        if not isinstance(element, BTree):
            return False
        if not element.kind == self.kind:
            return False
        elif len(element) != len(self):
            return False
        return element.prefix() == self.prefix()

    def __ne__(self, element):
        return not self == element

    def copy(self):
        temp = BTree(self.kind)
        for element in self:
            temp.add(element)
        return temp

    def __add__(self, element):
        clone = self.copy()
        if not isinstance(element, self.kind) and not hasattr(element, '__iter__'):
            raise TypeError(
                f'{element} cannot be added to BTree of type {self.type}')
        if hasattr(element, '__iter__'):
            for i in element:
                if isinstance(i, self.kind):
                    raise TypeError(
                        f'{element} cannot be added to BTree of type {self.type}')
                clone.add(element)
        else:
            clone.add(element)

    def __getitem__(self, position):
        return self.infix()[position]
