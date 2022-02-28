import pickle

from flask import Flask
from model_training import preping_data


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/xiaotong/UCB-MFE-python-preprogram/Ruitong_Xiao/trained_model.pckl', 'rb'))
    # this is not the best way to do it
    # app.data = X
    app.data, _ = preping_data('sqlite:///Users/xiaotong/UCB-MFE-python-preprogram/Ruitong_Xiao/data.db')
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/all/<string:token>/<string:time_stamp>")
def ret_all(token:str, time_stamp:str):
    val=[]
    val=return_all(token,time_stamp)
    return {"VOl_"+str(token):val[0],"RET_"+str(token):val[1],"Hourly_Return_"+token:val[2]}

@app.route("/<string:token>/<string:time_stamp>")
def ret_vol(token:str, time_stamp:str):
    r=return_vol(token,time_stamp)
    return {"VOl_"+str(token):r}

@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)
