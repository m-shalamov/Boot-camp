import datetime
import mongoengine

class People(mongoengine.Document):
    registrated_date = mongoengine.DateTimeField(default = datetime.datetime.now)
    name = mongoengine.StringField(required = True)
    email = mongoengine.StringField(required = True)
    spyder_ids = mongoengine.ListField()
    cage_ids = mongoengine.ListField()
    
    meta = {
        'db_alias':'core',
        "collection": 'people'
    }
    