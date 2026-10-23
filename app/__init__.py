import os
from pathlib import Path

from flask import Flask

from app.db import init_app


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
        DATABASE=str(Path(app.instance_path) / "social_media.sqlite"),
    )

    if test_config:
        app.config.update(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
