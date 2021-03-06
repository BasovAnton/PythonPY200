from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DLNode(Node):
    def __init__(self, value, next_: Optional["DLNode"] = None, prev_: Optional["DLNode"] = None):
        super().__init__(value, next_)
        self.prev = prev_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DLNode"]):
        self.is_valid(prev_)
        self._prev = prev_

    def __repr__(self) -> str:
        next_ = None if self.next is None else f"DLNode({repr(self.next.value)})"
        prev_ = None if self.prev is None else f"DLNode({repr(self.prev.value)})"
        return f"DLNode({repr(self.value)}, {next_}, {prev_})"


dln_1 = DLNode("1")
dln_2 = DLNode("2")
dln_3 = DLNode("3")

dln_1.next = dln_2
dln_2.next = dln_3

dln_3.prev = dln_2
dln_2.prev = dln_1

print(repr(dln_2))
