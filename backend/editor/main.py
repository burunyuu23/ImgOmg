import sys
from collections import defaultdict

from flask import Flask, request, jsonify, Blueprint, abort
from flask_cors import CORS

from editor_module import Editor

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
auth_bp = Blueprint('auth', __name__, url_prefix='/api/editor')

editors = defaultdict(dict)


@auth_bp.route('/upload', methods=['POST'])
def upload():
    global editors

    input_json = request.get_json(force=True)
    req = input_json['req']

    login = input_json['login']
    editor = Editor(req['image'])
    editors[login] = editor

    img = editor.parse(req['methods'])

    dictToReturn = {'image': img}
    return jsonify(dictToReturn)


@auth_bp.route('/compress_size', methods=['POST'])
def compress_size():
    global editors

    input_json = request.get_json(force=True)

    login = input_json['login']
    if not editors[login]:
        return abort(403)
    editor = editors[login]

    img = editor.get_compress(input_json['rate'])

    dictToReturn = {'image': img}
    return jsonify(dictToReturn)


@auth_bp.route('/pre_prikol', methods=['POST'])
def pre_prikol():
    global editors

    input_json = request.get_json(force=True)

    login = input_json['login']
    if not editors[login]:
        return abort(403)
    editor = editors[login]

    img, file = editor.get_prikol(input_json['prikol'])

    dictToReturn = {'image': img, 'file': file}
    return jsonify(dictToReturn)


app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True, port=int(sys.argv[1]), host='0.0.0.0')
