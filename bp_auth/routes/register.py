from flask import render_template
from web.app.data_layer import ByClass, Events, EventSignUp, On

from bp_auth import auth_bp


@auth_bp.get("/register")
@auth_bp.get("/<string:_locale>/register")
def register(_locale: str) -> str:
    events = Events(EventSignUp(ByClass(On.SUBMIT)))
    return render_template("auth/register.html", events=events)
