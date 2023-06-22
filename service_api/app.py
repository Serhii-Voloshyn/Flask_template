from flask import Flask

from service_api.config import Config


app = Flask(__name__)

app.config.from_object(Config)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=app.config["SQLALCHEMY_DATABASE_URI"],
    SQLALCHEMY_TRACK_MODIFICATIONS=app.config[
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    ]
)


@app.route("/smoke", methods=["GET"])
def smoke():
    return "All clear, continue working as intended...", 200
