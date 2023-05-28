import base64
import re
from io import BytesIO
from PIL import Image

from modules.color import Color
from modules.compress import Compress
from modules.prikols import Prikols
from modules.size import Size


class Editor:
    def __init__(self, img, json_methods):
        self.img = Editor.base64_to_pil(img)
        self.img.save('cur.jpg', 'JPEG')

        self.color = Color(json_methods['color'])
        self.size = Size(json_methods['size'])
        self.compress = Compress(json_methods['compress'])
        self.prikols = Prikols(json_methods['prikols'])

    def parse(self):
        self.color.parse()
        self.size.parse()
        self.compress.parse()
        self.prikols.parse()

    @staticmethod
    def base64_to_pil(img_base64):
        """
        Convert base64 image data to PIL image
        """
        image_data = re.sub('^data:image/.+;base64,', '', img_base64)
        pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
        if pil_image.mode != "RGB":
            pil_image = pil_image.convert("RGB")
        return pil_image

