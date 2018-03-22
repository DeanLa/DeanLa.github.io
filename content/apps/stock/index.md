Template: apps
<!--<!DOCTYPE html>-->
<html lang="he">
<body class="text-right">
<div id="fb-root"></div>


<!--<div class="background-img"></div>-->
<div class="row text-center" id="head-logo" style="">
    <div class="col-sm-12">
        <h1 style="margin-bottom: 0">סטוק RANDOM</h1>
        <span style="font-size: 5em; margin-top: 0"><i class="fa fa-shopping-cart"></i></span>
    </div>
</div>
<div id="bg"></div>
<div class="container well">
    <div class="row"></div>

    <div class="col-sm-6 text-center col-sm-push-3" id="main-part">
        <div class="row">
            <h2 id="stock" class="center" style="">
                ברוכים הבאים
            </h2>
            <div class="row">
                <div class="col-sm-4 col-sm-push-4">
                    <button class="btn btn-success" id="change-stock">החלף מוצר
                        <i class="fa fa-repeat" aria-hidden="true"></i></button>
                </div>
                <div class="col-sm-4 col-sm-pull-4">
                    <button class="btn btn-danger" id="add-to-cart">הוסף לעגלה
                        <i class="fa fa-shopping-cart" aria-hidden="true"></i>
                    </button>
                </div>

                <div class="col-sm-4">
                    <button class="btn btn-primary" id="fb-share">שתף
                        <i class="fa fa-facebook" aria-hidden="true"></i></button>
                </div>

            </div>
        </div>
        <h3 class="follow">מחולל מוצרי הסטוק</h3>
        <p id="instructions">הכפתור "החלף מוצר" <span class="web-only">(או הכפתור K במקלדת)</span> יחולל עבורך מוצר סטוק
            נוסף.
            <br/> אם המוצר לטעמך הכפתור "הוסף לעגלה" <span class="web-only">(או הכפתור L במקלדת)</span> יוסיף אותו לעגלת
            הקניות.
        </p>
        <h2>מעל
            <span id="quantity">
1
        </span>
            מוצרים שונים!
        </h2>
        <div class="row follow">
            <iframe src="//www.facebook.com/plugins/follow?href=https%3A%2F%2Fwww.facebook.com%2FDeanLangsam&amp;layout=standard&amp;show_faces=true&amp;colorscheme=light&amp;width=450&amp;height=80"
                    scrolling="no" frameborder="0"
                    style="border:none; overflow:hidden;  height:80px; width: 100%;"
                    allowTransparency="true"></iframe>
        </div>
    </div>
    <div class="col-sm-3 col-sm-push-3">
        <div class="well text-right" id="cart-well">
            <h3>העגלה שלי</h3>
            <ul class="list-group" id="my-cart">
            </ul>
        </div>
    </div>
    <div class="col-sm-3 col-sm-pull-9">
        <!--ads-->
        <!--<div class="well">asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd </div>-->
    </div>

</div>

</body>

<script src="stock.js"></script>
<!--Tracking-->
<script>
    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date();
        a = s.createElement(o),
            m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-90395782-1', 'auto');
    ga('send', 'pageview');

</script>
</html>