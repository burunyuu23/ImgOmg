from PIL import Image


def parse(img, methods):
    (x, w, y, h) = methods
    crop = (x, y, w, h)

    if not(x == 0 and y == 0 and w == img.size[0] and h == img.size[1]\
            or crop == (0, 0, 0, 0)):
        img_crop = Image.new(color=0, size=(w - x, h - y), mode="RGB")
        img_crop.paste(img.crop(crop), (0, 0, w - x, h - y))
        img_crop.save('cur_size.jpg', 'JPEG')
        return img_crop
    return img
