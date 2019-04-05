from flask import Flask, request
from caesar import rotate_string, rotate_character
import math

app=Flask(__name__)
app.config["DEBUG"] = True
form= """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
        <label for="rot">rotate by:</label>
        <input type="text" id="rot" name="rot" value="0">
        <textarea type="text" name="text" rows="4" cols="50">{0}</textarea>
        <input type="submit">
        
        </form>
    </body>
</html>
"""
@app.route("/", methods=["POST"])
def encrypt():
    text = request.form["text"]
    rot = int(request.form["rot"])

    rotate = rotate_string(text, rot)
    return form.format(rotate)

@app.route("/")
def index():
    return form.format()



app.run()