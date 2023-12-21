---
layout: default
title: "Money Mov(i)es"
---
<head>
<script src="https://github.com/epfl-ada/ada-2023-project-fivefrenchspeakingpeoplenocap/blob/page/docs/assets/js/main.js"></script>
</head>
<div class="story-header">
    <h1>Money Mov(i)es</h1>
</div>

Lights, Camera, Analysis! Roll out the red carpet, because we're diving into the world of movies, where popcorn isn't the only thing popping – so are economic trends! Ever wondered if classic blockbusters like "Gone with the Wind" would give modern marvels a run for their money if we time-travel their earnings to today? Spoiler alert: when you toss inflation into the mix, some oldies might just top the charts. Zooming out, our world's economic rollercoaster seems to have a VIP seat for the movie industry. Does a country's wallet size, measured in GDP, dictate if its films will be box office hits or misses? Interestingly, this cinematic puzzle might have more twists than a thriller movie! Grab your 3D glasses, as we embark on this data-driven adventure, blending the art of cinema with the science of analysis!

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
<div class="elfsight-app-e405de8e-e0dc-4680-a320-38e64a6d668b" data-elfsight-app-lazy></div>

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

<p>\( \text{Adjusted Value} = \left( \frac{\text{Current Value}}{\text{CPI in Current Year}} \right) \times \text{CPI Base Year} \)</p>

- **Current Value:** The original revenue or budget of the movie.
- **CPI in Current Year:** The Consumer Price Index in the year the movie was released.
- **CPI Base Year:** The Consumer Price Index in the base year (2012).

<q> Fun Fact: On average, a movie ticket in 1960 cost around $0.69, while the average movie ticket price in 2023 is $10.53. </ins>

### When adjusted for inflation, how does the revenue of older movies compare to recent modern movies?
<div id="revenueChart"></div>

<iframe src="{{ '/assets/revenue_over_time.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

The plot above shows the movies with highest revenues for each year. As we can see, the maximum revenue per year is increasing over time. So, to accurately compare movie revenues over time, we need to account for inflation. Without this adjustment, comparing movies from different eras becomes misleading. Older movies, which might have been very successful, will seem less profitable due to the lower ticket prices at their time. 
After adjusting the revenue for inflation, the peaks in the revenue trends become more pronounced. We can see that some older movies actually have higher inflation-adjusted revenues than newer ones, which wouldn't be apparent if we only looked at nominal revenues. It's like watching a plot twist (pun intended). Some classics are giving modern blockbusters a run for their money! Now, let's look at the top 5 movies with highest revenues.

<table>
  <tr><th>Title</th><th>Year</th><th>Revenue</th><th>Revenue Adjusted</th></tr>
  <tr><td>Titanic</td><td>1997</td><td>$2.185 billion</td><td>$3.126 billion</td></tr>
  <tr><td>Love with the Proper Stranger</td><td>1963</td><td>$415 million</td><td>$3.111 billion</td></tr>
  <tr><td>Avatar</td><td>2009</td><td>$2.782 billion</td><td>$2.978 billion</td></tr>
  <tr><td>Star Wars Episode IV: A New Hope</td><td>1977</td><td>$775.4 million</td><td>$2.937 billion</td></tr>
  <tr><td>The Exorcist</td><td>1973</td><td>$441.1 million</td><td>$2.281 billion</td></tr>
</table>

Ever heard of 'Love with the Proper Stranger'? Yeah, we haven't heard either, yet it beats movies like Avatar and Star Wars in revenue when adjusted for inflation. Quite an unexpected twist...

### Is there a notable trend in the budget of movies over the years when considering inflation?
As we've delved into the world of box office revenues, we've witnessed some surprising twists. But what about the money poured into making these cinematic masterpieces? Let's turn our spotlight to the budgets of these films. When we adjust for inflation, the plot thickens: the inflation-adjusted budgets consistently outpace the nominal budgets. This isn't just a trivial detail; it's a clear indicator of how inflation has been playing a significant role in the movie-making business over time.

