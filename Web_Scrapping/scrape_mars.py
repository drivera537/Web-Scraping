from splinter import Browser #Allows to click thru the browser
from bs4 import BeautifulSoup as bs #Scrape library to retrieve infofrom html
import time
import pandas as pd #dataframes
from urllib.parse import urlparse #library use to get the base_url

# set path with locar chrome driver

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

# Define a scrape function

def scrape():
    browser = init_browser()
    mars_scrape_data = {}
    urlNews = "https://mars.nasa.gov/news/"
    browser.visit(urlNews)
    time.sleep(5)
    html = browser.html
    soup = bs(html, "html.parser")

    # Mars news
    title_element = soup.find('div', {'class': "content_title"})
    for title in title_element:
        title = title_element.find_all('a')[0].text

    date = soup.find_all('div', {"class": 'list_date'})[0].text
    paragraph = soup.find_all('div', {'class': "article_teaser_body"})[0].text

    article_data = {
                "article_date" : date,
                "article_title" : title,
                "article_synopsis": paragraph
    }
    mars_scrape_data['news'] = article_data
    
    #featured images
    o = urlparse("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")

    base_url = o.scheme + "://"+ o.netloc
    base_url

    imageUrl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(imageUrl)

    html_image = browser.html
    image_soup = bs(html_image, "html.parser")

    full_image = browser.find_by_id('full_image')
    full_image.click()

    time.sleep(5)

    to_main_image = browser.find_by_text('more info     ')
    to_main_image.click()

    time.sleep(5)

    html_image = browser.html
    soup = bs(html_image, "html.parser")

    i_path = soup.find("section", {'class': "content_page module"})
    image_path = i_path.find_all('img')[0]['src']

    image_url = base_url + image_path
    
    mars_scrape_data['featured_image'] = image_url
    
#     Weather
    
    weather_url = "https://twitter.com/marswxreport?lang=en"
    weather_url

    browser.visit(weather_url)

    html_weather = browser.html
    weather_soup = bs(html_weather, "html.parser")

    mars_weather = weather_soup.find("p", {"class" : 'tweet-text'}).get_text()
    
    mars_scrape_data['weather'] = mars_weather
    
     # Facts Table
    # browser = init_browser()

    url = 'http://space-facts.com/mars/'
    facts = pd.read_html(url)
    facts[0]

    facts_df = facts[0]
    facts_df.columns = ['keys','dimensions']
    to_html = facts_df.to_html()
    html_table = to_html.replace("\n", "")
    
    mars_scrape_data['table'] = html_table
    
    
#     Hemisphere
    
    urlNews = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(urlNews)

    o = urlparse("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    base_url = o.scheme + "://"+ o.netloc
    base_url

    time.sleep(5)

    hemisphere_lst = []

    find_a=browser.find_by_css('div[class="description"] a')
    find_a[0].click()

    time.sleep(5)

    html = browser.html
    hemisphere_soup = bs(html, "html.parser")

    title = hemisphere_soup.find('h2', {"class":"title"}).text

    image_src = hemisphere_soup.find("img", class_="wide-image")["src"]
    image_url = base_url + image_src

    hemisphere_1 = {'title': title, 'image_url' : image_url}
    hemisphere_lst.append(hemisphere_1)

    # go back to starting page
    browser.back()

    time.sleep(5)

    find_a=browser.find_by_css('div[class="description"] a')
    find_a[1].click()

    time.sleep(5)

    html = browser.html
    hemisphere_soup = bs(html, "html.parser")

    title = hemisphere_soup.find('h2', {"class":"title"}).text

    image_src = hemisphere_soup.find("img", class_="wide-image")["src"]
    image_url = base_url + image_src

    hemisphere_2 = {'title': title, 'image_url' : image_url}
    hemisphere_2
    hemisphere_lst.append(hemisphere_2)
    hemisphere_lst

    browser.back()

    time.sleep(5)

    find_a=browser.find_by_css('div[class="description"] a')
    find_a[2].click()

    time.sleep(5)

    html = browser.html
    hemisphere_soup = bs(html, "html.parser")

    title = hemisphere_soup.find('h2', {"class":"title"}).text

    image_src = hemisphere_soup.find("img", class_="wide-image")["src"]
    image_url = base_url + image_src

    hemisphere_3 = {'title': title, 'image_url' : image_url}

    hemisphere_lst.append(hemisphere_3)
    hemisphere_lst

    browser.back()

    time.sleep(5)

    find_a=browser.find_by_css('div[class="description"] a')
    find_a[3].click()

    time.sleep(5)

    html = browser.html
    hemisphere_soup = bs(html, "html.parser")

    title = hemisphere_soup.find('h2', {"class":"title"}).text

    image_src = hemisphere_soup.find("img", class_="wide-image")["src"]
    image_url = base_url + image_src

    hemisphere_4 = {'title': title, 'image_url' : image_url}

    hemisphere_lst.append(hemisphere_4)
    
    mars_scrape_data['hemisphere'] = hemisphere_lst
    browser.quit()
    return mars_scrape_data
scrape()
