if 0:
    global db
    global request
    global session
    global response
    global Storage
    import string
    
    
settings = Storage()


#paths
settings.path_to = Storage()
settings.path_to.host = "%s://%s/" % (request.env.wsgi_url_scheme, request.env.http_host) # URL(scheme=True, host=True).replace("init/default/index", "") # "/"
settings.path_to.static = settings.path_to.host + request.application + "/static"
settings.path_to.default = settings.path_to.host + request.application + "/default"
settings.path_to.default_handler = settings.path_to.default + "/handler"

#Display
settings.app_name = "Not your Grandad's Quizzing App" # The application name/title
