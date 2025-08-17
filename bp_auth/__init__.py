from ._bp import auth_bp, auth_static_jobs
from .routes import login, password, register

__all__ = [
    "auth_bp",
    "auth_static_jobs",
    "login",
    "password",
    "register",
]
