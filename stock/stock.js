/**
 * Created by Dean on 14-Jan-17.
 */
 var items = [];
    $.getJSON("stock.json", function (data) {
        $.each(data, function (key, val) {
            console.log(val.length);
            items.push(val);
        })
    });

    function moreStock() {
        var txt = "";
        $.each(items, function (i, item) {
            txt += item[Math.floor(Math.random() * item.length)];
            txt += " ";
        });
        txt = txt.slice(0, -1);
        $("#stock").html(txt);
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