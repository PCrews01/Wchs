import os
import json
import requests
from flask import Blueprint, redirect, request, url_for, render_template
from flask_login import login_user, logout_user, login_required, current_user, login_manager
from oauthlib.oauth2 import WebApplicationClient
from .models import AuthenticatedUser
from website import DB

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
GOOGLE_CLIENT_ID = "113087941687-umil4kt4oulh9p35h9uu1r9ssvlqlbl8.apps.googleusercontent.com"

GOOGLE_CLIENT_SECRET ="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"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
auth = Blueprint('auth', __name__)
client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@auth.route('/login', methods=['GET', 'POST'])
def login():
        google_auth_provider = get_google_provider_cfg()
        authorization_endpoint = google_auth_provider["authorization_endpoint"]
        request_uri = client.prepare_request_uri(
              authorization_endpoint,
              redirect_uri="http://127.0.0.1:5000/login/callback",
              scope=["openid", "email", "profile"]
    )
        return redirect(request_uri)

@auth.route("/login/callback")
def callback():
    code = request.args.get("code")
    google_auth_provider = get_google_provider_cfg()
    token_endpoint = google_auth_provider["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
         token_endpoint,
         authorization_response=request.url,
         redirect_url=request.base_url,
         code=code
        )
    token_response = requests.post(
         token_url,
         headers=headers,
         data=body,
         auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)
    )
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = get_google_provider_cfg()
    ui = userinfo_endpoint["userinfo_endpoint"]
    uri,headers,body = client.add_token(ui)
    userinfo_response = requests.get(uri,headers=headers,data=body)

    if userinfo_response.json().get("email_verified"):
         unique_id = userinfo_response.json()["sub"]
         user_email = userinfo_response.json()["email"]
         user_name = userinfo_response.json()["given_name"]
         last_name = userinfo_response.json()["family_name"]
         picture = userinfo_response.json()["picture"]
         print(f"U info {userinfo_response.json()}")
    else:
         return "User email not verified", 400
    
    user = AuthenticatedUser(
         unique_id=unique_id,
         first_name=user_name,
         last_name=last_name,
         email=user_email,
         picture=picture

    )
    i = AuthenticatedUser.query.filter_by(email=user.email).first()
    if not AuthenticatedUser.query.filter_by(unique_id=unique_id).first():
        DB.session.add(user)
        DB.session.commit()
        return redirect(url_for('views.home'))
    login_user(user=i, remember=True, force=True)
    return redirect(url_for('views.home'))

@auth.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('views.home'))