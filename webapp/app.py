from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    ip_x_for = ""
    if request.headers.getlist("X-Forwarded-For"):
        list_for = request.headers.getlist("X-Forwarded-For")
        for x in list_for:
            ip_x_for += "," + x
    ip_default = request.remote_addr
    return f"IP default: {ip_default} IP X for: {ip_x_for}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)