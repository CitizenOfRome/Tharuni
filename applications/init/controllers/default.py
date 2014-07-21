if 0:
    '''For Eclipse PyDev to detect Web2Py stuff'''
    global db
    global request
    global session
    global response
    global settings, get_hash, xml, timedelta

    session = Session()
    request = Request()
    response = Response()

    from gluon.globals import *
    from gluon.html import *
    from gluon.http import *
    from gluon.sqlhtml import SQLFORM, SQLTABLE, form_factory
    from gluon.sql import *
    from gluon.validators import *
    import string, json
    from datetime import datetime

def index():
    '''Home Page'''
    return response.render('default/index.html', locals())

def handler():
    '''A generic handler'''
    if len(request.args) > 0:
        base = request.args[0]
        return response.render('default/' + base + '.html', locals())
    else:
        return index()
