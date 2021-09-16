import datetime
import mongoengine

class Spyders(mongoengine.Document):
    registrated_date = mongoengine.DateTimeField(default = datetime.datetime.now)
    species = mongoengine.StringField(required = True)
    name = mongoengine.StringField(required = True)
    is_venomous = mongoengine.StringField(required = True)
    meta = {
        'db_alias':'core',
        "collection": 'spyders'
    }