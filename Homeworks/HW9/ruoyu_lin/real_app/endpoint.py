import pickle
from flask import Flask 
from model_train import prep_data
import os
from flask import send_from_directory

DIR_DATA = os.getcwd().replace("real_app", "data")

def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open(os.path.join(DIR_DATA, "model.pkl"), "rb"))
    app.data, _ = prep_data(os.path.join(DIR_DATA, "pricedata.csv"))
    
#     * ADD MORE STUFF * 
    
    return app 

app = creat_app()


@app.route("/")
def main_page():
    return """
    <p>This is an app to predict BTC returns using other coins, cny-usd forex data and spy. 
    Created by Ruoyu Lin in Feb. 2022.</p> \n
    \n
    <p>Enter date of format "2019-08-07" to localhost:port/yyyy-mm-dd to obtain model prediction. </p>
    
    """

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/test/<string:s>")
def dynamic_health_check(s: str):
    return f"{s}"

@app.route("/<string:date>")
def predict_ret_btc(date: str):
    # date input must be of form yyyy-mm-dd e.g. 2022-02-24
    ret = app.model.predict(
        app.data.loc[date].to_frame().T
    )[0]
    return {"ret_btc": str(ret)}


# Write more functions like this if needed 
# @app.route() 
# def 

if __name__ == "__main__":
    app.run("localhost", port = 5555)