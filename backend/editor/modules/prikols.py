import base64
import os
import cv2
import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps
import random


def parse(img, method):
    prikol = method['prikol']
    file = method['file']
    return base(img, prikol, file)[0]


def base(img, prikol, file):
    match prikol:
        case 'D̸̦̘̾͊͜͝R̵̠͕͛̐͜͝A̵̡̞̟͛̕͝I̵͍͓͓͊̓͘N̵͉̙̈́̈́͊͜ S̵̡͉͔͑̈́̒T̴̻̟̙̈́͠͠Ý̸̼̼͆̀͜L̸̡͕͚͒̽͝E̴͔͕͙͐͆́':
            img = overlay_images(img, f'drain_gang_effects/{file}')
        case '𝕖𝕝𝕖𝕘𝕒𝕟𝕥':
            img = overlay_images(img, 'elegant/zern.jpg')
            img = apply_vignette(img)
        case 'sudo rm -fr /background --no-preserve-root':
            img = remove_background()
    return img, file


def pre_parse(img, method):
    file = random.choice(os.listdir('drain_gang_effects'))
    method = method['prikol']
    return base(img, method, file)


def overlay_images(img, overlay_path):
    background = img.convert('RGB')
    overlay = Image.open(overlay_path).convert('RGB')

    if background.size != overlay.size:
        overlay = overlay.resize(background.size)

    blended_image = ImageChops.screen(background, overlay)

    blended_image.save('cur_prikols.jpg')
    return blended_image


def remove_background():
    image = cv2.imread('cur.jpg')
    # Create a mask initialized with zeros
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define the rectangle enclosing the object of interest
    rectangle = (10, 10, image.shape[1] - 30, image.shape[0] - 30)

    # Apply GrabCut algorithm to segment the image and refine the mask
    cv2.grabCut(image, mask, rectangle, None, None, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where foreground and possible foreground pixels are marked as likely
    mask_likely = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Apply the mask to the original image
    result_image = cv2.bitwise_and(image, image, mask=mask_likely)

    rgb_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb_image)


def apply_vignette(image):
    # Create a circular mask with a radial gradient
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.width, image.height), fill=255, outline=0)
    vignette = ImageOps.fit(mask, (image.width, image.height))

    # Apply blur effect to the vignette mask
    blurred_vignette = vignette.filter(ImageFilter.GaussianBlur(radius=image.width/10))

    # Apply the blurred vignette mask to the image
    result = Image.new('RGB', image.size)
    result.paste(image, mask=blurred_vignette)

    return result

