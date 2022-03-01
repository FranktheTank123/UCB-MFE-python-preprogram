from flask import Blueprint


UI_routes = Blueprint("UI_routes", __name__)


@UI_routes.route('/')
def hello_world():
    return "<h1>WELCOME</h1> Pages available :<ul><li>health_check</li><li>predict</li></ul> "

@UI_routes.route("/predict")
def predict_landing():
    return "<h4>This app lets you predict the monthly excess returns of Unilever stock</h4> Kindly use predict/YYYY-MM-DD to get the returns, 1994-01-31 to 2015-12-31"

@UI_routes.route("/health_check")
def ping():
    return "Status : OK"
