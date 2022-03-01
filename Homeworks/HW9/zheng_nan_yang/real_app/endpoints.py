import pickle
import numpy as np

from flask import Flask, render_template, request
from model_training import preping_data


def creat_app():
    app = Flask(__name__, template_folder='templates')
    app.model = pickle.load(open("C:\\Users\\AndrewYang\\Desktop\\Python MFE Precourse\\UCB-MFE-python-preprogram\\Homeworks\\HW9\\zheng_nan_yang\\data\\wine_model.pckl", "rb"))
    # this is not the best way to do it
    # app.data = X
    app.data, _ = preping_data("C:\\Users\\AndrewYang\\Desktop\\Python MFE Precourse\\UCB-MFE-python-preprogram\\Homeworks\\HW9\\zheng_nan_yang\\data\\winequality_red.csv")
    return app

app = creat_app()


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/health_check")
def ping():
    return "pong"

@app.route('/home')
def form():
    return render_template('form.html')
 
@app.route('/result', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /result is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form

        X_test = np.array([v for _,v in form_data.items()])
        X_test = X_test.reshape(1,-1)
        res = app.model.predict(X_test)
        output = "Good" if res[0] == 1 else "Bad"

        # return "Wine Quality: " + output
        return render_template('output.html',form_data = form_data, output = output)


if __name__ == '__main__':
    app.run("localhost", port=5000)