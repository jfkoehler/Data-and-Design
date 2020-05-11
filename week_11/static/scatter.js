// d3.csv("static/ads.csv", function(data){
//     console.log(data)});

const svg = d3.select('#svg');

svg.append('circle')
    .attr('cx', 200)
    .attr('cy', 200)
    .attr('r', 60)
    .style('fill', 'grey');



    
