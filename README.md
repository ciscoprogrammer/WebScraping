# WebScraping





## Description
This project is designed to scrape product information from Google Shopping pages. It extracts details like seller name, item price, total price, and the URL for each product offer.

## Setup

 
 **Python Version**: Python 3.x

 
 **Libraries Required**:
  - Selenium
  - BeautifulSoup4

    
**Driver Required**: Chrome WebDriver





## Usage


1. **Install Dependencies**: 
                             Please Ensure whether you have Python 3.x installed along with `selenium` and `bs4` (BeautifulSoup4) libraries. 
                             If not installed, use pip to install them:


   
          pip install selenium bs4
   


2. **WebDriver**: Download the Chrome WebDriver and place it in a known directory. Update the `chrome_driver_path` in the script to point to this file.






3. **Running the Script**: Run the script using Python.
   
   python webScraping.py




   
4. **Output**: The script prints the extracted information for each seller in the console.





## Please Note
  The script runs in headless mode. No browser UI will be displayed during its execution.
  

