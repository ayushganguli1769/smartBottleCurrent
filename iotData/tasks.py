from background_task import background
from iotData.models import Parameter, Bottle
from . models import Bottle
import random 
import requests
import json
import time

@background(schedule=1)
def abcdfeed_database():
    all_bottle = Bottle.objects.all()
    for bottle in all_bottle:
        if bottle.is_active:
            data_url = 'https://api.thingspeak.com/channels/963032/feeds.json?api_key=DKMF4NLA7PPP3ZA8&results=2'
            response = requests.get(data_url)
            data = response.json()
            field = data['feeds'][0]['field1']
            b = str(random.randrange(1,633,1))
            c = str(random.randrange(1,633,1))
            x = Parameter(bottle = bottle,field1 = field, field2 = b, field3 = c)
            x.save() 
        else:
            x = Parameter(bottle = bottle,field1 = "0", field2 = "0", field3 = "0")
            x.save() 
abcdfeed_database(repeat=0,repeat_until=None)
# do not acess db
