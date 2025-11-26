from collections import deque


def is_palindrome(string: str):
    """Check if a string is a palindrome"""

    string = string.replace(" ", "").lower()
    d = deque(string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
