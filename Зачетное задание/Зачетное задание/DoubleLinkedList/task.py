from typing import Any, Iterable, Optional
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def insert(self, index: int, value) -> None:
        if not isinstance(index, int):
            raise TypeError()
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1

        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)
            self._len += 1

    def __delitem__(self, index: int) -> None:

        """Удаление узла по индексу"""
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:
            raise IndexError()

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
            self._tail = tail
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def __len__(self) -> int:
        return self._len

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.CLASS_NODE(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


class DoubleLinkedList(LinkedList):
    CLASS_NODE = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node


class NewLinkedList(LinkedList):

    def remove_(self, x):
        # s = 0
        # for i in range(self._len):
        #     s += 1
        #     if self[i] == x:
        #         self.__delitem__(i)  # del self[i]
        #         break
        #     if self._len == s:
        #         raise TypeError

        for i, value in enumerate(self):
            if value == x:
                self.__delitem__(i)  # del self[i]
                break

        if i == len(self) - 1:
            raise TypeError


if __name__ == "__main__":
    list_ = [5, 2, 3, 7, 9]
    linked_list = LinkedList(list_)
    print(linked_list)
    print(linked_list.__repr__())

    linked_list_2 = NewLinkedList(list_)
    linked_list_2.remove_(5)
    print(linked_list_2)
