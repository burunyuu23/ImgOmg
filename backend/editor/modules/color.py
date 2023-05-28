from PIL import ImageEnhance, ImageOps, Image


def parse(img, methods):
    for method, value in methods.items():
        match method:
            case 'brightness':
                if value != 100:
                    brightness_factor = value / 100
                    # Фактор яркости (больше 1 увеличит яркость, меньше 1 уменьшит)
                    enhancer = ImageEnhance.Brightness(img)
                    img = enhancer.enhance(brightness_factor)
            case 'saturation':
                if value != 100:
                    saturation_factor = value / 100
                    # Фактор насыщенности (больше 1 увеличит насыщенность, меньше 1 уменьшит)
                    enhancer = ImageEnhance.Color(img)
                    img = enhancer.enhance(saturation_factor)
            case 'contrast':
                if value != 100:
                    contrast_factor = value / 100
                    # Фактор контрастности (больше 1 увеличит контрастность, меньше 1 уменьшит)
                    enhancer = ImageEnhance.Contrast(img)
                    img = enhancer.enhance(contrast_factor)
            case 'sepia':
                if value != 0:
                    sepia_image = sepia_filter(img)
                    img = Image.blend(img, sepia_image, value/100)
            case 'grayscale':
                if value != 0:
                    enhancer = ImageEnhance.Color(img)
                    # Преобразование в оттенки серого с настройкой уровня (0.0 - полностью чёрно-белое, 1.0 - без изменений)
                    img = enhancer.enhance(1 - value / 100)
            case 'invert':
                if value != 0:
                    inverted_image = ImageOps.invert(img)
                    # Инвертирование с настройкой уровня (0.0 - без изменений, 1.0 - полностью инвертировано)
                    img = Image.blend(img, inverted_image, value / 100)
    return img


def sepia_filter(img):
    width, height = img.size
    sepia_data = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            sepia_data.append((tr, tg, tb))

    # Create a new image with the sepia data
    sepia_image = Image.new('RGB', (width, height))
    sepia_image.putdata(sepia_data)

    # Adjust the intensity
    return sepia_image.point(lambda i: i)
