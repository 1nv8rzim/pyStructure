from typing import Union, Any


class BTree:

    class Node:
        def __init__(self, value, rest):
            if isinstance(rest, Union[Node, None]):
                raise TypeError(f'{rest} is not type of Node or None')
            self.value = value
            self.rest = rest

        def __str__(self):
            return f'Node({self.value}, {self.rest})'

        def __repr__(self):
            return f'Node({self.value}, {self.rest})'

    def __init__(self, kind, *args):
        pass

    def add(self, element):
        pass

    def remove(self, element):
        pass

    def prefix(self):
        pass

    def infix(self):
        pass

    def postfix(self):
        pass

    def contains(self, element):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __eq__(self, element):
        pass

    def __ne__(self, element):
        pass

    def copy(self):
        pass

    def __getitem__(self, position):
        pass
