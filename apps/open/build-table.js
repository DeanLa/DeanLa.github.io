console.log(data);
var today = new Date();
var time = (today.getHours() < 10 ? '0' : '') + today.getHours() + ":" +
    (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
var weekday = today.getDay() + 1;
console.log(time);

function totalMinutes(s) {
    h = parseInt(s.split(":")[0]) * 60;
    m = parseInt(s.split(":")[1]);
    return h + m
}

function isBetween(check, between) {
    check = totalMinutes(check);
    after = totalMinutes(between.split("-")[0]);
    before = totalMinutes(between.split("-")[1]);
    return (check > after) & (check < before)

}

function createNowOpen(element, row) {
    let hours = element["hours"];
    let cell = row.insertCell();
    if (weekday in hours) {
        let td = hours[weekday];
        console.log(td);
        for (let hour of td) {
            if (isBetween(time, hour)) {
                text = document.createTextNode("פתוח");
                cell.appendChild(text);
                cell.classList.add("green");
                return
            }
        }

    }
    text = document.createTextNode("סגור");
    cell.appendChild(text);
    cell.classList.add("red");
}

function createOpenHours(element, row) {
    let hours = element["hours"];
    let cell = row.insertCell();
    if (weekday in hours) {
        let td = hours[weekday];
        console.log(td);
        text = document.createTextNode(td.join(", "));
        cell.appendChild(text);
    }
}


function generateTable(table, data) {
    for (let element of data) {
        let row = table.insertRow();
        // place
        let place = row.insertCell();
        let text = document.createTextNode(element["name"]);
        place.appendChild(text);
        // hours
        createNowOpen(element, row);
        createOpenHours(element, row)


    }
}

function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data) {
        let th = document.createElement("th");
        // th.setAttribute("dir", "rtl");
        th.classList.add("text-center");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function makeTable(table, data, head) {
    generateTable(table, data);
    generateTableHead(table, head);
}

let trDays = ["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"];
// let header = document.querySelector(".header");
// header.appendChild(document.createTextNode("פתוח עכשיו?"));
htext = trDays[weekday - 1] + " " + time;
document.querySelector(".timenow").appendChild(document.createTextNode(htext));
// Table
let table = document.querySelector("table");
let head = ["ענף", "פתוח עכשיו?", "שעות פתיחה היום"];

var data;
$.getJSON("data.json", function (json) {
    data = json;
    makeTable(table, data, head);

});