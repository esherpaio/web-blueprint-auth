from flask import render_template
from web.app.data_layer import ByClass, EventLogin, Events, EventSignUp, On

from bp_auth import auth_bp


@auth_bp.get("/register")
@auth_bp.get("/<string:_locale>/register")
def register(_locale: str) -> str:
    events = Events(EventSignUp(ByClass(On.SUBMIT)))
    return render_template("register.html", events=events)


@auth_bp.get("/login")
@auth_bp.get("/<string:_locale>/login")
def login(_locale: str) -> str:
    events = Events(EventLogin(ByClass(On.SUBMIT)))
    return render_template("login.html", events=events)


@auth_bp.get("/password-request")
@auth_bp.get("/<string:_locale>/password-request")
def password_request(_locale: str) -> str:
    return render_template("password_request.html")


@auth_bp.get("/password-recover")
@auth_bp.get("/<string:_locale>/password-recover")
def password_recover(_locale: str) -> str:
    return render_template("password_recover.html")
