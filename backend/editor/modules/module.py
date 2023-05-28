class Module:
    def __init__(self, methods):
        self.methods = methods

    def parse(self):
        for method in self.methods:
            print(method)
