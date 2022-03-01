import pickle

from flask import Flask
from model_training import prep_data
from blue_prints.UI import UI_routes
from blue_prints.model import model_routes


def creat_app():
    app = Flask(__name__)
    app.register_blueprint(UI_routes)
    app.register_blueprint(model_routes)
    app.config['model'] = pickle.load(open('data/best_model.pkl', 'rb'))
    app.config['data'], _ = prep_data('data/Data_PGUN.csv')
    return app


if __name__ == '__main__':
    app = creat_app()
    app.run("localhost", port=5000)
