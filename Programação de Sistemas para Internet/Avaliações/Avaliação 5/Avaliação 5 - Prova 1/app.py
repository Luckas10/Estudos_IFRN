from flask import Flask
from config import Config
from models.user import User
from auth import bp
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Inicialize o LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Registre o Blueprint do auth
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()
