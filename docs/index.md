---
layout: default
title: "I love Bojan"
---
<div class="story-header">
    <h1>The Impact of KURWA BOBER</h1>
</div>

# I love Bojan
PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO PIWO

## And Stefan

[This song's mood slaps](https://youtu.be/AUHDbzCVK1E?si=9jNx17OTC5X39hu6)
### And you girls

<div id="myPlot" style="width:100%;height:400px;"></div>
<script>
    var trace1 = {
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        type: 'scatter'
    };

    var layout = {
        title: 'Relation of piwo to happiness',
        xaxis: {
            title: 'Piwo',
        },
        yaxis: {
            title: 'Happiness'
        }
    };

    Plotly.newPlot('myPlot', [trace1], layout);
</script>

## Word Map Plot Example

Below is an example of a word map plot using Plotly:

<div id="worldGdpMap" style="width:100%;height:500px;"></div>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv').then(function(rows) {
        function unpack(rows, key) {
            return rows.map(function(row) { return row[key]; });
        }

        var data = [{
            type: 'choropleth',
            locations: unpack(rows, 'CODE'),
            z: unpack(rows, 'GDP (BILLIONS)').map(Number),
            text: unpack(rows, 'COUNTRY'),
            colorscale: [
                [0, 'rgb(5, 10, 172)'], [0.35, 'rgb(40, 60, 190)'],
                [0.5, 'rgb(70, 100, 245)'], [0.6, 'rgb(90, 120, 245)'],
                [0.7, 'rgb(106, 137, 247)'], [1, 'rgb(220, 220, 220)']
            ],
            autocolorscale: false,
            reversescale: true,
            marker: {
                line: {
                    color: 'rgb(180,180,180)',
                    width: 0.5
                }
            },
            colorbar: {
                autotic: false,
                tickprefix: '$',
                title: 'GDP<br>Billions US$'
            }
        }];

        var layout = {
            title: '2014 Global GDP<br>Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">CIA World Factbook</a>',
            geo: {
                showframe: true,
                showcoastlines: true,
                margin: {
                l: 50, // left margin
                r: 50, // right margin
                t: 100, // top margin
                b: 50 // bottom margin
                },
                projection: {
                    type: 'robinson'
                }
            }
        };

        Plotly.newPlot("worldGdpMap", data, layout, {showLink: false});
    }).catch(function(error) {
        console.error('Error loading or parsing data', error);
    });
</script>