<iframe src="{{ '/assets/budget_over_time.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

As we trace the lines of both nominal and inflation-adjusted budgets, an intriguing pattern emerges. There's a discernible upward trajectory, revealing that the investments in high-budget movies have been steadily climbing over the decades. This trend raises some questions: What drives this continuous increase in movie budgets? Is it the pursuit of more "flashy" special effects or the cost of A-list stars? Maybe it's the overall growth of the industry? As the economy grows, the movie industry seems to grow with it. We will explore this in the following section.

## Global Economic Growth and its Influence on the Movie Industry
Gross Domestic Product (GDP) is the total cash value of everything produced within the nation - a true heartbeat of the country's economy. It's a great economic growth indicator because it tells us how healthy the economy is. When it comes to movies making bucks, GDP is a big deal. A high GDP means people have more money to spend on tickets and popcorn. This way we can see the impact that economic growth has on movie revenue, by comparing how well the two move together.

We kick off, with a simple graph with relative yearly values of the world's GDP and mean movie revenue, spanning from 1960 to 2012. Our eyes are the primary sense that allows us to delve into the cinematic experience - and they can also help us quickly assess the relation between the two.

<iframe src="{{ '/assets/world_gdp_vs_mean_movie_revenue.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

At first glance, this may look like a catastrophic flop. Something that would make a movie studio completely abandon the idea... But wait! Look at the correlations! Both Spearman and Pearson coefficients indicate a high level of correlation between the two time series and are backed, by p-values way smaller than 0.05. We can confidently say that even if the two are not moving tightly together, they still show similar behavior and like to either grow or shrink at the same time.

Some John Doe can now wonder: "Hmm, okay... But nothing in life is this simple. There have to be some deviations from this relation. I can't believe that some random third-world country's GDP correlates with movie revenue the same as the cradle of the movie industry that the USA is". And it is a completely logical argument. We would expect that the correlation between GDP and movie revenue of rich countries will be bigger than countries that are still in the early development phase - they just have more money to spend on the entertainment industry.

To try and unravel whether this common sense logic is true, we can move from the whole screen to separate pixels - zoom in to how the GDP of each of the countries correlates with movie revenue. 

<iframe src="{{ '/assets/gdp_revenue_correlation.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

Now that is a very interesting picture. We see that there certainly are divergences from how the worlds GDP correlates with movie revenue. Whats even more interesting - correlation is still quite high for developing countries in Africa, but the whole post-soviet region glows green. Is this a cold war stigma? Between 1960 and 1989, when the Iron Curtain was still casting shadow, most of the western movies were either completely unavaible in this part of the world or their screenings were delayed significantly. Let's take a closer look.

<q> Fun Fact Again: *Star Wars* made it to Hungarian cinemas almost two years after it's official release. </q> 

<iframe src="{{ '/assets/gdp_revenue_correlation_ussr.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

After separating the correlations of the USSR, its satellite and aligned countries, and the rest of the world, we can see that the distributions are different. We also confirmed it, by the p-value of (oh, the irony) Kolmogorov-Smirnov test smaller than 0.05. It really looks like there are regional differences in how the GDP and movie revenue are related, and we have strong reasons to believe that it is a consequence of the soviet rule - thankfully, one of the most harmless ones.

## Determinants of a Movie's Financial Success

For some, movies are simply a gateway to entertainment, a captivating escape into different worlds and stories. Yet, for others, they're not just about the thrill of storytelling; they're a strategic avenue to make money, navigating the intricate balance between creativity and commerce. Can moviemakers, directors or investors shape the movie's financial destiny by tweaking certain factors? Let's find out!

### Budget and Revenue
While it's a piece of cake to separate low and high budget movies, don't let the numbers fool you into thinking financial success is a done deal. Movie magic is not just about fat wallets - it is about the right mix of many ingridients. In this section, we will specifically take a closer look at the relationship between budget and revenue. 

First, let's take a look at the distribution of the budget and revenue and see how money moves at a high level.

[ADD PLOT HERE]

