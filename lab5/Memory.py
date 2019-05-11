class Memory:

    def __init__(self, name):
        self.name = name
        self.memory = {}

    def contains_key(self, name):
        return name in self.memory.keys()

    def get(self, name):
        return self.memory.get(name)

    def put(self, name, value):
        self.memory[name] = value

    def __repr__(self):
        return self.name


class MemoryStack:

    def __init__(self, memory=None):
        self.stack = [memory] if memory else [Memory("Top Level")]

    def get(self, name):
        indices = reversed(range(0, len(self.stack)))
        for i in indices:
            if self.stack[i].contains_key(name):
                return self.stack[i].get(name)
        # return None

    def insert(self, name, value):
        self.stack[-1].put(name, value)

    def set(self, name, value):
        indices = reversed(range(0, len(self.stack)))
        for i in indices:
            if self.stack[i].contains_key(name):
                self.stack[i].put(name, value)

    def push(self, memory):
        self.stack.append(memory)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
