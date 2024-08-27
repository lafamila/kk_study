from enum import Enum


class Act(Enum):
    PUSH = 1
    POP = -1


class Brackets(Enum):
    PARENTHESES = 1
    CURLY = 2
    SQUARE = 3


class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": (Brackets.PARENTHESES, Act.PUSH), ")": (Brackets.PARENTHESES, Act.POP),
            "{": (Brackets.CURLY, Act.PUSH), "}": (Brackets.CURLY, Act.POP),
            "[": (Brackets.SQUARE, Act.PUSH), "]": (Brackets.SQUARE, Act.POP)
        }
        stack = list()
        for c in s:
            bracket, act = map[c]
            if act == Act.PUSH:
                stack.append(bracket)
            elif stack:
                out = stack.pop(-1)
                if out != bracket:
                    return False
            else:
                return False

        return False if stack else True
