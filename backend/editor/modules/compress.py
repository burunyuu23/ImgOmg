from PIL import Image
import io


def compress(img, rate):
    output_buffer = io.BytesIO()
    img.save(output_buffer, format='JPEG', quality=rate)
    output_buffer.seek(0)

    return output_buffer.getvalue()


def parse(img, methods):
    compress_rate = methods

    if compress_rate > 100:
        return img
    return Image.open(io.BytesIO(compress(img, compress_rate)))
