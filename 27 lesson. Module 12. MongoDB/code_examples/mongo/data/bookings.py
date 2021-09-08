import mongoengine

class Bookings(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField()
    guest_spyder_id = mongoengine.ObjectIdField()
    
    booked_date = mongoengine.DateTimeField()
    check_in_date =  mongoengine.DateTimeField(required=True)
    check_out_date =  mongoengine.DateTimeField(required=True)
    
    @property
    def duration(self):
        d = self.check_out_date - self.check_in_date
        return d.days
    
