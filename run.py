from flask import Flask
app = Flask(__name__)

print("Crashing...")
return -1

@app.route("/")
def root():
    import socket 
    return "Version 0.3 by %s!" % socket.gethostname() 

app.run(host="0.0.0.0",
        port=5000,
        debug=True)
