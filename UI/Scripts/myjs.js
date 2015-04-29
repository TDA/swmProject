/// <reference path="jquery-2.1.3.min.js" />

$(function () {
    //alert("this works");
    //$('#title').addClass('standout');
    //$('#title')

   
    hide();
    var output = "";
    $("#role").change(function () {
        hide();
        $("#batAttr").val("Select the style").prop('selected', true);
        $("#bowlAttr").val("Select the style").prop('selected', true);
        $('#noOfPlayers').val('');
        if ($("#role option:selected").text() == "Select the role of a player") {
            hide();
        }
        else if ($("#role option:selected").text() == "Batsmen") {
            $('#batAttr').show();
        }
        else {
            $('#bowlAttr').show();
        }
    });

    $("#batAttr").change(function () {
        $('#noOfPlayers').show();
        $('#btnSubmit').show();
    });

    $("#bowlAttr").change(function () {
        $('#batAttr').show();
    });

    $('#btnSubmit').click(function () {
        //alert(parseInt($('#noOfPlayers').val(), 10));
        if ($("#batAttr  option:selected").text() == "Select the style" || isNaN(parseInt($('#noOfPlayers').val(), 10))  ||
            ($("#role option:selected").text() == "Bowler"&& $("#bowlAttr  option:selected").text() == "Select the style")) {
            alert("Incorrect values. Please check!!");
        }
        else if (parseInt($('#noOfPlayers').val(),10)+parseInt($("#noOfBatsmen").text(), 10) + parseInt($("#noOfBowlers").text(), 10) + parseInt($("#noOfAllrounders").text(), 10) > 10) {
            alert("Total players should be less than 11");
        }
        else {
            if ($("#role option:selected").text() == "Batsmen") {
                $("#noOfBatsmen").text(parseInt($('#noOfPlayers').val(), 10) + parseInt($("#noOfBatsmen").text(), 10));
                output = output + "[1," + $("#batAttr option:selected").text() + "," + parseInt($('#noOfPlayers').val(), 10) + "],";
            }
            else if ($("#role option:selected").text() == "Bowler") {
                $("#noOfBowlers").text(parseInt($('#noOfPlayers').val(), 10) + parseInt($("#noOfBowlers").text(), 10));
                output = output + "[2," + $("#batAttr option:selected").text() + "," + $("#bowlAttr option:selected").text() + "," + parseInt($('#noOfPlayers').val(), 10) + "],";
            }
            else if($("#role option:selected").text() == "Allrounder") {
                $("#noOfAllrounders").text(parseInt($('#noOfPlayers').val(), 10) + parseInt($("#noOfAllrounders").text(), 10));
                output = output + "[2," + $("#batAttr option:selected").text() + "," + $("#bowlAttr option:selected").text() + "," + parseInt($('#noOfPlayers').val(), 10) + "],";

            }

        }
    });

    $('#btnReset').click(function () {
        $("#noOfBatsmen").text(0);
        $("#noOfBowlers").text(0);
        $("#noOfAllrounders").text(0);
    });

    $('#btnProceed').click(function () {
        alert(output)
    });
});


hide = function () {
    $('#batAttr').hide();
    $('#bowlAttr').hide();
    $('#noOfPlayers').hide();
    $('#btnSubmit').hide();
};
