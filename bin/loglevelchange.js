/*global window URL*/
require([
    'jquery',
    'underscore',
    'splunkjs/mvc',
], function ($,_,mvc) {
  $(document).ready(function(){
    var token = "";
    var host_name = "";
    var tickets;
    var ticket_json = {};


      // Checks if user selected atr instance is valid.
      $(document.body).on("click","#Force Change", function(e) {
        e.preventDefault();
        ContainerName = $('#ContainerName').val();
        newLogLevel = $('#newLogLevel').val()
        var data = {"ContainerName":ContainerName,"newLogLevel": newLogLevel};

// If valid, set .host to valid & call getDropDown() & extracts auth token
        var jqxhr = $.post('../../custom/aaam-atr-v3-controlroom-ui/ConfigurationEndpoint/checkATRHealth', data, function(response) {
          if(response.status == 200){
            $(".host").addClass("active");
            $("#host_name").css("background-color","rgba(0,255,0,0.2)");
            $("#username").css("background-color","rgba(0,255,0,0.2)");
            $("#password").css("background-color","rgba(0,255,0,0.2)");
            token = response.token;
