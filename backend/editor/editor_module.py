import base64
import re
from io import BytesIO
from PIL import Image

from modules import color, size, compress, prikols


class Editor:
    def __init__(self, img):
        self.img = Editor.base64_to_pil(img)
        self.img.save('cur.jpg', 'JPEG')

    def parse(self, json_methods):
        self.img = color.parse(self.img,  json_methods['color'])
        self.img = size.parse(self.img,  json_methods['size'])
        self.img = compress.parse(self.img, json_methods['compress'])
        # self.img = prikols.parse(self.img,  json_methods['prikols'])
        return Editor.pil_to_base64(self.img, json_methods['compress'])

    def get_compress(self, rate):
        img, filesize = compress.get_bytes(self.img, rate)
        img = Editor.pil_to_base64(img)
        return img, filesize

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

    @staticmethod
    def pil_to_base64(img, rate=100):
        buffered = BytesIO()
        img.save(buffered, format="JPEG", quality=rate)
        buffered.seek(0)
        img_byte = buffered.getvalue()
        return "data:image/png;base64," + base64.b64encode(img_byte).decode()

