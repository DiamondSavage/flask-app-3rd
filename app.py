from flask import Flask
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    environment = os.environ.get("APP_ENV", "Not Set")

    return f"""
<html>
<head>
<title>DevOps Demo</title>

<style>
body {{
    background:#1e1e1e;
    color:white;
    font-family:Arial;
    padding:40px;
}}

.card {{
    background:#2d2d2d;
    padding:25px;
    border-radius:10px;
    width:450px;
}}

h1 {{
    color:#4CAF50;
}}

p {{
    font-size:18px;
}}
</style>

</head>

<body>

<div class="card">

<h1>🚀 Docker + Flask Demo</h1>

<p><b>Hostname:</b> {hostname}</p>

<p><b>Current Time:</b> {current_time}</p>

<p><b>Environment:</b> {environment}</p>

<p><b>Container ID:</b> {hostname}</p>

</div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)