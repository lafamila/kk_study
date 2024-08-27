from enum import Enum


class Act(Enum):
    PUSH = 1
    POP = -1


class Brackets(Enum):
    PARENTHESES = 1
    CURLY = 2
    SQUARE = 3


class Stack:
    class Node:
        def __init__(self, value):
            self._value = value
            self._next = None

        def connect(self, node):
            self._next = node

    def __init__(self):
        self._head = None
        self._count = 0

    def __len__(self):
        return self._count

    def push(self, value):
        node = self.Node(value)
        if len(self) > 0:
            temp = self._head
            node.connect(temp)
        self._head = node
        self._count += 1

    def pop(self):
        if len(self) == 0:
            raise Exception("Stack Is Empty")
        temp = self._head
        self._head = temp._next
        self._count -= 1
        return temp._value

    def act(self, action, value):
        if action == Act.PUSH:
            self.push(value)
            return None
        else:
            return self.pop()


class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": (Brackets.PARENTHESES, Act.PUSH), ")": (Brackets.PARENTHESES, Act.POP),
            "{": (Brackets.CURLY, Act.PUSH), "}": (Brackets.CURLY, Act.POP),
            "[": (Brackets.SQUARE, Act.PUSH), "]": (Brackets.SQUARE, Act.POP)
        }
        stack = Stack()
        for c in s:
            bracket, action = map[c]
            try:
                out = stack.act(action, bracket)
                if out is not None and out != bracket:
                    return False
            except:
                return False

        return False if len(stack) else True
