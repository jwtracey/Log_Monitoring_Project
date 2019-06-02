import json

docker_containers = ["ansible","aqe-editor-client","atr-mongo","atr-postgres","automation-queue","automation-worker","bot","bot-hazelcast","chatbot-client","client","consul","elasticsearch","gamification","gateway","identity-management","identity-management-client","kb-hub","knowledgebase","knowledgebase-client","mlcore-frontend","mlcore-master","mlcore-mongo","mlcore-predict-worker","mlcore-redis","mlcore-train-worker","mongo-provision","monitoring","monitoring-client","nginx","notification","plugin-automation-camel","plugin-automation-chatbot","plugin-automation-rundeck","plugin-standalone","rabbitmq","rabbitmq-plgins","rundeck","rundeck-provision","splunk","ticket-management"]

for dock_container in docker_containers:
    response = {dock_container : "ENABLED"}
    x = json.dumps(response)
    print(x)
