import base64
import re
from io import BytesIO
from PIL import Image

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def base64_to_pil(img_base64):
    """
    Convert base64 image data to PIL image
    """
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    return pil_image


@app.route('/upload', methods=['POST'])
def index():
    input_json = request.get_json(force=True)

    img = base64_to_pil(input_json['image'])
    img.save('cur.jpg', 'JPEG')
    print(input_json)
    dictToReturn = {'image': input_json['image']}
    return jsonify(dictToReturn)


@app.route('/color')
def color():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=8081)
