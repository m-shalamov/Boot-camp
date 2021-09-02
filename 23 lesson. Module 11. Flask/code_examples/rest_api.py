from flask_restx import Api, Namespace, fileds, Resourse

api = Api()

###################################
registration_namespace = Namespace("registration", description = "Registr api")

registration_model = registration_namespace.model("registration",{
    "login": fileds.String(
        required = True,
        description = "User login"
    ),
    ...
})


@registration_namespace.route("")
class RegistrationClass(Resourse):
    @registration_namespace.response(201, "the user was created")
    @registration_namespace.response(500, "Internal Server error")
    def post(self):
        try:
            login = request.json["login"]
        except KeyError as e:
            registration_namespace.abort(400)
        except ...
        return {
            "description": "The user was created"
        }
        
###################################################
import unittest

class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config[]
        ...
    def setUp(self):
        db.create_all()
    def tearDown(self):
        db.drop_all()
    
    def test_valid_user_registration(self):
        response = self.register("Tom", "1234")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'description': "The user was created"})
    
    def test_invalid_user_registration(self):
        ...
    
    def register(self, login, password):
        return self.app.post(
            "/registration",
            json = {"login": login, "password": password},
            follow_redirects = True
        )

########################################################
class Config:
    registration_schema = {
        "proprties": {
            "login": {'type': "string", "minLength": 2, "maxlength": 4, "pattern": "^[\w.-]+$"}
        }
    }





@app.route("/registration", methods = ["POST"])
@expects_json(Config.registration_schema)
def registration():
    pass
##################################################33
class Users(db.Model):
    id
    login
    password
    items
    def get_token(self, expires_sec = 1800):
        s = Serializer(app.config["SECRET_KEY"],expires_sec )
        return s.dumps({"user_id": self.id}).decode("utf-8")
    @staticmethod
    def get_user_with_token( token):
        s = Serializer(app.config["SECRET_KEY"])
        user_id = s.loads(token)["user_id"]
        return Users.query.get(user_id)
        
    
