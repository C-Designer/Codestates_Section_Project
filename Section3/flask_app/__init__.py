from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

    if config is not None:
        app.config.update(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from flask_app.views.main_views import main_bp

    app.register_blueprint(main_bp)
    # app.register_blueprint(user_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)