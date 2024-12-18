from flask_login import LoginManager
from core.models import User, session

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()