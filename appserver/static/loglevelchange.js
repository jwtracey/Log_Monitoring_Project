/*global window URL*/
require([
    'jquery',
    'underscore',
    'splunkjs/mvc',
], function ($,_,mvc) {
  $(document).ready(function(){
    //var token = "";
    //var tickets;
    //var ticket_json = {};
    var Container = "";
    var newLogLevel = "";
    var data = {};

//var grabedurl = "dh-ctrl-rm-atr.atrmywizard360.com"
//document.getElementById('appURL').href = "https://" +  grabedurl + "splunk/en-US/app/Log_Monitoring_Project/docker_logging_level_table"

    $(document.body).on("click","#force_change", function(e) {
        e.preventDefault();
        Container = $('#ContainerName').val();
        console.log(Container)
        newLogLevel = $('#newLogLevel').val();
        console.log(newLogLevel)
        data = {"ContainerName":Container,"newLogLevel": newLogLevel};
        console.log(data)
        //var sendin = $.post('../../custom''loglevelEndpoint.py', data, function(response) {

    }
    }
    }
    //
