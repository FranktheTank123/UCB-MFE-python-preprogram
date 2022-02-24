import pickle
from flask import Flask
from model_training import preping_data


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/USP/Desktop/Assignment_9/data/best_model.pkl', 'rb'))

    app.data, _ = preping_data('sqlite:////Users/USP/Desktop/Assignment_9/data/data.db')
    return app


app = creat_app()


@app.route("/")
def Assignment9():
    return "<p>This is the FINAL PROJECT!</p>"



@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    ret_sol = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)