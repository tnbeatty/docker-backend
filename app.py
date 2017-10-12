from flask import Flask, render_template, request, make_response, g
import os
import socket
import random
import json

hostname = socket.gethostname()

app = Flask(__name__)

@app.route("/", defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def hello(path):
    dbk_client_id = request.cookies.get('dbk_client_id')
    if not dbk_client_id:
        dbk_client_id = hex(random.getrandbits(64))[2:-1]

    # Do some stuff with the cookie here

    resp = make_response(render_template(
        'index.html',
        hostname=hostname,
        path=path
    ))
    resp.set_cookie('dbk_client_id', dbk_client_id)

    print('\n\n+------ NEW REQUEST ------+\n')

    print('Received by %s'%hostname)

    print(request.headers)
    print(request.base_url, request.host_url, request.host)

    print('\n+------ END ------+\n')

    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
