
from flask import Flask, request
import  requests
import json

app = Flask(__name__)

@app.route('/')
def query():
    ip= request.args.get('ip')
    api_req = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey=4d505bdce1a54968a93c185c6131e907&ip={ip}&fields=time_zone")
    api_req_json = json.loads(api_req.text)
    api_req_json_value = (api_req_json['time_zone']['name'])

    return api_req_json_value

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

