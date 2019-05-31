import requests
import json


#hardcoded variables need to be changed
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


docker_containers = ["ansible","aqe-editor-client","atr-mongo","atr-postgres","automation-queue","automation-worker","bot","bot-hazelcast","chatbot-client","client","consul","elasticsearch","gamification","gateway","identity-management","identity-management-client","kb-hub","knowledgebase","knowledgebase-client","mlcore-frontend","mlcore-master","mlcore-mongo","mlcore-predict-worker","mlcore-redis","mlcore-train-worker","mongo-provision","monitoring","monitoring-client","nginx","notification","plugin-automation-camel","plugin-automation-chatbot","plugin-automation-rundeck","plugin-standalone","rabbitmq","rabbitmq-plgins","rundeck","rundeck-provision","splunk","ticket-management"]


for dock_container in docker_containers:
    response = requests.get(Log_URL+dock_container, headers=ticketSysHeaders, verify=False)
    response = response.json()
    data = {dock_container : response}
    print(data)




