import requests
import json


docker_containers = ["ansible","aqe-editor-client","atr-mongo","atr-postgres","automation-queue","automation-worker","bot","bot-hazelcast","chatbot-client","client","consul","elasticsearch","gamification","gateway","identity-management","identity-management-client","kb-hub","knowledgebase","knowledgebase-client","mlcore-frontend","mlcore-master","mlcore-mongo","mlcore-predict-worker","mlcore-redis","mlcore-train-worker","mongo-provision","monitoring","monitoring-client","nginx","notification","plugin-automation-camel","plugin-automation-chatbot","plugin-automation-rundeck","plugin-standalone","rabbitmq","rabbitmq-plgins","rundeck","rundeck-provision","splunk","ticket-management"]

ENABLED = "ENABLED"

enabled = {"Container" : "Status",
           "ansible" : ENABLED,
           "aqe-editor-client" : ENABLED,
           "atr-mongo" : ENABLED,
           "atr-postgres" : ENABLED,
           "automation-queue" : ENABLED,
           "automation-worker" : ENABLED,
           "bot" : ENABLED,
           "bot-hazelcast" : ENABLED,
           "chatbot-client" : ENABLED,
           "client" : ENABLED,
           "consul" : ENABLED,
           "elasticsearch" : ENABLED,
           "gamification" : ENABLED,
           "gateway" : ENABLED,
           "identity-management" : ENABLED,
           "identity-management-client" : ENABLED,
           "kb-hub" : ENABLED,
           "knowledgebase" : ENABLED,
           "knowledgebase-client" : ENABLED,
           "mlcore-frontend" : ENABLED,
           "mlcore-master" : ENABLED,
           "mlcore-mongo" : ENABLED,
           "mlcore-predict-worker" : ENABLED,
           "mlcore-redis" : ENABLED,
           "mlcore-train-worker" : ENABLED,
           "mongo-provision" : ENABLED,
           "monitoring" : ENABLED,
           "monitoring-client" : ENABLED,
           "nginx" : ENABLED,
           "notification" : ENABLED,
           "plugin-automation-camel" : ENABLED,
           "plugin-automation-chatbot" : ENABLED,
           "plugin-automation-rundeck" : ENABLED,
           "plugin-standalone" : ENABLED,
           "rabbitmq" : ENABLED,
           "rabbitmq-plgins" : ENABLED,
           "rundeck" : ENABLED,
           "rundeck-provision" : ENABLED,
           "splunk" : ENABLED,
           "ticket-management" : ENABLED}
enabled = json.dumps(enabled)
print(enabled)