Even though the budget is not the only deciding factor, it is one of the key ingredients in the recipe for financial success. Given the plots, it is clear that throwing in some extra bucks can make a big difference in rising the revenue. However, money is not infinite, and scoring a high revenue comes at scary risk - moviemaker elites do not want to waste money! It is then of huge importance to accordingly spread the budget to optimize the other ingredients. You wouldn't want to spend millions on hiring Amber Heard, when you could cast Johnny Depp instead, right?

[MAYBE ADD AMBER HEARD MEME]

In order to measure the real financial success of a movie, we will introduce two additional metrics given the budget and revenue: Profit and Return of Investment. 

### Profit
In this analysis, we define profit as the difference between the revenue and the budget. We are aware that other factors influence the profit of a movie, such as overpriced merch or streaming rights (unless you enjoy living on the edge and torrenting movies). However, we will not take these factors into account, as they are not available in our dataset.

[ADD PROFIT FORMULA]

The aim is to maximize the profit, but if the movie is a flop and generates less revenue than the budget, the moviemakers can go home and cry in the corner with their empty pockets. Though, some get lucky and manage to obtain high numbers in profit and then go cool off on Bora Bora.

Let's discover some movies that have made it to the top and bottom of the profit charts.

[ADD 2 TABLES HERE]

You have probably been crying while watching "Titanic", having nightmares while running away from the dinosaurs from "Jurassic Park", or forget everything you have studied for before an exam like Dory from "Finding Nemo". These movies are in the top-5 list of highest grossing movies which gained an enormous and exceptional revenue compared to their budget and revenue gained by other movies. Contradictingly, the movies in the bottom-5 list are unheard of and we cannot make cool references as before. These movies are less known and are significantly underperforming in terms of profit when compared to the other movies.

Now, check this out! The top dogs have an impressive average rating on IMDB, a cool 8.36. People love them. But those struggling movies down below? Not so much. Their average rating is a meh 5.28. Ouch! We will take a greater look into movie ratings a litter later on in this datastory, stay tuned!

#### A paradox?
Maybe by now you have noticed the contradiction: we claimed that budget and revenue have a love story going on and are positively correlated, but yet some movies make a negative profit. How could this be possible? In the beginning we had also mentioned that budget is not the only factor in determening the revenue. In fact, this is a love triangle (or maybe even octagon) where other factors, such as the movie genre or the cast, play a role in determining the profit as well. Therefore, do not jump straight into conclusion that you can become a moviemaker if you are rich - the risk is still very high to go bankrupt!

[ADD BOX OFFICE BOMBS FUN FACT]

#### Profit Trend Over Time

Now that we have a better understanding of the profit, let's take a look at how it has evolved over time. We will plot the average profit of movies released in each year. Should we expect to see more movies with higher profit in the future?

[ADD PLOT HERE]

Stepping back and looking at the big picture, it seems as if the average profit is taking a bit of a dip over time. It's not really bumpy, and the numbers are smoothing out. There are some significant outliers, so we decide to show you the years with the highest and lowest average profit.

[ADD NUMBERS HERE]

The 90s were tough, but "The Sound of Music" was tougher, boosting 1965 as they year with the highest average profit. Just 4 years before, we have the lowest average, declaring 1961 as the sad year for the movie industry.

But, does the year of release for a movie statistically and significantly influence the profit? We perform a one-way ANOVA test and impose the null hypothesis as following:

$H_0$: *The average profit is the same for all years.*

What we observed is a p-value smaller than 0.05, so we throw the null hypothesis in the trash and welcome the alternative one with open hands. This means, average profits are statistically different for different years. In addition, we performed a Spearman correlation test which further cleared the doubts and revealed a negative correleation between the year and the profit. Sad news, but profit is decreasing over time. However, we cannot clearly separate the factors that influence the decrease in profit for now.

#### Profit Outliers
What were the chances that a movie made an outstanding profit in the past? We will do a box-plot and try to characterize the outliers.

[ADD PLOT HERE]

