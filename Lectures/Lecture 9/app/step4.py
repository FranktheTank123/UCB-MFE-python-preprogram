from flask import Flask
import pandas as pd
import time


def creat_app():
    app = Flask(__name__)
    app.df = pd.DataFrame()  # connect_sql(DATA_BASE_PATH)
    # app.model = load_model
    # app.data = load_data
    return app


app = creat_app()


@app.route("/")
def return_df_shape():
    return f"app.df is of shape: {app.df.shape}"


@app.route("/append_row")
def append_row_and_return_df_shape():
    app.df = pd.concat([app.df, pd.DataFrame({"a": [1]})])
    return f"app.df is of shape: {app.df.shape}"


@app.route("/append_with_delay")
def sleep_and_append_row_and_return_df_shape():
    # raise condition!
    df = app.df
    time.sleep(3)
    app.df = pd.concat([df, pd.DataFrame({"a": [1]})])
    return f"app.df is of shape: {app.df.shape}"


if __name__ == '__main__':
    app.run("localhost", port=5000)
