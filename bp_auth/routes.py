from flask import render_template
from web.app.data_layer import ByClass, EventLogin, Events, EventSignUp, On

from bp_auth import auth_bp


@auth_bp.get("/auth/register")
@auth_bp.get("/auth/<string:_locale>/register")
def register(_locale: str) -> str:
    events = Events(EventSignUp(ByClass(On.SUBMIT)))
    return render_template("auth/register.html", events=events)


@auth_bp.get("/auth/login")
@auth_bp.get("/auth/<string:_locale>/login")
def login(_locale: str) -> str:
    events = Events(EventLogin(ByClass(On.SUBMIT)))
    return render_template("auth/login.html", events=events)


@auth_bp.get("/auth/password-request")
@auth_bp.get("/auth/<string:_locale>/password-request")
def password_request(_locale: str) -> str:
    return render_template("auth/password_request.html")


@auth_bp.get("/auth/password-recover")
@auth_bp.get("/auth/<string:_locale>/password-recover")
def password_recover(_locale: str) -> str:
    return render_template("auth/password_recover.html")
