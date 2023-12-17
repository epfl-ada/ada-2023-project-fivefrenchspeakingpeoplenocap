---
layout: default
title: "I love Bojan"
---
<body>
    <div class="header">
        <h1>Money Mov(i)es</h1>
    </div>

<div class="container">
    <!-- Introduction Section -->
    <section id="introduction">
        <p>Lights, Camera, Analysis! Roll out the red carpet, because we're diving into the world of movies, where popcorn isn't the only thing popping – so are economic trends! Ever wondered if classic blockbusters like "Gone with the Wind" would give modern marvels a run for their money if we time-travel their earnings to today? Spoiler alert: when you toss inflation into the mix, some oldies might just top the charts. Zooming out, our world's economic rollercoaster seems to have a VIP seat for the movie industry. Does a country's wallet size, measured in GDP, dictate if its films will be box office hits or misses? Interestingly, this cinematic puzzle might have more twists than a thriller movie! Grab your 3D glasses, as we embark on this data-driven adventure, blending the art of cinema with the science of analysis!</p>
    </section>

<!-- Goals and Objectives Section -->
<section id="goals">
    <h2>Goals and Objectives</h2>
    <p>Ever wondered what's really going on behind those glitzy movie premieres and blockbuster earnings? Well, we're pulling back the curtain to reveal the economic drama behind the silver screen! So, grab your popcorn, and let's dive into the world of movie economics</p>
    
<p>Here's the blockbuster lineup of questions we're tackling:</p>
<ul>
    <li><strong>Inflation and Trends in the Movie Industry:</strong> When adjusted for inflation, how does the revenue of older movies compare to recent modern movies? Is there a notable trend in the budget of movies over the years when considering inflation?</li>
    <li><strong>Global Economic Growth and its Influence on the Movie Industry:</strong> What is the relationship between global economic indicators (like GDP) and movie's gross revenue? Are there regional differences?</li>
    <li><strong>Determinants of a Movie's Financial Success:</strong> How do factors like budget, runtime, and movie ratings impact the movie's revenue or profitability?</li>
    <li><strong>Influence of Global Events on the Movie Industry:</strong> How have significant global events, such as the Global Financial Crisis in 2007-2008, influenced movie budgets and revenues?</li>
    <li><strong>Correlation Between Movie Content and Financial Success:</strong> Does the frequency of money-related words in movie plot summaries correlate with box office success? Are they more frequent after the Global Financial Crisis?</li>
    <li><strong>Predictive Analysis of Movie Revenue:</strong> Can a regression model using variables like budget, GDP, country, runtime, and release year effectively predict a movie's revenue?</li>
</ul>
</section>

<!-- Inflation and Trends in the Movie Industry Section -->
<section id="inflation-trends">
    <h2>Inflation and Trends in the Movie Industry</h2>
    <p>As we journey through the glitz and glamour of the movie industry, let's take a moment to adjust our lenses for inflation. It's like time-traveling with numbers! Did you know that without this adjustment, comparing the box office success of "Gone with the Wind" to "Avengers: Endgame" is like comparing apples to space shuttles? Let's dive into the real score of movie revenues when we level the playing field with inflation.</p>
    
<p><strong>Understanding Inflation:</strong> Imagine buying a movie ticket in the 1960s. Now, fast forward to today's prices. That's where the Consumer Price Index (CPI) comes into play. It's our financial time machine:</p>
<blockquote>
    $$ \text{Adjusted Value} = \left( \frac{\text{Current Value}}{\text{CPI in Current Year}} \right) \times \text{CPI Base Year} $$
</blockquote>
<ul>
    <li><strong>Current Value:</strong> The original revenue or budget of the movie.</li>
    <li><strong>CPI in Current Year:</strong> The Consumer Price Index in the year the movie was released.</li>
    <li><strong>CPI Base Year:</strong> The Consumer Price Index in the base year (2012).</li>
</ul>

<!-- Interactive Plot or Image -->
<div id="revenuePlot">[Interactive Revenue Plot Here]</div>
<script>
    // JavaScript for interactive plot (if applicable)
</script>

<p>After adjusting for inflation, it's like watching a plot twist in the box office saga. Some classics are giving modern blockbusters a run for their money! For instance, when we adjust for inflation, "Titanic" sails past "Avatar" in terms of revenue. Check out this table:</p>

<!-- Styled Table -->
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Year</th>
            <th>Revenue</th>
            <th>Revenue Adjusted</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1990</td>
            <td>Titanic</td>
            <td>1997</td>
            <td>$2.185 billion</td>
            <td>$3.126 billion</td>
        </tr>
        <tr>
            <td>637</td>
            <td>Love with the Proper Stranger</td>
            <td>1963</td>
            <td>$415 million</td>
            <td>$3.111 billion</td>
        </tr>
        <tr>
            <td>2132</td>
            <td>Avatar</td>
            <td>2009</td>
            <td>$2.782 billion</td>
            <td>$2.978 billion</td>
        </tr>
        <tr>
            <td>7103</td>
            <td>Star Wars Episode IV: A New Hope</td>
            <td>1977</td>
            <td>$775.4 million</td>
            <td>$2.937 billion</td>
        </tr>
        <tr>
            <td>2122</td>
            <td>The Exorcist</td>
            <td>1973</td>
            <td>$441.1 million</td>
            <td>$2.281 billion</td>
        </tr>
    </tbody>
</table>

<p>Now, let's settle the debate: Are 'older' movies more successful than 'newer' ones? We're defining 'older' as pre-2000 and 'newer' as post-2000. Spoiler alert: The plot thickens as we look at the data!</p>

<!-- Histogram or Q-Q Plot -->
<div id="movieHistogram">[Histogram or Q-Q Plot Here]</div>
<script>
    // JavaScript for interactive histogram/Q-Q plot (if applicable)
</script>

<p>Our trusty Mann-Whitney U test will help us crack this case. If the p-value is less than 0.05, it's time for a plot twist: there's a significant difference between the old and new movies.</p>
<div class="test-results">
        <h3>Mann-Whitney U Test Results</h3>
        <p><strong>Statistic:</strong> 7,220,205.0</p>
        <p><strong>P-Value:</strong> 9.23e-18</p>
        <p><strong>Median Revenue for Older Movies:</strong> $28,111,512.43</p>
        <p><strong>Median Revenue for Newer Movies:</strong> $19,323,866.66</p>
    </div>

    <div class="conclusion">
        <p>With a p-value way less than our 0.05 threshold, the verdict is clear: <span class="highlight">Older movies have a significantly higher median revenue than newer movies</span> when adjusted for inflation. It seems like the classics aren't just golden in our hearts but also in the box office!</p>
    </div>
<!-- Global Economic Growth and its Influence on the Movie Industry  -->
<section id="global-economic-growth">
    <h2>Global Economic Growth and its Influence on the Movie Industry</h2>
</section>


    <!-- Optional: Add JavaScript or additional scripts here -->

</body>
