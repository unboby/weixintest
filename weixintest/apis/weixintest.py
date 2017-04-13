# coding: utf8
#
# weixintest - version
#
# Author: ilcwd
# Create: 14/11/12
#

import flask
import hashlib
from ..core import success_response, normal_success_response
from ..core import config
from decorators import check_weixin_sig
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

app = flask.Blueprint('weixintest', __name__)


@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
#@check_weixin_sig
def index():
    echostr = flask.request.args.get('echostr', '')
    print flask.request.args
    print flask.request.data
    tree = ET.fromstring(flask.request.data)
    tousername = tree.find('ToUserName').text
    print tousername
    return normal_success_response("1")
