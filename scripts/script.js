$(document).ready(function() {
    $('#addMotor').click(function() {
        var toAdd = $('input[name=motorItem]').val();
        if (toAdd) {
            $('#finalList').append('<div class="itemFinalList">' + toAdd + '<div>');
            $('#finalList').css("height", "+=18px");
        }
    });
    $('#addEsc').click(function() {
        var toAdd = $('input[name=escItem]').val();
        if (toAdd) {
            $('#finalList').append('<div class="itemFinalList">' + toAdd + '<div>');
            $('#finalList').css("height", "+=18px");
        }
    });
    $('#addProp').click(function() {
        var toAdd = $('input[name=propItem]').val();
        if (toAdd) {
            $('#finalList').append('<div class="itemFinalList">' + toAdd + '<div>');
            $('#finalList').css("height", "+=18px");
        }
    });
});

// This adds any item from the parts list when you click on it
$(document).on('click','.itemTextPartsList', function() {
    var toAdd = $(this).text();
    $('#finalList').append('<div class="itemFinalList">' + toAdd + '<div>');
    $('#finalList').css("height", "+=18px");
});

// This removes any item from the final list when you click on it.
$(document).on('click','.itemFinalList', function() {
    $(this).remove();
    $('#finalList').css("height", "-=18px");
});

$(document).on('click','#reset', function() {
    $('#finalList').empty();
    $('#finalList').append('<p style="text-decoration: underline">Quad specifications</p>');
    $('#finalList').css("height", "40px");
});

// This takes the user to the Add page if he clicks the Add button on the main page.
$(document).on('click','#add', function() {
    window.location.href = "/Add";
});

// Tabs logic.  From (http://www.my-html-codes.com/javascript-tabs-html-5-css3)
window.onload=function() {

  // get tab container
  var container = document.getElementById("tabContainer");
    // set current tab
    var navitem = container.querySelector(".tabs ul li");
    //store which tab we are on
    var ident = navitem.id.split("_")[1];
    navitem.parentNode.setAttribute("data-current",ident);
    //set current tab with class of activetabheader
    navitem.setAttribute("class","tabActiveHeader");

    //hide two tab contents we don't need
    var pages = container.querySelectorAll(".tabpage");
    for (var i = 1; i < pages.length; i++) {
      pages[i].style.display="none";
    }

    //this adds click event to tabs
    var tabs = container.querySelectorAll(".tabs ul li");
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].onclick=displayPage;
    }
}

// on click of one of tabs
function displayPage() {
  var current = this.parentNode.getAttribute("data-current");
  //remove class of activetabheader and hide old contents
  document.getElementById("tabHeader_" + current).removeAttribute("class");
  document.getElementById("tabpage_" + current).style.display="none";

  var ident = this.id.split("_")[1];
  //add class of activetabheader to new active tab and show contents
  this.setAttribute("class","tabActiveHeader");
  document.getElementById("tabpage_" + ident).style.display="block";
  this.parentNode.setAttribute("data-current",ident);
}