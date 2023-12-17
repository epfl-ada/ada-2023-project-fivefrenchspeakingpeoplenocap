---
layout: default
title: "I love Bojan"
---
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
# Money Mov(i)es

## Introduction
Lights, Camera, Analysis! Roll out the red carpet, because we're diving into the world of movies, where popcorn isn't the only thing popping – so are economic trends! Ever wondered if classic blockbusters like "Gone with the Wind" would give modern marvels a run for their money if we time-travel their earnings to today? Spoiler alert: when you toss inflation into the mix, some oldies might just top the charts. Zooming out, our world's economic rollercoaster seems to have a VIP seat for the movie industry. Does a country's wallet size, measured in GDP, dictate if its films will be box office hits or misses? Interestingly, this cinematic puzzle might have more twists than a thriller movie! Grab your 3D glasses, as we embark on this data-driven adventure, blending the art of cinema with the science of analysis!

## Goals and Objectives
Ever wondered what's really going on behind those glitzy movie premieres and blockbuster earnings? Well, we're pulling back the curtain to reveal the economic drama behind the silver screen! So, grab your popcorn, and let's dive into the world of movie economics.

Here's the blockbuster lineup of questions we're tackling:
- **Inflation and Trends in the Movie Industry:** When adjusted for inflation, how does the revenue of older movies compare to recent modern movies? Is there a notable trend in the budget of movies over the years when considering inflation?
- **Global Economic Growth and its Influence on the Movie Industry:** What is the relationship between global economic indicators (like GDP) and movie's gross revenue? Are there regional differences?
- **Determinants of a Movie's Financial Success:** How do factors like budget, runtime, and movie ratings impact the movie's revenue or profitability?
- **Influence of Global Events on the Movie Industry:** How have significant global events, such as the Global Financial Crisis in 2007-2008, influenced movie budgets and revenues?
- **Correlation Between Movie Content and Financial Success:** Does the frequency of money-related words in movie plot summaries correlate with box office success? Are they more frequent after the Global Financial Crisis?
- **Predictive Analysis of Movie Revenue:** Can a regression model using variables like budget, GDP, country, runtime, and release year effectively predict a movie's revenue?

## Inflation and Trends in the Movie Industry
As we journey through the glitz and glamour of the movie industry, let's take a moment to adjust our lenses for inflation. It's like time-traveling with numbers! Did you know that without this adjustment, comparing the box office success of "Gone with the Wind" to "Avengers: Endgame" is like comparing apples to space shuttles? Let's dive into the real score of movie revenues when we level the playing field with inflation.

### Understanding Inflation
Imagine buying a movie ticket in the 1960s. Now, fast forward to today's prices. That's where the Consumer Price Index (CPI) comes into play. It's our financial time machine:

$$ \text{Adjusted Value} = \left( \frac{\text{Current Value}}{\text{CPI in Current Year}} \right) \times \text{CPI Base Year} $$

- **Current Value:** The original revenue or budget of the movie.
- **CPI in Current Year:** The Consumer Price Index in the year the movie was released.
- **CPI Base Year:** The Consumer Price Index in the base year (2012).

Fun(not) Fact: On average, a movie ticket in 1960 cost around $0.69, while the average movie ticket price in 2023 is $10.53.

<div id="revenueChart"></div>

<iframe src="{{ '/assets/revenue_over_time.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

After adjusting for inflation, it's like watching a plot twist, pun intended. Some classics are giving modern blockbusters a run for their money! Check out this table:

| Title                           | Year | Revenue       | Revenue Adjusted |
|---------------------------------|------|---------------|------------------|
| Titanic                         | 1997 | $2.185 billion | $3.126 billion   |
| Love with the Proper Stranger   | 1963 | $415 million   | $3.111 billion   |
| Avatar                          | 2009 | $2.782 billion | $2.978 billion   |
| Star Wars Episode IV: A New Hope| 1977 | $775.4 million | $2.937 billion   |
| The Exorcist                    | 1973 | $441.1 million | $2.281 billion   |

Ever heard of 'Love with the Proper Stranger'? Yeah, we haven't heard either, yet it beats movies like Avatar and Star Wars in revenue when adjusted for inflation. Quite the unexpected twist...

## Is there a notable trend in the budget of movies over the years when considering inflation?
As we've delved into the world of box office revenues, we've witnessed some surprising twists. But what about the money poured into making these cinematic masterpieces? Let's turn our spotlight to the budgets of these films. When we adjust for inflation, the plot thickens: the inflation-adjusted budgets consistently outpace the nominal budgets. This isn't just a trivial detail; it's a clear indicator of how inflation has been playing a significant role in the movie-making business over time.

<iframe src="{{ '/assets/budget_over_time.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

As we trace the lines of both nominal and inflation-adjusted budgets, an intriguing pattern emerges. There's a discernible upward trajectory, revealing that the investments in high-budget movies have been steadily climbing over the decades. This trend raises some questions: What drives this continuous increase in movie budgets? Is it the pursuit of more "flashy" special effects, the cost of A-list stars, or the overall growth of the industry? Whatever the reasons, one thing is clear – the world of cinema is not just evolving in its storytelling and technology but also in its economic footprint. 

## Global Economic Growth and its Influence on the Movie Industry
[Content for this section]

## Determinants of a Movie's Financial Success
[Content for this section]

## Influence of Global Events on the Movie Industry
[Content for this section]

## Correlation Between Movie Content and Financial Success
[Content for this section]

## Predictive Analysis of Movie Revenue
[Content for this section]
