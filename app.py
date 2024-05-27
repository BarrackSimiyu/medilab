from flask import *
from flask_restful import Api

app = Flask( __name__ )

api = Api( app )
# endpoints /routes 
from views.views import MemberSignup,MemberSignin,Memberprofile,AddDependant

api.add_resource(MemberSignup, '/api/member_signup')
api.add_resource( MemberSignin, '/api/member_signin' )
api.add_resource(Memberprofile,'/api/member_profile')
api.add_resource(AddDependant,'/api/add_dependant')

if __name__== '__main__':
    


    app.run(debug=True)

