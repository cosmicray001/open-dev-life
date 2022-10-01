// example to get data attribute using javascripts

var plant = document.getElementById('fruits');
var fruitName = plant.getAttribute('data-item-name');
var fruitId = plant.getAttribute('data-id');

// example to get data attribute using javascripts

$( document ).ready(function() {
    // 1st example
    var fruitName_1 = $(this).data('item-name');
    var fruitId_1 = $(this).data('id');

    //or
    // we can use below example

    var fruitName_2 = $(this).attr('data-item-name');
    var fruitId_2 = $(this).attr('data-id');

});


// Reference 
// http://html5doctor.com/html5-custom-data-attributes/