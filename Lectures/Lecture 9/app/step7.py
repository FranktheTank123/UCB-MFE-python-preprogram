import jsonschema
from flask import Flask
from flasgger import Swagger
from flask import request


def creat_app():
    app = Flask(__name__)
    app.swagger = Swagger(app)
    return app


app = creat_app()


@app.route("/ping")
def ping():
    """
    Indicates that the server is up
    ---
    tags: [housekeeping]
    responses:
      200:
        description: Server is up
      400:
        description: Server is dead
    """
    return "pong"


@app.route('/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return result


# curl -X POST localhost:5000/get_colors -d '{"palette": "all"}'
@app.route('/get_colors', methods=["POST"])
def get_colors():
    """A different way of getting colors
    This is using docstrings for specifications.
    ---
    parameters:
      - name: body
        in: body
        schema:
          id: get_color_input
          required: [palette]
          properties:
            palette:
              type: string
              enum: [all, rgb, cmyk]
              default: all
          example: {
            "palette": "all",
          }
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          id: get_color_output
          example:
            rgb: ['red', 'green', 'blue']
    """
    req = request.get_json(force=True)
    try:
        jsonschema.validate(
            req,
            schema=app.swagger.get_schema("get_color_input"),
            format_checker=jsonschema.FormatChecker(),
        )
    except jsonschema.exceptions.ValidationError:
        return "invalid input", 403
    palette = req['palette']
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return result


if __name__ == '__main__':
    app.run("localhost", port=5000)
