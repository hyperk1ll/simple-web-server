from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    client_ip = request.remote_addr
    return f"Your IP is {client_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
