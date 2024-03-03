import json

from django.http import HttpResponse
import requests
import dotenv
import os


# Create your views here.
def index(request):
    token = _get_access_token(request)
    url = 'https://api.intra.42.fr/v2/me'
    token = 'Bearer ' + token
    headers = {'Authorization': token}
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    login = data["login"]
    return HttpResponse("로그인 됐어요! " + " " + login)


def login(request):
    return HttpResponse(
        '''<button onclick="location.href='https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-dbe4225a662546c4fe5012e0ccbf95ff6ddcea48a2069e5016d85fa9e055d71e&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fapi%2Fv1%2Fuser%2Foauth%2F&response_type=code'">로그인</button>''')


def _get_access_token(request):
    dotenv.load_dotenv()
    grant_type = "authorization_code"
    client_id = os.environ.get("ID")
    client_secret = os.environ.get("SECRET")
    code = request.GET.get("code")
    state = request.GET.get("state")

    redirect_uri = os.environ.get("REDIRECT")
    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "state": state,
        "redirect_uri": redirect_uri,
    }
    token_request = requests.post("https://api.intra.42.fr/oauth/token", data)
    token_response_json = token_request.json()
    return token_response_json.get("access_token")
