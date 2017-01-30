/**
 * Created by Dean on 02-Jan-17.
 */


var xCol = "date_in_year";
var yCol = "total_deaths";
var WIDTH = 1200;
var HEIGHT = 600;
var MARGINS = {
    top: 20,
    right: 20,
    bottom: 20,
    left: 50
};
var vis = d3.select("#visualisation");
vis.attr("width", WIDTH).attr("height", HEIGHT);
// var xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([1, 30]);
var parseDate = d3.time.format("%m%d").parse;
var xScale = d3.time.scale().range([MARGINS.left, WIDTH - MARGINS.right])
    .domain([parseDate("0101"), parseDate("0131")]);
var yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0, 700]);
var xAxis = d3.svg.axis()
    .scale(xScale)
    .orient("bottom");
// .ticks(2);
var yAxis = d3.svg.axis()
    .scale(yScale)
    .orient("left");

var xAxisG = vis.append("svg:g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")");

var yAxisG = vis.append("svg:g")
    .attr("class", "y axis")
    .attr("transform", "translate(" + (MARGINS.left) + ",0)");


var lineGen = d3.svg.line()
    .x(function (d) {
        return xScale(d[xCol]);
    })
    .y(function (d) {
        return yScale(d[yCol]);
    })
    .interpolate("linear");

function type(d) {
    // console.log(d[xCol])
    // console.log(d[yCol])
    d[xCol] = parseDate(d[xCol]);
    d[yCol] = +d[yCol];
    return d
}

function render(d, year) {
    console.log("YEAR: ", year);
    console.log("YEAR: ", year);
    vis.append('svg:path')
        .attr('d', lineGen(d))
        .attr('stroke', 'green')
        .attr('stroke-width', 2)
        .attr('fill', 'none');
}

d3.csv("./2016.csv", type, render, 2016);
d3.csv("./2017.csv", type, render, 2017);
console.log("TEST");
xAxisG.call(xAxis);
yAxisG.call(yAxis);