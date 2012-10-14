if 0:
    '''For Eclipse PyDev to detect Web2Py stuff'''
    from gluon.globals import *
    from gluon.html import *
    from gluon.http import *
    from gluon.sqlhtml import SQLFORM, SQLTABLE, form_factory
    session = Session()
    request = Request()
    response = Response()
    from gluon.sql import *
    from gluon.validators import *
    import string, json, datetime
    global datetime
    global db
    global request
    global session
    global response
    global settings

    
db.define_table('questions',
    db.Field('question', 'text'),
    db.Field('options', 'list:string'),
    db.Field('answer', 'string'),
    db.Field('approved', 'boolean', default=False),
    db.Field('time', 'datetime', default=datetime.utcnow())
)
