from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/scan', methods=['POST'])
def create_scan():
    d = request.get_json(force=True)
    if not d:
        abort(400)
    id = request.json['id']
    ip = request.json['ip']
    start_port = request.json['start']
    end_port = request.json['end']
    print("id:%s" % id)
    return jsonify({'request': "Ok"}), 201

@app.route('/dump', methods=['POST'])
def dump():
    print(repr(request.get_json(force=True)))
    return jsonify({'request': "Ok"}), 201

@app.route('/scans/<scanid>', methods=['GET'])
def get_scanid(scanid):
    id = scanid
    print("Asking for results id:%s" % id)
    a = {'id': id, 'port': 123, 'state': 'ukn', 'service': 'ssh', 'reason': 'synack'}
    result_list = []
    result_list.append(a)
    print(repr(result_list))
    return jsonify({'results': result_list}), 201

@app.route('/scans', methods=['GET'])
def get_scans():
    print("Asking for all scans")
    a = {'id': 1, 'port': 22, 'state': 'ukn', 'service': 'ssh', 'reason': 'synack'}
    b = {'id': 2, 'port': 80, 'state': 'ukn', 'service': 'http', 'reason': 'synack'}
    result_list = []
    result_list.append(a)
    result_list.append(b)
    return jsonify({'results': result_list}), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=12345, debug=True)
