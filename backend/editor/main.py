from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from editor_module import Editor

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/upload', methods=['POST'])
def index():
    input_json = request.get_json(force=True)

    print(input_json)

    editor = Editor(input_json['image'], input_json['methods'])
    editor.parse()

    dictToReturn = {'image': input_json['image']}
    return jsonify(dictToReturn)


@app.route('/color')
def color():
    pass


if __name__ == '__main__':
    app.run(debug=True, port=8081)