There are in total 171 movies (red dots) that are above the 95th percentile in terms of profit. These giant movies throw under the bus the other movies when it comes to comparing money. Interestingly enough these movies represent only **2.38%** of the total available movies. The question now is can we translate this chance into the future? It's a hard question to answer, but if we assume that our dataset is equivallently representative of the entire movie collection, we can estimate that the number is in similar proportion, perhaps even less as profit is decreasing over time.

[TODO]

<form id="inputForm">
  <label for="textInput">Enter Text:</label>
  <input type="text" id="textInput" name="textInput">

  <!-- Submit button -->
  <button type="button" onclick="checkInput()">Submit</button>

  <!-- Display result -->
  <p id="result"></p>
</form>

### Return of Investment (ROI)
In addition to profit, we will also take a look at another metric - return of investment. ROI is the percentage of the original investment that was gained or lost. It is calculated as follows:

[ADD FORMULA]

We can claim that ROI is a more representative metric of the success as it is a relative measure of financial success or failure in terms of percentage of the original investment. Wouldn't it be nice to earn a lot of money despite being tight on cash and quadriple your initial investment?

Let's take a look at the movies with higest ROI. Will they be the same movies as the ones with highest profit?

[ADD TABLE HERE]

The first observation is that these movies do not match with the highest-profit ones. These movies did more with less. Despite having possibly smaller budgets, they rocked a way higher ROI than the big-budget blockbusters. This is due to the fact that ROI is relative measure of success or failure in terms of percentage of the original investment, rather than an absolute one. It goes to show, it's not just about the money you throw in – smart moves and clever choices play a killer role in a movie's financial success.

### Ratings


Let's briefly dive into movie ratings and how they tie into a film's financial success. We're opting for IMDb ratings as a source for a movie's quality and popularity. While we won't focus too heavily on this part and pretend we are Sherlock Holmes, we will still aim to unveil some intriguing observations through our exploratory data analysis. Moreover, movie ratings are given after the movie is released, so they can't be used to predict the movie's financial success. It would be completely biased!

Here is a quick overview of the ratings distribution on the plot below.

[ADD PLOT HERE]

Movies can get around with ratings ranging from 1 to 10, but the party seems to happen mostly between 6 and 7. We're however going along with the assumption that once a squad of viewers has watched the movie, the rating converges into a real ground value. Even though people may see the same number differently (a 7 for you might be a hit but a miss for someone else), we're running with it for our analysis as these numbers don't tell the full story – no neat labels to put on a movie based on a number rating alone. 

Can we somehow connect the inital budget to the rating? Should I expect to get a 10 if I put in a budget more than any other movie?

[ADD PLOT HERE]

Unfortunately, the answer might disappoint you. The horizontal regression line is as flat as it can get. Even if you borrow the entire net worth of Elon Musk, getting out of a 6 is a nearly impossible job, you are still going to be an average moviemaker.

#### Ratings Over Time

In this part, we try to capture the relationship between the release year and the rating. How does the rating trend change over time?

[ADD PLOT HERE]

While the average rating across the years consistently swings between a respectable 6 and 7, a visible trend is emerging – a subtle decline in this cinematic metric over time. The reasons behind this intriguing shift remain a mystery, suggesting further analysis to explore the correlations at play.


As a final exploration, we try to group the best and worst rated movies for each year and compare their profit gaps. How much financially better are the best rated movies compared to the worst rated movies?

[ADD PLOT HERE]

The gap in profits between the best and worst-rated movies is, on average, quite big – around 49 times. This means the top-rated movies make about 44 times more money than the lowest-rated ones. For example, in 1973, "The Sting" made a whopping 1174 times more profit than "The Crazies."

Interestingly, there are times when low-rated movies make more money than high-rated ones. This might be because of other factors, like the popularity of the actors. In 2011, "Warrior" had a much higher rating than "Justin Bieber: Never Say Never," but it made way less money. That's because Justin Bieber's huge fanbase turned up to watch his movie, despite it not getting great reviews. It goes to show that sometimes, what critics say doesn't always match up with what audiences want to see. Never say never to earning some cash despite a low rating!

