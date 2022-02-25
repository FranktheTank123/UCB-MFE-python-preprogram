import json
import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from model_definition import labels, mdl_predict

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads/"

app.secret_key = "mfe_python"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in set(
        ["png", "jpg", "jpeg"]
    )


@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def get_output():
    if request.method == "POST":
        p = []
        animal = ""
        img_path = ""
        img = request.files["img_file"]
        # print(allowed_file(img.filename))
        if allowed_file(img.filename):
            filename = secure_filename(img.filename)
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            img.save(img_path)

            p, animal = mdl_predict(img_path)

    return render_template(
        "index.html",
        pred=json.dumps(p),
        animal=animal,
        label=json.dumps(labels),
        img_path=img_path,
    )


if __name__ == "__main__":
    # app.run(debug=True)
    app.run("localhost", port=5000)
