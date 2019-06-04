import splunk.appserver.mrsparkle.controllers as controllers #controller- runs py script when a sensor triggers the controller.
from splunk.appserver.mrsparkle.lib.decorators import expose_page
import splunk.appserver.mrsparkle.lib.util as util
import cherrypy
import os
import subprocess
import datetime
from os.path import isfile as IfFileExists
import json
import datetime
import ConfigParser
import requests
from json import dumps as dict_to_json
from requests.auth import HTTPBasicAuth
import csv


        SPLUNK_HOME = os.environ['SPLUNK_HOME']
        Config = ConfigParser.ConfigParser()
        path = SPLUNK_HOME+"/etc/apps/aaam-atr-v3-controlroom-data/bin/settings.conf"
        Config.read(path)

        # Hit auth endpoint with login details to retrieve token
        ATR_auth_URL = host + '/atr-gateway/identity-management/api/v1/auth/token'

        ATR_data = {'username': username,'password': password}
        ATR_token_headers = {'Content-Type': 'application/json;charset=utf-8','Accept': '*/*'}
        ATR_token_response = requests.post(ATR_auth_URL, data=json.dumps(ATR_data),headers=ATR_token_headers, verify=False)


        # Write values to infraConfiguration.csv lookup
        SPLUNK_HOME = os.environ['SPLUNK_HOME']
        infraInfoPath = SPLUNK_HOME + "/etc/apps/aaam-atr-v3-controlroom-ui/lookups/infraConfiguration.csv"
        infraFile = open(infraInfoPath,"w+")
        infraFile.seek(0)
        infraFile.write(data)
        infraFile.truncate()
        infraFile.close()

