from flask import Flask
from flask import Flask
from public import public
from admin import admin
from authority import authority
from police import police
from api import api

app=Flask(__name__)
app.secret_key='amal'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(authority,url_prefix='/authority')
app.register_blueprint(police,url_prefix='/police')
app.register_blueprint(api,url_prefix='/api')

app.run(debug=True,port=5555,host="")