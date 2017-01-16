/**
 * Created by Dean on 14-Jan-17.
 */
var items = [];
$.getJSON("stock.json", function (data) {
    $.each(data, function (key, val) {
        console.log(val.length);
        items.push(val);
    });
    moreStock();
});

function moreStock() {
    var txt = "";
    var whichVars = [];
    $.each(items, function (i, item) {
        idx = Math.floor(Math.random() * item.length)
        txt += item[idx];
        txt += " ";
        whichVars.push(idx);
    });
    txt = txt.slice(0, -1);
    $("#stock").html(txt);
    return whichVars;
}
function itemRemove() {
    $(this).parent().remove()
}
function addToCart() {
    var currentItem = $("#stock").html();
    $("#my-cart").append('<li class="list-group-item">' +
        currentItem +
        '<a href="#" class="badge badge-default pull-left cart-remove"> X </a></li>');
    // console.log(currentItem)
}


$("#change-stock").click(moreStock);
$("#my-cart").on("click", "li .cart-remove", itemRemove);
$("#add-to-cart").click(addToCart);
$("#fb-share").on("click", function () {
    FB.ui({
        method: 'share',
        display: 'popup',
        href: 'http://deanla.com/stock/',
        quote: "quote stock",
        hashtag: "hashtag stock"
    }, function (response) {
    });
});

$("body").keypress(function (event) {
    k = event.which;
    // console.log(k);
    // key K
    if ($.inArray(k, [75, 107, 1500]) >= 0) {
        moreStock();
    } // key L
    else if ($.inArray(k, [76, 108, 1498]) >= 0) {
        addToCart();
    }

});
// var csvContent = "data:text/csv;charset=utf-8,";
// var draws = [];

// $("#fb-share").on("click", function () {
//     for (var i = 0; i < 100000; i++) {
//         res = moreStock();
//         draws.push(res);
//         // console.log(i);
//     }
//     // console.log(draws)
//     draws.forEach(function (nums, index) {
//         dataString = nums.join(",");
//         csvContent += index < draws.length ? dataString + "\n" : dataString;
//     })
//     var encodedUri = encodeURI(csvContent);
//     // window.open(encodedUri);
//     // $(this).setAttribute("href")
//     var link = document.createElement("a");
//     link.setAttribute("href", encodedUri);
//     link.setAttribute("download", "my_data.csv");
//     document.body.appendChild(link); // Required for FF
//
//     link.click(); //
// });


