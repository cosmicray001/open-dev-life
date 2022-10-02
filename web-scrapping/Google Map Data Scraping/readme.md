## _Google Map Scrapping Without API (Using Selenium Web Driver, beautifulsoup and Python Scripting)_

![N|Solid](https://i.ibb.co/FzfzLq4/scrape-google-maps-with-python-and-selenium-removebg-preview.png)
What We'll Need to for making The Scrapper
- Python.
- Chrome Driver 
- Chrome browser.
- Selenium 
- Beautiful Soup.
### Install Selenium And beautifulsoup 

```sh 
pip install selenium
```
```sh 
pip install beautifulsoup4 #to extract required data from HTML using CSS selectors or XPath  
``` 


#### Download the webdriver from here. 
| Plugin | Download Link |
| ------ | ------ |
| ChromeDriver | [https://chromedriver.chromium.org/downloads][PlDb] |

## Steps
Make sure you have the path to your chromedriver file Before initializing Webdriver. You shall see the new Chrome driver open after running the code.
For making the simulation of a genuine browsing experience, we need selenium.
To achieve that have to initialize some delay.
```
startup_delay=5
next_page_delay = 3.5
wait_after_element_loaded= 2
delay_to_check_if_element_visible = 1
load_specific_result_delay = 4
```
### Google map queries

Here, we scraped the resturants data of Bangladesh. You can modify the query link according to your need. Be assure of the current google map query link current format.
```sh
map_query1= "https://www.google.com/maps/search/restaurants+in+Dhaka/&pws=0"
map_query2= "https://www.google.com/maps/search/restaurants+in+Chittagong/&pws=0" 
```
### Beautifulsoup initialization:
```soup = BeautifulSoup(html,'lxml')```
### Webdriver Simulation
ChromeDriver will extract the data till it appears. For more result, we may provide multiple map queries.
![N|Solid](https://i.ibb.co/34RFx1Q/google-maps-HTML-parsing-768x518.png)
#### Language settings to get Specified language result
```sh
options = webdriver.ChromeOptions()
options.add_argument('--lang=en-GB') #Setting language to En-UK
```
## Data Cleaning
After we collect the data through simulation, we have to do some data engineering with **python**

## Results to CSV
Finally, save the acquired the data to your desired format
```sh
df = pd.DataFrame(data=table)
df.to_csv("map_data.csv", encoding='utf-8-sig')
```


## License

MIT

**Open Source**

