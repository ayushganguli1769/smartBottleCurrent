from background_task import background
from iotData.models import Parameter, Bottle
from . models import Bottle
import random 

@background(schedule=1)
def abcdfeed_database():
    all_bottle = Bottle.objects.all()
    for bottle in all_bottle:
        a = str(random.randrange(1,633,1))
        b = str(random.randrange(1,633,1))
        c = str(random.randrange(1,633,1))
        x = Parameter(bottle = bottle,field1 = a, field2 = b, field3 = c)
        x.save() 

abcdfeed_database(repeat=1,repeat_until=None)
# do not acess db
