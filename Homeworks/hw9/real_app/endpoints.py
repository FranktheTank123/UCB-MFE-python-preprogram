from flask import Flask
import pickle
from model_training import preping_data,return_vol,return_all

def app_create():
    app= Flask(__name__)
    app.model = pickle.load(open('D:/flask/T1/Data/finalized_model.pckl', 'rb'))
    app.data, _ = preping_data('sqlite:///D:/flask/T1/Data/data.db')
    return app

app = app_create()

@app.route("/")
def home():
    return "Hello, World!"

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

if __name__ == "__main__":
    app.run()