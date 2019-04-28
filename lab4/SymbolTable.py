from copy import deepcopy


class VariableSymbol(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):

    def __init__(self, parent, name):  # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.entries = {}

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.entries[name] = symbol

    def get(self, name):  # get variable symbol or fundef from <name> entry
        if name in self.entries.keys():
            return self.entries[name]
        else:
            return None

    def get_parent_scope(self):
        return self.parent

    def push_scope(self, name):
        new_scope = SymbolTable(self, name)
        new_scope.name = name
        new_scope.parent = self
        new_scope.entries = deepcopy(self.entries)
        return new_scope

    def pop_scope(self):
        parent_scope = self.get_parent_scope()
        if parent_scope is None:
            print('Cannot pop root scope')
        return parent_scope
