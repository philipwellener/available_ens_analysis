# Available ENS Analysis
## By Philip Wellener

### How to Run Analysis
1. Run registered_ens_scrape.py with command line: scrapy runspider registered_ens_scrape.py -o -:csv > registered_ens.csv 2> TRACE

      i. Visually inspect how many pages are in the table on the webpage: https://ens.tools/domains?perPage=250&showFilters=true&expiration=registered. Change line 21 of registered_ens_scrape.py to the total number of pages in the table
      
      ii. This program took about 1 hour to run with 4713 pages (approx. 1.2 million domains) on a Mac M1 chip
  
2. Edit available_words.py on line 32 to run desired file for filtering ENS names. Current available files are:
  
      i. sowpods.csv -> https://www.wordgamedictionary.com/sowpods/download/sowpods.txt
  
      ii. forbes.csv -> top companies according to forbes
  
      iii. baby_names_over_100_2021.csv -> popular baby names in 2021 (more than 100 babies named given name)
  
      iv. pro_athletes.csv -> top paid athletes
  
      v. frequent_words.csv -> frequently used words
    
3. Run available_words.py with command line: python3 available_words.py
4. View output file - output contents contain expired ENS domain names
