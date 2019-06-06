/*global window URL*/
require([
    'jquery',
    'underscore',
    'splunkjs/mvc',


var grabedurl = "dh-ctrl-rm-atr.atrmywizard360.com"
document.getElementById('appURL').href = "https://" +  grabedurl + "splunk/en-US/app/Log_Monitoring_Project/docker_logging_level_table?form.Docker_Name=ansible&form.docker_word_search=INFO"

function loglevelchange() {
    $(document.body).on("click","#Force Change", function(e) {
        ContainerName = $('#ContainerName').val();
        newLogLevel = $('#newLogLevel').val()
        var data = {"ContainerName":ContainerName,"newLogLevel": newLogLevel};
        var sendin = $.post('../../custom/Log_Monitoring_Project/loglevelEndpoint', data, function(response) {


    }
    }

