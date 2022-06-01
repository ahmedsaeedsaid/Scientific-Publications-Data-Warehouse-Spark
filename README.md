# Scientific-Publications-Data-Warehouse-Spark
The purpose is to extract data about scientific publications from JSON data that describe, title, topic, authors, etc. about a huge number of papers and populate a data warehouse in order to issue analytics queries using SQL. We will use Spark DataFrames to extract and transform the data. We will use also Spark tables (delta tables) to be used for dimensions and fact table as will be shown below.

the data source: https://www.aminer.org/citation
