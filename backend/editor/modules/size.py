from modules.module import Module


class Size(Module):
    def __init__(self, methods):
        super().__init__(methods)

    def parse(self):
        x, w, y, h = self.methods
