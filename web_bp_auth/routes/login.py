from flask import render_template
from web.app.data_layer import ByClass, EventLogin, Events, On

from web_bp_auth import auth_bp


@auth_bp.get("/login")
@auth_bp.get("/<string:_locale>/login")
def login(_locale: str) -> str:
    events = Events(EventLogin(ByClass(On.SUBMIT)))
    return render_template("auth/login.html", events=events)
