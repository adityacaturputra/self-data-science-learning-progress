// Define Simulation Params
const trials = 10;
const pSuccess = 0.5;

// Set Margin to Top and Bottom of Page
var margin = {
    top: 30, 
    right: 100, 
    bottom: 30, 
    left: 100
};

function getWidthUnit(w, n){
    // Define Wifth Unit; W / N + 1, includes 0
    return (w / (n + 1))
}

function doubleSliderInit(w, h, n){

    wu = getWidthUnit(w, n)

    // Init Slider w. Access
    var slider = d3
        .sliderBottom()
        .min(0)
        .max(n)
        .width(wu * n)
        .step(1)
        .displayValue(false)
        .fill('#008A27')
        .default([4, 6])
        .on('onchange', val => {
            var lb = val[0], ub = val[1];
            chartUpdate(w, h, n, lb, ub)
        });

    d3.select('#d3-binomPlot-slider')
        .append('svg')
            .attr('aria-label', 'slider')
        .append('g')
            .attr("transform", "translate(" + (margin.left + (wu/2)) + ",30)")
            .call(slider);   
}


function updateLabels(lb, ub) {
    // Handle for the double binomial plot
  
    // Define an array between the upper and lower bounds given; in this case, the bounds
    // will always be the slice of values between the slider knobs
    subarr = arr.slice(lb, ub + 1)
    
    // Calculate sum of subarray's item.p values, the probability of an individual outcome
    var sum = subarr.map(item => {return item.p}).reduce((a, b) => a+b, 0)
    
    // Alter text displayed based on the values of the bounds, if the elements appear on the page
    e = document.getElementById("d3-binomPlot-stg")
    e2 = document.getElementById("d3-binomPlot-result")
        
    if ((e != null) && (e2 != null)) {
        if (ub != lb) {
            e.innerHTML = `Probability of between ${lb} and ${ub} Heads: `
            e2.innerHTML =  `${(sum * 100).toFixed(2)}%`
        } else {
            document.getElementById("d3-binomPlot-stg").innerHTML =  `Probability of ${lb} Heads: `
            document.getElementById("d3-binomPlot-result").innerHTML =  `${(sum * 100).toFixed(2)}%`
        }
    }
}


function chartUpdate(w, h, n, lb, ub){

    var xlabels = Array.from(
        {length: n + 1}, (_, index) => index
    );

     // Remove the current binomial plot
     var svg = d3.select("svg");
     svg.selectAll("#d3-binomPlot > *").remove();
 
     // Generate the binomial plot; new, re-render the bars
     var svg = d3.select("svg")
             .append("g")
             .attr("transform", "translate(" + (margin.left) +  "," + (margin.top) + ")");
 
     // Set default scale and axis (X)
     var xR = d3.scaleLinear()
         .domain([0, n + 1])
         .range([0, w]);
 
     // Set default scales and axis (Y)
     var yR = d3.scaleLinear()
         .domain([0, .5])
         .range([h, 0]);
     
     // Define Wifth Unit; W / N + 1, includes 0
     wu = getWidthUnit(w, n)
 
     svg.append("g")
         .attr("transform", "translate(0," + h + ")")
         .call(
             // NOTE: fc (from package d3fc) enchances d3 axis w. additional fuctionality
             // drop in for d3.axisBottom(); required for centered labels
             fc.axisBottom(xR)
                 .tickFormat(d3.format("d"))
                 .tickValues(xlabels)
                 .tickCenterLabel(true)
         )
         
     svg.append("g")
         .attr("class", "grid")
         .call(
             d3.axisLeft(yR)
                 .tickSize(-w)
                 .ticks(5)
                 .tickFormat(d3.format(",.2f"))
         )
 
     // text label for the x axis
     svg.append("text")   
         .attr("class", "label")          
         .attr("y", h + 50)
         .attr("x", (w / 2))
         .style("text-anchor", "middle")
         .text("Number of Heads");
 
     // text label for the y axis
     svg.append("text")
         .attr("class", "label")          
         .attr("transform", "rotate(-90)")
         .attr("y", 0 - margin.left )
         .attr("x", 0 - (h / 2))
         .attr("dy", "1em")
         .style("text-anchor", "middle")
         .text("Probability");  
    
         var xR = d3.scaleLinear()
         .domain([0, n + 1])
         .range([0, w]);
 
     // Set default scales and axis (Y)
     var yR = d3.scaleLinear()
         .domain([0,.3])
         .range([h, 0]);

    // Generate a new series of bars w. variable colors, opacity, etc. based on state
    // of the slider and the return P(x)
    svg.selectAll(".bar")
        .data(arr)
        .enter()
        .append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return xR(d.successes) + wu * .04; }) // mulltiplication term for (0.08 *  widthUnit) gap between bars
            .attr("y", function(d) { return yR(d.p); })
            .attr("width", function(d) { return wu * .92; }) // multiplication term for (0.08 *  widthUnit) gap between bars
            .attr("height", function(d) { return Math.max(h - yR(d.p), 0); }) // Max @ 0 to prevent console returning floating point errors e.g. `1.2x10^-12 is not valid height` 
            .attr("fill", (d => ((d.successes >= lb) && (d.successes <= ub)) ? "#008A27" : "#10162F"))
            .style("opacity", 0.8)
            .on("mousemove", function(event, d){
                    tooltip = d3.select('.tooltip')  
                
                    tooltip.html(
                        "P("+ d.successes +" Heads | " + n + " Trials) = "  + (d.p.toFixed(3)) + "<br>")
                        .style("left", (event.clientX) + 20 + "px")
                        .style("top", (event.clientY) + "px")
                        .style("opacity", 1);
            })
            .on("mouseout", function(){ 
                tooltip.style("opacity", 0);	
            });
        
    // Update the labels for the 2-slider binomial applet; if applicable
    // Check w. ub != 0 && ub != null
    if ((ub > 0) &  (ub != null)) {
        updateLabels(lb, ub)
    }

}
    
function factorial(num){
    if (num < 0) 
        return -1;
    else if (num == 0) 
        return 1;
    else {
        return (num * factorial(num - 1));
    }
}

function binomialPMF(t, s, p){
    // Returns the binomial PMF for successes (s) in trials (t)
    // given a probability of successs (p).
    // p = ( t! / s! * (t-s)! ) * p ^ s * (1-p) ^ (t - s)
    return (factorial(t) / (factorial(s) * factorial(t-s))) * Math.pow(p, s) * Math.pow(1-p, t-s)
}

function genBinomialSeries(n, N, p){
    // Calculate the probability of (0...N) successes given n trials and p success prob.
    // 0 where N > n, but want fixed array len. for simplicity...
    var probSeries = [];
    for (s = 0; s <= N; s++) {
        probSeries.push({
            "successes": s,
            "trials": n,
            "p": binomialPMF(n, s, p),
        })
    } 
    return probSeries
}


function appletInit(){
    
    // Access SVG object from 
    var svgNode = d3.select('svg').node();
    width = svgNode.getBoundingClientRect().width - margin.left - margin.right;
    height = svgNode.getBoundingClientRect().height  - margin.top - margin.bottom;
    
    arr = genBinomialSeries(trials, trials, pSuccess)    
    
    chartUpdate(width, height, trials, 4, 6)

    // Init slider w. default state, width of each tick == w/n+1, leaves room
    // for zero
    doubleSliderInit(width, height, trials)
}