
import requests
from bs4 import BeautifulSoup

baseUrl = 'https://www.merriam-webster.com/browse/dictionary/'

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# For each letter in the alphabet, Merriam-Webster has a number of pages of words. We hardcode those numbers here.
pageCount = [72,72,109,58,37,46,41,45,38,11,15,38,62,28,32,101,6,55,134,65,28,16,32,2,5,4]

def scrapeAPage(a,x): 
    url = baseUrl + a + "/" + str(x)
    # acquire HTML data from one of Merriam-Webster's list-of-words webpages
    response = requests.get(url)
    # parse the HTML data with BeatifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # isolate the list of words using Soup's find() methods and CSS selectors
    words = soup.find('ul', class_='d-flex flex-wrap align-items-baseline row').findChildren('span')
    # print the words using Soup's get_text() method
    output_File = open("./word-pages/words-" + a + "-" + str(x) + ".txt", "w")
    for word in words:
        print(word.get_text(), file = output_File)
    output_File.close()
    
i = 0
for letter in alphabet:
    for number in range(1, pageCount[i] + 1):
        scrapeAPage(letter, number)
    i = i + 1 