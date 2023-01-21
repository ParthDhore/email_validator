from controller.email import email_val
def initialize_routes(api):
    api.add_resource(email_val,'/verify/<string:email>')