## Influence of the 2007-2008 Global Financial Crisis on the Movie Industry
In 2007 and 2008, the world faced a big financial crisis, shaking economies everywhere. This crisis even reached into the world of movies, an industry known for big spending and earnings. We will now look at how this financial crisis might have changed how much money was spent on making movies and how much they earned. Did movie makers have to cut down their costs? Did people stop going to the movies as much because they had less money to spend? Let's find out how this big financial event impacted the world of movies, both in making them and in how much they earned.

### Did the 2007-2008 Global Financial Crisis influence movies' revenues?
To uncover how the 2007-2008 Global Financial Crisis might have affected movie revenues, we'll look at the movies in three parts: movies released before, during, and after the crisis. Think of it as a three-act story in the world of movies.

By plotting the average movie revenues for each period, our initial findings show a drop in revenues during the crisis. To dig deeper, we used an ANOVA test, showing us that these changes are significant - the revenues really did vary across these periods. If we take a closer look with a post-hoc analysis, we can reveal that the most noticeable change happened between the movies released before and during the crisis. This suggests that the financial crisis did have a notable impact on movie revenues. But, it's important to remember that this doesn't prove the crisis was the only reason for the change. Other factors could also have played a part. Just like in a movie, there's often more to the story than meets the eye.

<iframe src="{{ '/assets/average_revenue_periods.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

### Was the budget of the movies affected by the 2007-2008 Gorldwide Financial Crisis?
Next, we turn our focus to the budgets of movies in the same three periods: before, during, and after the 2007-2008 Global Financial Crisis. This time, we're curious to see if the crisis had any impact on how much was spent on making movies.

Our initial plot shows something interesting: movie budgets seem to be slightly higher after the crisis. However, the overlapping confidence intervals suggest that these changes might not be significant, so we run an ANOVA test, just like we did for the revenues.
The results showed no significant difference in movie budgets across these periods. Despite the slight ups and downs we see in the plot, statistically speaking the crisis didn't bring major changes in how much movies cost to make.
<iframe src="{{ '/assets/average_budget_periods.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

## Correlation Between Movie Content and Financial Success
[Content for this section]
### Are money-related movies more frequent after the Global Financial Crisis?
Intriguing question right? We performed document retrieval using the universal sentence encoder to embed the movie plots a query. That led us to find 1000 movies related to money. Here's a word cloud showing the most common words in these money-themed movie plots. You'll notice that words like 'money', 'wealthy', 'life', 'financial', 'crime', and 'business' pop up a lot.

<img src="https://github.com/epfl-ada/ada-2023-project-fivefrenchspeakingpeoplenocap/assets/58995762/c9475360-fdac-404f-ac2d-3e2324c1968a" width="100%">


Okay, so now that we have successfully found the movies that are money related, we need to group and count them by year, so we can visualize to determine whether there is a trend between the Global Financial Crisis and money-related movies.
<iframe src="{{ '/assets/money_movies_over_time.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

We can see a clear spike after the year of 2008. Next, we will compare the frequency of money-related movies to the overall number of movies produced each year.This way, we can figure out if there's really an uptick in the share of these money movies, or if it's just a side effect of more movies being made in general.  We're focusing on the post-2008 era because we're super curious about how the big financial crash back then might've influenced the kind of money stories hitting the big screen. If we look at a larger period other financial ups and downs might muddle the picture we're trying to get.

<iframe src="{{ '/assets/proportion_money_movies_over_time.html' | relative_url }}" width="100%" height="500" frameborder="0"></iframe>

Such a huge event shook the whole world, so it's no surprise it popped up in movies too. But here's something interesting – there's a bit of a delay, like 1-2 years, before we see a real jump in these money-themed movies. This delay might be because it takes a movie about 1-2 years from start to finish. It's like the financial crisis left its mark on the movie world, but it took a little while to show up on the big screen.
## Predictive Analysis of Movie Revenue

[Content for this section]
