import sys

from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS, cross_origin

from editor_module import Editor

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
auth_bp = Blueprint('auth', __name__, url_prefix='/api/editor')

editor = ''


@auth_bp.route('/upload', methods=['POST'])
def upload():
    global editor

    input_json = request.get_json(force=True)

    editor = Editor(input_json['image'])
    img = editor.parse(input_json['methods'])

    dictToReturn = {'image': img}
    return jsonify(dictToReturn)


@auth_bp.route('/compress_size', methods=['POST'])
def compress_size():
    global editor

    input_json = request.get_json(force=True)

    img, size = editor.get_compress(input_json['rate'])

    dictToReturn = {'image': img, 'size': size}
    return jsonify(dictToReturn)


@auth_bp.route('/pre_prikol', methods=['POST'])
def pre_prikol():
    global editor

    input_json = request.get_json(force=True)

    img, file = editor.get_prikol(input_json['prikol'])

    dictToReturn = {'image': img, 'file': file}
    return jsonify(dictToReturn)


app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True, port=int(sys.argv[1]), host='0.0.0.0')
