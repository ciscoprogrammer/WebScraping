from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from bs4 import BeautifulSoup
import time


chrome_driver_path = r'C:\Users\pillaiyar\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe' 

# Setting up Chrome options
options = Options()
options.add_argument('--headless')  


driver = webdriver.Chrome(options=options)




urls = ["https://www.google.com/shopping/product/r/IN/4230178614358911281/offers?hl=en&prds=eto:17131126769242662962_0;6326090483440549713_0;15248775086782062038_0,pid:11732264193616438339,rsk:PC_16879916843159125235&sa=X&ved=0ahUKEwjA8_bu1ZWDAxWV1zgGHfg7ABQQnbAGCBo",
        "https://www.google.com/shopping/product/r/IN/11023132008453636978/offers?hl=en&prds=eto:14426953020799245486_0;8667074771712969208_0;7617244668650886687_0,pid:13870004559578428055,rsk:PC_7260751228471929012&sa=X&ved=0ahUKEwj67NGLg5aDAxVL-jgGHS04D6oQnbAGCBs",
        "https://www.google.com/shopping/product/r/IN/15404994514283323463/offers?hl=en&prds=eto:17738977628641196277_0;921906337036655219_0;2119468403766887547_0,pid:16529090163249391614,rsk:PC_3197772538215868153&sa=X&ved=0ahUKEwi_wMvphpaDAxUN1zgGHdmQB3MQnbAGCBo",
        "https://www.google.com/shopping/product/r/IN/4040474213320180612/offers?hl=en&prds=eto:14520231140635229900_0;6338084040441038453_0;11163428069106974225_0,pid:9603597453237868931,rsk:PC_1767166610178777258&sa=X&ved=0ahUKEwjB9_erh5aDAxXmyzgGHSKsBM4QnbAGCBo",
        "https://www.google.com/shopping/product/r/IN/1114581155868477883/offers?hl=en&prds=eto:17318724645965405145_0;17142809917890863226_0;4771641477754235277_0,pid:14547521437821686297,rsk:PC_1509139158716623279&sa=X&ved=0ahUKEwjPuePZh5aDAxVgz6ACHdicCWsQnbAGCBw",
        "https://www.google.com/shopping/product/r/IN/10318573556119124665/offers?hl=en&prds=eto:5853521612477268406_0;17127459721609628316_0;4751418741293099822_0,pid:1636047406118797574,rsk:PC_4715517573010967882&sa=X&ved=0ahUKEwjc8KiEiJaDAxWD7zgGHax0Cr8QnbAGCBo",
        "https://www.google.com/shopping/product/r/IN/14730190730529363995/offers?hl=en&prds=eto:18055118078881947271_0;7588958160812610057_0;14279912861262740096_0,pid:6659111570239853740,rsk:PC_17204076376013743666&sa=X&ved=0ahUKEwj6wvTwiJaDAxWEoOkKHcW4AQcQnbAGCBs",
        "https://www.google.com/shopping/product/16348859168733324896/offers?hl=en&psb=1&q=books&oq=books&gs_lcp=Cgtwcm9kdWN0cy1jYxADUABYAGAAaABwAHgAgAEAiAEAkgEAmAEA&sclient=products-cc&prds=eto:3529650260159849863_0,pid:8615590158941496728,rsk:PC_14924321773709793431&sa=X&ved=0ahUKEwjFvsCciZaDAxVYzDgGHc_UCFAQ3q4ECPsJ",
        "https://www.google.com/shopping/product/15142959110214331901/offers?hl=en&psb=1&q=books&oq=books&gs_lcp=Cgtwcm9kdWN0cy1jYxADUABYAGAAaABwAHgAgAEAiAEAkgEAmAEA&sclient=products-cc&prds=eto:5631772050310191915_0,pid:13446482478751855715,rsk:PC_5303122689534223597&sa=X&ved=0ahUKEwjFvsCciZaDAxVYzDgGHc_UCFAQ3q4ECJoK",
        "https://www.google.com/shopping/product/r/IN/14547376552891273523/offers?hl=en&prds=eto:8778875706435999320_0;8920238975617432575_0;15406531198716689607_0,pid:17188523997227842181&sa=X&ved=0ahUKEwjqzc69ipaDAxXW4TgGHWigAf4QnbAGCBs"
]

# Open the page
for url in urls:
    driver.get(url)


    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'sh-osd__online-sellers-cont')))



    soup = BeautifulSoup(driver.page_source, 'html.parser')


    sellers_container = soup.find('tbody', id='sh-osd__online-sellers-cont')



    if sellers_container:
        # Looping through each seller row and extract information
        for row in sellers_container.find_all('tr', recursive=False):
            # Extracting the seller name
            try:
            
                seller_name = row.find('a', class_="b5ycib shntl").get_text(strip=True)
            except AttributeError:
                seller_name = 'Not Found'
            
            try:
                item_price = row.find('span', class_="g9WBQb fObmGc").get_text(strip=True)
                #item_price_tag = row.find('span', class_='gW9lQb f0bmGc')
                #item_price = item_price_tag.get_text(strip=True) if item_price_tag else 'Not Found'
            except AttributeError:
                item_price = 'Not Found'

            try:
                #total_price = row.find('td', class_='drzWO').get_text(strip=True)
                total_price_tag = row.find('div', class_='drzWO')
                total_price = total_price_tag.get_text(strip=True) if total_price_tag else 'Not Found'
            except AttributeError:
                total_price = 'Not Found'

            try:
                visit_site_url_tag = row.find('a', class_="UxuaJe shntl FkMp")
                if visit_site_url_tag and 'href' in visit_site_url_tag.attrs:
                    # Extracting the URL part after 'q=' and before '&'
                    raw_url = visit_site_url_tag['href']
                    visit_site_url = raw_url.split('q=')[1].split('&')[0]

                else:
                    visit_site_url = 'N/A'
            except AttributeError:
                visit_site_url = 'Not Found'




            
            # Printing the extracted information
            print(f"Seller: {seller_name}, Item Price: {item_price}, Total Price: {total_price}, URL: {visit_site_url}")
            print("\n")
    else:
        print("No seller information found on the page.")


driver.quit()
