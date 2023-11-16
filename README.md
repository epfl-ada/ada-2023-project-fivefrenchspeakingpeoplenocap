# Title

## Abstract

## 🔎Research Questions

## 📊Proposed additional datasets 
- [**IMDB Datasets**](https://developer.imdb.com/non-commercial-datasets/): We utilized two specific datasets from IMDB: `title.basics.tsv` and `title.ratings.tsv`, which include data for 10 million movies. These were merged with the CMU Movies dataset, by using the movie title, runtime, and release year as a key. This will enrich our primary dataset with the ratings for the movies, which will later be used for exploring the correlation between movie ratings and revenue. 
- [**TMDB Dataset**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset): We used the `movies_metadata.csv` file from this dataset, which provides metadata for over 45,000 movies. This dataset was used in order to extract the budget for the movies. By matching the imdb_id as a key, we enriched the IMDB Dataset with budget information for each movie.
- [**Worldbank Consumer Price Index**](https://data.worldbank.org/indicator/FP.CPI.TOTL?end=2012&locations=US&name_desc=false&start=1990&view=chart): Our analysis integrates the Consumer Price Index data provided by Worldbank. We focus specifically on the CPI data for the United States, which aligns with our dataset's use of USD as the currency for budget and revenue. By using the CPI dataset, we enrich the CMU movie dataset by calculating inflation-adjusted revenue and budget values, allowing us to make an accurate and fair comparison across movies from different years.
- [**Worldbank Gross Domestic Product**](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD): By analyzing the GDP data, we aim to examine how cinema gross revenue and budget trends align with changes in the global economy. Furthermore, this dataset enables us to discover regional differences, if they exist. We are particularly interested in identifying which regions demonstrate a stronger connection between their cinema revenue growth and economic performance.

## 🧮Methods

### Data Loading and Preprocessing
- **Loading Data**: The IMDB, TMDB, CPI, and GDP datasets are loaded using `pandas`. Relative paths and column structures for each dataset are predefined to facilitate the process.
- **Data Merging**: Data is merged using common keys such as `imdb_id`, `movie title`, `runtime`, and `release year`. This is done to combine rating information and budget details.
- **Data Cleaning**: Duplicates are identified and removed. Missing values are appropriately handled, either by removing them or replacing them with meaningful values depending on the context.


## 🗓️Proposed timeline
```

├── 30.10.23 - 05.11.23 - Decide on idea and research questions
│  
├── 06.11.23 - 12.11.23 - Data handling and merging
│  
├── 13.11.23 - 17.11.23 - 
│  
├── 18.11.23 - 26.11.23 - Work on homework 2
│  
├── 27.11.23 - 03.12.23 - 
│    
├── 04.12.23 - 10.12.23 - 
│  
├── 11.12.23 - 17.12.23 - 
│  
├── 18.12.23 - 22.12.23 - 

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
    <th class="tg-0lax">TODOs</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Matea </td>
    <td class="tg-0lax">  </td>
  </tr>
  <tr>
    <td class="tg-0lax">Stefan </td>
    <td class="tg-0lax">  </td>
  </tr>
  <tr>
    <td class="tg-0lax">Bojan </td>
    <td class="tg-0lax">  </td>
  </tr>
  <tr>
    <td class="tg-0lax">Mikolaj </td>
    <td class="tg-0lax"> </td>
  </tr>
  <tr>
    <td class="tg-0lax">Wiam </td>
    <td class="tg-0lax"> </td>
  </tr>
</tbody>
</table>

