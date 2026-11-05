def constant(items):
    steps = 1
    first = items[0]
    return steps


def linear(items):
    steps = 0
    for item in items:
        steps += 1
    return steps


def quadratic(items):
    steps = 0
    for a in items:
        for b in items:
            steps += 1
    return steps


data = [10, 20, 30, 40, 50]

print("O(1):", constant(data))
print("O(n):", linear(data))
print("O(n²):", quadratic(data))


class Stack:
    def __init__(self):
        self._items = []

    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack ცარიელია")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


def reverse_text(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == reverse_text(cleaned)


print(reverse_text("Python"))
print(reverse_text("გამარჯობა"))
print(is_palindrome("level"))
print(is_palindrome("Race car"))
print(is_palindrome("hello"))