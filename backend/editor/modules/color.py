from modules.module import Module


class Color(Module):
    def __init__(self, methods):
        super().__init__(methods)

    def parse(self):
        for method, value in self.methods.items():
            match method:
                case 'brightness':
                    if value != 100:
                        pass
                case 'saturation':
                    if value != 100:
                        pass
                case 'contrast':
                    if value != 100:
                        pass
                case 'sepia':
                    if value != 0:
                        pass
                case 'grayscale':
                    if value != 0:
                        pass
                case 'invert':
                    if value != 0:
                        pass
