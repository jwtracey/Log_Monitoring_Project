import sys
sys.path.append('/Users/jwtracey/Library/Python/2.7/lib/python/site-packages')

import logging
import os
import subprocess
import cherrypy
import ConfigParser
import splunk
#import splunk.bundle as bundle
import splunk.appserver.mrsparkle.controllers as controllers #controller- runs py script when a sensor triggers the controller
#import splunk.appserver.mrsparkle.lib.util as util
from splunk.appserver.mrsparkle.lib.decorators import expose_page
import json
import requests
import datetime
from json import dumps as dict_to_json
from requests.auth import HTTPBasicAuth
import csv


#hardcoded variables need to be Changed
ATR_URL = "https://dh-controlroomdev.atrmywizard360.com/"
ATR_User = "admin"
ATR_Pass = "Z0MP4ES7ZDHMBKZB"
ATR_data = {'username': ATR_User,'password': ATR_Pass}
Log_URL = ATR_URL + "atr-gateway/ticket-management/loggers/"
ATR_auth_URL = ATR_URL + 'atr-gateway/identity-management/api/v1/auth/token'

ATR_token_headers = {'Content-Type': 'application/json;charset=utf-8','Accept': '*/*'}
ATR_token_response = requests.post(ATR_auth_URL, data=json.dumps(ATR_data),headers=ATR_token_headers, verify=False)
ATR_token_response = ATR_token_response.json()

ATR_token = ATR_token_response['token']

ticketSysHeaders = {'Accept': 'application/json', 'apiToken': ATR_token}

class Controller(controllers.BaseController):
    @expose_page(must_login=False)
    def status(self, **kwargs):
        return "I am here: "

#../../custom/LoggingLevelsChange/loglevelEndpoint/changelogginglevel
    @expose_page(must_login=False, methods=['POST'])
    def changelogginglevel(self,**kwargs):
        ContainerName = kwargs.get('ContainerName')
        EffectiveLevel = kwargs.get('newLogLevel')
        #changing logging levels on swagger
        ContData = {"name" : ContainerName,
                    "effectiveLevel" : EffectiveLevel}
        r = requests.post(Log_URL+ContainerName, data=json.dumps(ContData), headers=ticketSysHeaders, verify=False)
        return self.render_json({'status':200,'message':"HitEndpoint","Name":ContainerName,"EffectiveLevel":EffectiveLevel})



