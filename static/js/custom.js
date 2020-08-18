$(document).ready(function() {
    var data_loaded = false
    $("#usernameInp").focus();

    function getCardForData(data) {
        if (data.caption == "") {
            return null;
        }

        cardElement = $(document.createElement("div"))
            .addClass("card")
            .attr("id", "dataItem")
            .data("id", data.id);
        cardText = $(document.createElement("p"))
            .addClass("card-text")
            .text(data.caption);
        cardBody = $(document.createElement("div"))
            .addClass("card-body py-2")
        cardFooter = $(document.createElement("div"))
            .addClass("card-footer py-0")
        cardLink = $(document.createElement("a"))
            .attr("href", "https://www.instagram.com/p/"+data.shortcode)
            .append("<small><b>"+data.id+"</b></small>")
        
        cardBody.append(cardText);
        cardElement.append(cardBody);
        cardFooter.append(cardLink);
        cardElement.append(cardFooter);

        return cardElement;
    }

    $("#scrapeUsernameBtn").click(function() {
        $("#scraperSpinner").show();
        data_loaded = false;
        $("#allCards").empty();
        $("#username").empty();
        $.post(
            $SCRIPT_ROOT + '/scrape',
            JSON.stringify({"username" : $("#usernameInp").val()})
        )
        .done(function(data){
            console.log(data);
            if (data.status) {
                data.scraped_data.data.forEach(item => {
                    if (item.caption != null || item.caption != "") {
                        $("#allCards").append(getCardForData(item));
                    }
                });
                $("#username").text = data.username;
                data_loaded = true;
            }
        })
        .fail(function(){
            console.log(status)
            alert("error");
        })
        .always(function(){
            $("#scraperSpinner").hide();
        });
    })    

});