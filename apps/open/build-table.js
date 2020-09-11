console.log(data);
var today = new Date();
var time = today.getHours() + ":" + today.getMinutes();
var weekday = today.getDay() + 1;
console.log(time);

function totalMinutes(s) {
    h = parseInt(s.split(":")[0]) * 60;
    m = parseInt(s.split(":")[1]);
    return h + m
}

function isBetween(check, between) {
    // debugger;
    check = totalMinutes(check);
    // debugger;
    after = totalMinutes(between.split("-")[0]);
    before = totalMinutes(between.split("-")[1]);
    console.log(check);
    console.log(before);
    console.log(after);
    // debugger;
    return (check > after) & (check < before)
    // after

}

function generateTable(table, data) {
    for (let element of data) {
        let row = table.insertRow();
        // place
        let place = row.insertCell();
        let text = document.createTextNode(element["name"]);
        place.appendChild(text);
        // hours
        // debugger;
        let hours = element["hours"];
        let cell = row.insertCell();
        var done = 0;
        if (weekday in hours) {
            let td = hours[weekday];
            console.log(td);
            for (let hour of td) {
                if (isBetween(time, hour)) {
                    text = document.createTextNode("פתוח");
                    cell.appendChild(text);
                    cell.classList.add("green");
                    done = 1
                }
            }
            if (done) {
                continue;
            }

        }
        text = document.createTextNode("סגור");
        cell.appendChild(text);
        cell.classList.add("red");

        // }
        // console.log(hours[key])
        // for (key in element) {
        //     let cell = row.insertCell();
        //     cell.classList.add('green');
        //     let text = document.createTextNode(element[key]);
        //     cell.appendChild(text);
        // }
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

let header = document.querySelector(".header");
header.appendChild(document.createTextNode("פתוח עכשיו"));
document.querySelector(".timenow").appendChild(document.createTextNode(today));
// Table
let table = document.querySelector("table");
let head = ["ענף", "פתוח עכשיו?"];

var data;
$.getJSON("data.json", function (json) {
    data = json;
    makeTable(table, data, head);

});