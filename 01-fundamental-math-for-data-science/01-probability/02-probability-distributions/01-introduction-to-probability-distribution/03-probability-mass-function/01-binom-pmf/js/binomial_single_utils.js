const margin = {
    top: 30, 
    right: 100, 
    bottom: 30, 
    left: 100
};

function getWidthUnit(w, n){
    // Define Width Unit; W / N + 1, includes 0
    return (w / (n + 1))
}

function singleSliderInit(w, h, n, p){
    
    wu = getWidthUnit(w, n)

    var slider = d3
        .sliderHorizontal()
        .min(1)
        .max(n)
        .width(wu * n)
        .ticks(n - 1)
        .displayValue(false)
        .step(1)
        .on('onchange', (val) => {
            var xlabels = Array.from(
                {length: n + 1}, (_, index) => index
            );

            // Prob of (0...n) successes given val trials w. prob == p 
            arr = genBinomialSeries(val, n, p)    
            chartUpdate(arr, xlabels, w, h, n)
        });

    // Calc Width Unit..
    d3.select('#d3-binomPlot-slider')
        .append('svg')
        .append('g')
        .attr("transform", "translate(" + (margin.left + (wu/2)) + ",30)")
        .call(slider);
}

function chartUpdate(arr, xlabels, w, h, n){

    wu = getWidthUnit(w, n)
    
    // Remove the current binomial plot
    var svg = d3.select("svg");
    
    svg.selectAll("#d3-binomPlot > *")
        .remove();

    // Generate the binomial plot; new, re-render the bars
    var svg = d3.select("svg")
            .append("g")
            .attr("transform", "translate(" + (margin.left) +  "," + (margin.top) + ")");

    // Set default scale and axis (X)
    var xR = d3.scaleLinear()
        .domain([0, n+1])
        .range([0, w]);

    // Set default scales and axis (Y)
    var yR = d3.scaleLinear()
        .domain([0, 0.55])
        .range([h, 0]);

    // NOTE: fc (from package d3fc) enhances d3 axis w. additional functionality
    // drop in for d3.axisBottom(); required for centered labels
    svg.append("g")
        .attr("transform", "translate(0," + h + ")")
        .call(
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
                .ticks(n+1)
                .tickFormat(d3.format(",.2f"))
        )
        
    // Generate a new series of bars w. variable colors, opacity, etc. 
    // based on state of the slider and the return P(x)
    svg.selectAll(".bar")
        .data(arr)
        .enter()
        .append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return xR(d.successes) + wu * .04; }) // multiplication term for (0.08 *  widthUnit) gap between bars
            .attr("y", function(d) { return yR(d.p); })
            .attr("width", function() { return wu * .92; }) // multiplication term for (0.08 *  widthUnit) gap between bars
            .attr("height", function(d) { return Math.max(h - yR(d.p), 0); }) // Max @ 0 to prevent console returning floating point errors e.g. `1.2x10^-12 is not valid height` 
            .attr("fill", "#10162F")
            .style("opacity", 0.8)
            .on("mousemove", function(event, d){
                    // When using single slider; use ub
                    tooltip = d3.select('.tooltip')                    

                    tooltip.html(
                        "P("+ d.successes +" Heads | " + d.trials + " Trials) = "  + (d.p.toFixed(3)) + "<br>")
                        .style("left", (event.clientX) + 20 + "px")
                        .style("top", (event.clientY) + "px")
                        .style("opacity", 1);  
                }    
            )
            .on("mouseout", function(){ 
                tooltip.style("opacity", 0);	
            });
        
    // text label for the y axis
    svg.append("text")    
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left )
        .attr("x", 0 - (h / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Probability");
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
    // given a probability of success (p).
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
    // Set Number of Trials
    const trials = 10;
    const pSuccess = 0.5;

    var svgNode = d3.select('svg').node();

    var width = svgNode.getBoundingClientRect().width - margin.left - margin.right;
    var height = svgNode.getBoundingClientRect().height  - margin.top - margin.bottom;

    // Init w. default state. Success == 0, P == 0.5, For single 
    // slider app, start chartUpdate w. no upper (ub) or lower (lb) bounds 
    var xlabels = Array.from(
        {length: trials + 1}, (_, index) => index
    );

    var arr = Array.from(
        {length: trials + 1}, (_, index) => 0
    );

    // Prob of (0...n) successes given val trials w. p == 0.5 (hardcoded!)
     
    chartUpdate(arr, xlabels, width, height, trials)

    // Init slider w. default state, width of each tick == w/n+1, leaves room
    // for zero
    singleSliderInit(width, height, trials, pSuccess)
}