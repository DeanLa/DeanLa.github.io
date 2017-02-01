/**
 * Created by Dean on 30-Jan-17.
 */
var margin = {
    top: 10,
    right: 20,
    bottom: 50,
    left: 60
};
var width = 1000 - margin.left - margin.right;
var height = 500 - margin.top - margin.bottom;

var svg = d3.select('#visualisation')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .call(responsivefy)
    .append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);

// X Axis
var parseDate = d3.timeParse("%m%d");
var xScale = d3.scaleTime()
    .range([0, width])
    .domain([parseDate("0101"), parseDate("0231")]);
svg.append('g')
    .attr('transform', `translate(0, ${height})`)
    .call(d3.axisBottom(xScale).ticks(5));

// Y Axis
var yScale = d3.scaleLinear()
    .range([height, 0])
    .domain([0, 1900]);
svg
    .append('g')
    .call(d3.axisLeft(yScale));

// Labels
svg.append("text")
    .classed("legend", true)
    .attr("transform",
        `translate(${width / 2} ,${height + margin.top + 30})`)
    .style("text-anchor", "middle")
    .text("Date 2016");

svg.append("text")
    .classed("legend", true)
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Total Celebrity Deaths");

const type = function (data) {
    data.forEach(d => {
        d.date_in_year = parseDate(d.date_in_year);
        d.total_deaths = +d.total_deaths;
        d.deaths = +d.deaths;
    });
};

var line = d3.line()
    .x(d => xScale(d.date_in_year))
    .y(d => yScale(d.total_deaths))


d3.csv('./2016.csv', function (err, data) {
    type(data);
    svg
        .append('path')
        .attr('class', 'line total y2016')
        .attr('d', line(data))
});

d3.csv('./2017.csv', function (err, data) {
    type(data);
    svg
        .append('path')
        .attr('class', 'line total y2017')
        .attr('d', line(data));
});
for (i = 0; i <= 1; i++) {
    y_pos = 20 * (i + 1);
    svg
        .append('path')
        .attr('d', `M50,${y_pos}L100,${y_pos}`)
        .attr('class', 'line y' + (i + 2016));
    svg
        .append('text')
        .classed('legend', true)
        .attr('x', '110')
        .attr('y', 5 + y_pos)
        .text('' + (i + 2016));
}

function responsivefy(svg) {
    // get container + svg aspect ratio
    var container = d3.select(svg.node().parentNode),
        width = parseInt(svg.style("width")),
        height = parseInt(svg.style("height")),
        aspect = width / height;

    // add viewBox and preserveAspectRatio properties,
    // and call resize so that svg resizes on inital page load
    svg.attr("viewBox", "0 0 " + width + " " + height)
        .attr("preserveAspectRatio", "xMinYMid")
        .call(resize);

    // to register multiple listeners for same event type,
    // you need to add namespace, i.e., 'click.foo'
    // necessary if you call invoke this function for multiple svgs
    // api docs: https://github.com/mbostock/d3/wiki/Selections#on
    d3.select(window).on("resize." + container.attr("id"), resize);

    // get width of container and resize svg to fit it
    function resize() {
        var targetWidth = parseInt(container.style("width"));
        svg.attr("width", targetWidth);
        svg.attr("height", Math.round(targetWidth / aspect));
    }
}