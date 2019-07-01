#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
import qrcode
import base64
from io import BytesIO
from flask import send_file
app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

@app.route('/')
def hello_world():
    return render_template('qr_tool.html')


@app.route('/cal',methods=['POST','GET'])
def cal():
    if request.method == 'GET':
        num1 = request.args.get('num1','')
        num2 = request.args.get('num2','')
        num = str(int(num1) + int(num2))
        return render_template('hello.html', num1=num1,num2=num2,num=num)
        # return num
    else:
        return 'error'


@app.route('/qrcode',methods=['POST','GET'])
def qr_code():
    if request.method == 'GET':
        data = request.args.get('msg','')
        
        img = qrcode.make(data)
        byte_io = BytesIO()
        img.save(byte_io, 'PNG')
        byte_io.seek(0)
        return send_file(byte_io, mimetype='image/png', cache_timeout=0)
    else:
        return 'error'

if __name__=='__main__':
    app.run(debug=True, host="0.0.0")