
registration_schema = {
    'type': 'object',
    'properties': {
        'login': {'type': 'string',  "minLength": 2, "maxLength": 20, "pattern": "^[\w.-]+$"},
        'password': {'type': 'string', "minLength": 4, "maxLength": 15}
    },
    'required': ['login', 'password']
}

@app.route('/registration', methods = ["POST"])
@expects_json(registration_schema)
def register():
    login = requests.json.get("login")
    password = requests.json.get("login")
    user = User(...)
    response = {
        "result": "The user was created"
    }
    return jsonify(response), 201

    abort(401, "text")

@app.route('/items/new', methods = ["POST"])
@expects_json(creation_schema)
def new_item():
    user = User.get_user_with_token(requests.json.get("token"))
    item = Item(name = requests.json.get("name", user_id = user.id))
    db.session.add(item)
    db.session.commit()

@app.route('/items/id', methods = ["POST"])
@expects_json(creation_schema)
def delete_item():
    user = User.get_user_with_token(requests.json.get("token"))
    item = Items.query.get()
    db.session.delete(item)
    db.session.commit()


@errors.app_errorhandler(401)
def error_401(error):
    response = {}
    return jsonify(response),401

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(40), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}'"
    
    def get_token(self, expires_sec = 1800):
        s = Serializer(app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id},...).decode("utf-8")
    
    def get_user_with_token(token):
        s = Serializer(app.config["SECRET_KEY"])
        user_id = s.loads(token)["user_id"]
        return User.query.get(user_id)
    

registration_namespace = Namespace("registration", description="Registration API")

registration_model = registration_namespace.model('registration', {
    'login': fields.String(
        required = True,
        description='User login',
        help = 'String containing latin letters, digits, ".", "_", minLength = 2, maxLength 20'
    ),
    'password': fields.String(
        required = True,
        description='User password',
        help = 'String containing with minLength = 4, maxLength 15'
    )
})



@registration_namespace.route("")
class RegistrationClass(Resource):
    @registration_namespace.response(200, 'The user with such a login already exists. Please choose another login')
    @registration_namespace.response(201, 'The user was created')
    @registration_namespace.response(400, 'Wrong input')
    @registration_namespace.response(500, 'Internal Server error')
    @registration_namespace.expect(registration_model)
    def post(self):
        """Create a user with such a login and a password"""    
        return {
			"description": "The user was created"
		}, 201
    def get(self):
        """Create a user with such a login and a password"""    
        return {
			"description": "The user was created"
		}, 201