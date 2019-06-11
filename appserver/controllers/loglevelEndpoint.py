import requests
import json


#hardcoded variables need to be Changed
ATR_URL = "https://dh-ctrl-rm-atr.atrmywizard360.com/"
ATR_User = "admin"
ATR_Pass = "HYZWL3P48WFBWV1M"
ATR_data = {'username': ATR_User,'password': ATR_Pass}
Log_URL = ATR_URL + "atr-gateway/ticket-management/loggers/"
ATR_auth_URL = ATR_URL + 'atr-gateway/identity-management/api/v1/auth/token'

ATR_token_headers = {'Content-Type': 'application/json;charset=utf-8','Accept': '*/*'}
ATR_token_response = requests.post(ATR_auth_URL, data=json.dumps(ATR_data),headers=ATR_token_headers, verify=False)
ATR_token_response = ATR_token_response.json()

ATR_token = ATR_token_response['token']

ticketSysHeaders = {'Accept': 'application/json', 'apiToken': ATR_token}

#changing logging levels on swagger

Container = ContainerName
EffectiveLevel = newLogLevel

changeData = {"Name" : Container, "effectiveLevel" : EffectiveLevel}
response = requests.post(Log_URL+Container, data=json.dumps(changeData), headers=ticketSysHeaders, verify=False)
