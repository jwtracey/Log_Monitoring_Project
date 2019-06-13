/*global window URL*/
require([
    'jquery',
    'underscore',
    'splunkjs/mvc',
    'splunkjs/mvc/simplexml/ready!',
], function ($,_,mvc) {
  $(document).ready(function(){

    //var token = "";
    //var tickets;
    //var ticket_json = {};

    var data = {};


    $(document.body).on("click","#force_change", function(e) {
        e.preventDefault();
        var Container = $('#ContainerName').val();
        var LoggingLevel = $('#newLogLevel').val();
        data = {"ContainerName":Container,"newLogLevel": LoggingLevel};
        console.log(data);
        var sendin = $.post('../../custom/Log_Monitoring_Project/loglevelEndpoint/changelogginglevel', data,  function(response) {
            if(response.status == 200){
                alert("It worked!");

    };
    });
    });
    });
    });
