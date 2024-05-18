
# Web Scraping and Automation Project

This repository contains scripts for web scraping and browser automation. The projects included are:

flipkart.py: Scrapes data from Flipkart and stores it in a CSV file.
ajio.py: Automates browser scrolling on Ajio to handle infinite scrolling.
searchyoutube.py: Automates YouTube searches and plays song.




## Installation

#### Clone the repository:

```bash
git clone https://github.com/Khushi-r2005/webScrapping.git
cd webScrapping
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

### Ajio Scroller
The ajio.py script automates browser scrolling on Ajio to handle infinite scrolling.
1.Ensure you have ChromeDriver installed and it's in your PATH.
2.Run the script:
```bash
python ajio.py
```
The script will scroll through the Ajio website.

### YouTube Search and Play
The Searchyoutube.py script automates YouTube searches and plays songs.
1.Ensure you have ChromeDriver installed and it's in your PATH.
2.Run the script:
```bash
python Searchyoutube.py
```
The script will open YouTube, search for a specified song, and play it.
