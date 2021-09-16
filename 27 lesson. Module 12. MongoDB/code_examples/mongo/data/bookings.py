import mongoengine


class Bookings(mongoengine.EmbeddedDocument):
    guest_id = mongoengine.ObjectIdField()
    guest_spyder_id = mongoengine.ObjectIdField()

    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required=True)
    check_out_date = mongoengine.DateTimeField(required=True)

    review = mongoengine.StringField()
    rating = mongoengine.IntField(default=0)

    @property
    def duration_in_days(self):
        return (self.check_out_date - self.check_in_date).days

