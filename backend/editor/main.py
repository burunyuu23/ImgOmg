from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from editor_module import Editor
from modules import compress

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

editor = ''


@app.route('/upload', methods=['POST'])
def upload():
    global editor

    input_json = request.get_json(force=True)

    print(input_json)

    editor = Editor(input_json['image'])
    img = editor.parse(input_json['methods'])

    dictToReturn = {'image': img}
    return jsonify(dictToReturn)


@app.route('/compress_size', methods=['POST'])
def compress_size():
    global editor

    input_json = request.get_json(force=True)

    img, size = editor.get_compress(input_json['rate'])

    dictToReturn = {'image': img, 'size': size}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(debug=True, port=8081)
