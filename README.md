# Amazon-Web-Scraping
Amazon Web Scraper is a project focused on extracting product data from Amazon to analyze pricing trends and product availability. This data was used to gain insights into market competition and consumer sentiment, supporting e-commerce decision-making and product optimization strategies. Below is the detailed documentation of the scraping process and data handling

# Projects Report

## A.	Project Overview
	Project Title: Amazon Web Scraping.
	Objective: Scrape specific data from Amazon webpage
	Team Members: Daffa Arkananta

## B.	Data Collection
  ### a.	Tools Used
    1.	Python
    2.	BeautifulSoup4
    3.	Selenium
    4.	Pandas
    5.	CSV

### b.	Data Sources
	Source 1: Amazon Product Listings
	Description: Product data was scraped directly from the Amazon website using automated scripts written in Python. The scraped information includes product names, prices, and links.
	URL or Location: https://www.amazon.com/s?k=neutral+running+shoes&i=fashion&page={i}&content-id=amzn1.sym.8abbd447-1969-42f6-a01f-457e40e4fa71%3Aamzn1.sym.8abbd447-1969-42f6-a01f-457e40e4fa71&pd_rd_r=8e72cf34-b9d6-4578-afd8-6b2dc8928c14&pd_rd_w=0uDqR&pd_rd_wg=srOPY&pf_rd_p=8abbd447-1969-42f6-a01f-457e40e4fa71&pf_rd_r=7F7Y2A6G89DJ8KAWSJ34&qid=1747639307&sprefix=neutral+running+shoes%2Caps%2C98&wi=ff0ec07d-4319-4655-8bd1-84411325856c_1&ref=slsr_runtype_d_t_m_vn_ff0ec07d-4319-4655-8bd1-84411325856c_1
	Data Format: Link.
