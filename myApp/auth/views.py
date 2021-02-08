from . import auth

@auth.route("/login",methods=['POST'])
def login():
    pass

@auth.route("/registration",methods=['POST'])
def register():
	pass

@auth.route("/<id>",methods=['GET','PUT'])
def account():
	pass