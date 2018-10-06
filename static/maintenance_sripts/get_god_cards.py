#gishoo
#3-19-2018
#download all smite god card art

#As of now the script works todo: check if a for the god exists in the images
#folder if so hash both and see if they are the same image if not replace old
#image with the new
###try:
import os        #used for directory changing and os id'ing
import requests  #used to grab the website
from datetime import datetime # used for the timestamps
from bs4 import BeautifulSoup #used to parse the html returned
from fake_useragent import UserAgent #provides headers for requests to use
from time import sleep #slow down requests so to prevent ip timeouts. optional maybe
import random # used for rng
###except ImportError:
#Python 3.5

#this creates the global variable headers to use
ua = UserAgent()
ua.chrome
header = {'User-Agent': ua.chrome}

#Should point to the page where all the god thumbnails are at the bottom of
#the page.
starting_url = "https://smite.gamepedia.com/Smite_Wiki"
#no slash because the <a href> contain slashes
top_level_url = "https://smite.gamepedia.com"

#This script assumes it is being run from the maintenance_scripts directory
#so for downloads it needs to change directories to the images directory.
os.chdir('../images')

def main():

    main_site = requests.get(starting_url, headers=header)
    if main_site.status_code == 200:
        main_site_soup = BeautifulSoup(main_site.text, 'lxml')
        #Returns a list of <a tags that have the href to the individual god pages
        god_pages_list = main_site_soup.select('html > body > div > div > div > div > div > table > tr > td > div > div > center > div > div > span > a')
        #as of 3-19-2018 there are 94 released gods
        for god_page_extension in god_pages_list:
            #the href's point to /<god name> so we need the top level domain
            god_page_url = top_level_url + god_page_extension['href']
            god_site = requests.get(god_page_url, headers=header)
            god_site_soup = BeautifulSoup(god_site.text, 'lxml')
            god_image_url = god_site_soup.find('meta', {'property':'og:image'})['content']

            image_name_tag = god_site_soup.find(id="firstHeading")
            image_name = image_name_tag.text
            with open(image_name + '_default'+ '.jpg', 'wb') as image:
                image.write(requests.get(god_image_url, headers=header).content)


if __name__ == "__main__":
    main()
