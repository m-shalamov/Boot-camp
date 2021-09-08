import datetime
import mongoengine
from data.bookings import Bookings

class Cages(mongoengine.Document):
    registrated_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required = True)
    price = mongoengine.FloatField(required = True)
    size = mongoengine.FloatField(required = True)
    allow_venomous =  mongoengine.StringField(required = True)
    
    bookings = mongoengine.EmbeddedDocumentListField(Bookings)
    
    
    meta = {
        "db_alias": "core",
        "collection": "cages"
    }