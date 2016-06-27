from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    import socket 
    return "Done by %s!" % socket.gethostname() 

app.run(host="0.0.0.0",
        port=5000,
        debug=True)
