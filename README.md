
# Web Scraping and Automation Project

This repository contains scripts for web scraping and browser automation. The projects included are:

flipkart.py: Scrapes data from Flipkart and stores it in a CSV file.

ajio.py: Automates browser scrolling on Ajio to handle infinite scrolling.

searchyoutube.py: Automates YouTube searches and plays song.

extractinstagram.py : scrapes data of given username from instagram




## Installation

#### Clone the repository:

```bash
git clone https://github.com/Khushi-r2005/webScrapping.git
cd web-scrapping
```
#### Installation Required:

install chrome driver in your system
```bash
pip install pandas
pip install requests
pip install BeautifulSoup
pip install selenium
```
## Usage/Examples

### Flipkart Scraper
The flipkart.py script scrapes data (here,list of Iphones) from Flipkart and stores it in a CSV file.

Run the script:
```bash
python flipkart.py
```
The scraped data will be saved in Iphone.csv

https://github.com/Khushi-r2005/web-scraping/assets/128570886/da196ae4-8b13-4efc-8bd4-6e100ce9d59b


### Ajio Scroller
The ajio.py script automates browser scrolling on Ajio to handle infinite scrolling.
1.Ensure you have ChromeDriver installed and it's in your PATH.

2.Run the script:
```bash
python ajio.py
```
The script will scroll through the Ajio website.

https://github.com/Khushi-r2005/web-scraping/assets/128570886/d383c33f-e68f-4a82-9816-cf3d31c108c1

### YouTube Search and Play
The Searchyoutube.py script automates YouTube searches and plays songs.
1.Ensure you have ChromeDriver installed and it's in your PATH.

2.Run the script:
```bash
python Searchyoutube.py
```
The script will open YouTube, search for a specified song, and play it.

https://github.com/Khushi-r2005/web-scraping/assets/128570886/c9284e40-eb08-4e37-8046-e405661f3eb6


### Instagram Scrapper
The extractinstagram.py scrapes data (like profile, followers, followings, number of posts ) and download the post of given username from instagram

Run the script:
```bash
pip install instaloader
```
```bash
python extractinstagram.py
```
