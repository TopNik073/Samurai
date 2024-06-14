from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

flow = InstalledAppFlow.from_client_secrets_file(
    "creds.json",
    scopes=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ],
)
flow.run_local_server()

credentials = flow.credentials
user_info_service = build("oauth2", "v2", credentials=credentials)
user_info = user_info_service.userinfo().get().execute()

if user_info["verified_email"]:
    print(user_info["email"])
    print(user_info["name"])
