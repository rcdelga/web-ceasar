from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
      <style>
          body {{
              background-color: black;
          }}
          form {{
              background-color: #888;
              padding: 20px;
              margin: 0 auto;
              width: 540px;
              font: 16px sans-serif;
              border-radius: 10px;
              font-family: Calibri;
              font-size: 20px;
          }}
          input {{
            border-radius: 5px;
          }}
          textarea {{
              margin: 10px 0;
              width: 540px;
              height: 120px;
              border-radius: 5px;
          }}
          #rot {{
            width: 35px;
            text-align: center;
          }}
      </style>
    </head>
    <body>
      <form method="POST">
        <label for="rot">Rotate by:</label>
        <input id="rot" name="rot" type="text" value="0"><br><br>
        <label for="text">Text to be encrypted:</label><br>
        <textarea type="text" name="text">{0}</textarea><br>
        <input type="submit">
      </form>
    </body>
    <footer>

    </footer>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    result = rotate_string(text,rot)

    return form.format(result)


@app.route("/")
def index():
    return form.format('')

app.run()