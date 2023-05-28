from modules.module import Module


class Compress(Module):
    def __init__(self, methods):
        super().__init__(methods)

    def parse(self):
        compress_rate = self.methods
