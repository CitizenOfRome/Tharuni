'''Add the modules folder to sys.path'''
import sys
path = '../modules/'
if not path in sys.path: sys.path.append(path)

from gluon.storage import Storage

import json

from datetime import datetime

def xml(s, sanitize=True, permitted_tags=['a', 'b', 'blockquote', 'br/', 'i', 'li', 'ol', 'ul', 'p', 'cite', 'code', 'pre', 'img/', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'tr', 'td', 'div', 'span', 'sup', 'sub', 'u', 'strike', 'tbody', 'hr', 'font', 'strong'], allowed_attributes={ 'a': ['href', 'title', 'rel'], 'img': ['src', 'alt'], 'blockquote': ['type'], 'td': ['colspan']}):
    return XML(s, sanitize, permitted_tags, allowed_attributes)

def strip_tags(s):
    return xml(s, True, [], []) + ""
