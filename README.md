# Money Mov(i)es
## 🎬Data Story
- Check out our [datastory](https://epfl-ada.github.io/ada-2023-project-fivefrenchspeakingpeoplenocap/)!

## 💰Abstract
Lights, Camera, Analysis! Roll out the red carpet, because we're diving into the world of movies, where popcorn isn't the only thing popping – so are economic trends! Ever wondered if classic blockbusters like "Gone with the Wind" would give modern marvels a run for their money if we time-travel their earnings to today? Spoiler alert: when you toss inflation into the mix, some oldies might just top the charts. Zooming out, our world's economic rollercoaster seems to have a VIP seat for the movie industry. Does a country's wallet size, measured in GDP, dictate if its films will be box office hits or misses? Interestingly, this cinematic puzzle might have more twists than a thriller movie! Grab your 3D glasses, as we embark on this data-driven adventure, blending the art of cinema with the science of analysis!

## 🔎Research Questions
1. **Inflation and Trends in the Movie Industry**: When adjusted for inflation, how does the revenue of older movies compare to recent modern movies? Is there a notable trend in the budget of movies over the years when considering inflation?
2. **Global Economic Growth and its Influence on the Movie Industry**: What is the relationship between global economic indicators (like GDP) and movie's gross revenue? Are there regional differences?
3. **Determinants of a Movie's Financial Success**: How do factors like budget, runtime, and movie ratings impact the movie's revenue or profitability?
4. **Influence of the Global Financial Crisis on the Movie Industry**: Did the Global Financial Crisis in 2007-2008, influenced movie budgets and revenues?
5. **Correlation Between Money Related Movies and the Global Financial Crisis**: How has the frequency of money-related movies evolved over time? Are they more frequent before or after the Global Financial Crisis?
6. **Predictive Analysis of Movie Revenue**: Can a regression model effectively predict a movie's revenue? 

## 📊Proposed additional datasets 
- [**IMDB Datasets**](https://developer.imdb.com/non-commercial-datasets/): We utilized two specific datasets from IMDB: `title.basics.tsv` and `title.ratings.tsv`, which include data for 10 million movies. These were merged with the CMU Movies dataset, by using the movie title, runtime, and release year as a key. This will enrich our primary dataset with the ratings for the movies, which will later be used for exploring the correlation between movie ratings and revenue. 
- [**TMDB Dataset**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset): We used the `movies_metadata.csv` file from this dataset, which provides metadata for over 45,000 movies. This dataset was used in order to extract the budget for the movies. By matching the imdb_id as a key, we enriched the IMDB Dataset with budget information for each movie.
- [**Worldbank Consumer Price Index**](https://data.worldbank.org/indicator/FP.CPI.TOTL?end=2012&locations=US&name_desc=false&start=1990&view=chart): Our analysis integrates the Consumer Price Index data provided by Worldbank. We focus specifically on the CPI data for the United States, which aligns with our dataset's use of USD as the currency for budget and revenue. By using the CPI dataset, we enrich the CMU movie dataset by calculating inflation-adjusted revenue and budget values, allowing us to make an accurate and fair comparison across movies from different years.
- [**Worldbank Gross Domestic Product**](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD): By analyzing the GDP data, we aim to examine how cinema gross revenue and budget trends align with changes in the global economy. Furthermore, this dataset enables us to discover regional differences, if they exist.

## 🧮Methods

### Data Loading and Preprocessing

- **Loading Data**: The CMU, IMDB, TMDB, CPI, and GDP datasets are loaded using `pandas`. Relative paths and column structures for each dataset are predefined to facilitate the process.
- **Data Merging**: Data is merged using common keys such as `imdb_id`, `movie title`, `runtime`, and `release year`. We are interested in adding information like the budget, ratings, cpi and gdp from the external datasets to enrich the CMU movies dataset.
- **Data Cleaning**: This involved handling missing values, duplicates and irrelevant features.

### Data Analysis

- **Q1: Inflation and Trends in the Movie Industry**
First, we use the CPI to adjust movie budget and revenue values for inflation, allowing for a fair comparison across movies from different years. We then create line graphs to visually represent the trend of movie revenues and budgets over time. After splitting the movies into two groups, old and new, we test the normality in order to choose the right test for comparing the two groups. Since they do not follow a normal distribution, we perform a Mann–Whitney U test in order to see if there is a difference between the median values of the two groups.

- **Q2: Global Economic Growth and its Influence on the Movie Industry**
We analyze the correlation between global economic indicators (GDP) and movie gross revenues by calculating Pearson and Spearman correlation coefficients. Additionally, we compare the movie industry's growth in different countries or regions to understand differences in the context of global economic growth.

- **Q3: Determinants of a Movie's Financial Success**
Here we explore how different factors impact the movie’s financial success. Furthermore, we calculate the movie’s profit and return of investment as additional metrics of the success of a movie. We perform statistical tests in order to quantify the relationship between these factors and the metrics of the financial success of a movie. 

- **Q4: Influence of the Global Financial Crisis on the Movie Industry**
In order to evaluate the impact of the 2007-2008 financial crisis on the movie budgets and revenues we compare data before, during, and after the event.
We use statistical tests to determine if the differences (if any) pre- and post-event are significant.

- **Q5: Correlation Between Money Related Movies and the Global Financial Crisis**
We first clean the movies' plots, load a pretrained embedding model, and transform the processed plots to embeddings. We then retrieve the top-K plots, using queries that captures the "money-related movies" theme, embed the query using the same pretrained model and calculate cosine similarity between the query and all the plots. This way we extract the movies that are money related, and we compare the frequency of such movies released before and after the global financial crisis.

- **Q6: Predictive Analysis of Movie Revenue**
We use regression-based machine learning models like linear regression and random forest, to predict movie revenues based on the movies’s features. To ensure the model's reliability, we use cross-validation. 

## 🗓️Executed timeline
```

├── 30.10.23 - 05.11.23 - Decide on idea and research questions
│  
├── 06.11.23 - 12.11.23 - Data handling and merging
│  
├── 13.11.23 - 17.11.23 - Q1 & Q3
│  
├── 18.11.23 - 26.11.23 - Work on Homework 2
│  
├── 27.11.23 - 03.12.23 - Q2 & Q4 and leftovers from P2 
│    
├── 04.12.23 - 10.12.23 - Q5 & Q6
│  
├── 11.12.23 - 17.12.23 - Start datastory preparation and polish the code
│  
├── 18.12.23 - 22.12.23 - Final improvements and review on the datastory and code

```

## 👨‍👩‍👧‍👦Organization within the team
<table class="tg" style="table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 16px">
<col style="width: 180px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax">Teammate</th>
    <th class="tg-0lax">Contribution</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Matea </td>
    <td class="tg-0lax"> Loading and cleaning the dataset <br> Develop the datastory webpage <br> Q1 and Q4 </td>
  </tr>
  <tr>
    <td class="tg-0lax">Stefan </td>
    <td class="tg-0lax"> Loading and cleaning the dataset <br> Develop the datastory webpage <br> Q1 and Q5 </td>
  </tr>
  <tr>
    <td class="tg-0lax">Bojan </td>
    <td class="tg-0lax"> Create meaningful visualizations <br> Develop the datastory webpage <br> Q3 and Q5 </td>
  </tr>
  <tr>
    <td class="tg-0lax">Mikolaj </td>
    <td class="tg-0lax"> Loading and cleaning the dataset <br> Code and text revision <br> Q2 <br> Suffered by getting the page to work </td>
  </tr>
  <tr>
    <td class="tg-0lax">Wiam </td>
    <td class="tg-0lax"> Code and text revision <br> Write the README <br> Q6 </td>
  </tr>
</tbody>
</table>
<!-- End --!>
