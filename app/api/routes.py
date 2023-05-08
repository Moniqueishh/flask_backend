# API's we need

#DO we want to be able to search or add dates?
#If so, thats how we would search historical data for the weather API
#If not, lets do that last at least 

#Weather API (get from HW)
#possibly need to pull historic dates to forcast the weather for specific dates (Statistical Weather Data API)


#Spotify playlist for the place searched(Rewatch flask API class)

#Youtube videos based off place searched (can probably youtube how to do this)

#Possible Pinterest API or an API that can pick suggested outfits for the searched place?

# EXTRA:
# TRY to find an API that will let you see travel, or potentially book travel

from flask import Blueprint, request
from ..models import db, User, City, savedTrips
import re


api = Blueprint('api', __name__, url_prefix='/api')

@api.get('/users')
def get_users():
    users = User.query.all()
    if not users:
        return {'status': 'not ok', 'message': 'Unable to get users'}
    return {'status': 'ok', 'users': [user.to_dict() for user in users]}

@api.get('/users/<uid>')
def get_user(uid):
    user = User.query.filter_by(uid=uid).first()
    if not user:
        return {'status': 'not ok', 'message': 'Unable to get user'}
    return {'status': 'ok', 'user': user.to_dict()}

@api.post('/users')
def create_user():
    uid = request.json.get('uid')
    name = request.json.get('displayName')
    img = request.json.get('photoURL')
    print(img)
    user = User.query.filter_by(uid=uid).first()
    
    if user:
        return {'status': 'ok', 'message': 'Unable to create user. User already exists', 'user': user.to_dict()}
    user = User(uid=uid, name=name, img=img)
    user.create()
    return {'status': 'ok', 'user': user.to_dict()}