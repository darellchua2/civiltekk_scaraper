import requests
import bs4 as bs


def find_all_tables(soup):
    ### find all the tables in the website
    tables = soup.find_all('table')
    print("No of Tables:", len(tables))

    for i in range(0, len(tables)):
        print(tables[i])
        print("-----------------------------")


def look_for_one_specific_table(soup):
    ### lets look into a specific table now
    table = soup.find('table', {"class": "wikitable sortable card-list set-list__main"})
    print(table)


def look_for_one_specific_table_and_find_individual_attributes_inside_the_table(soup):
    ### lets look into a specific table now
    table = soup.find('table', {"class": "wikitable sortable card-list set-list__main"})
    print(table)
    tds = table.find_all('td')
    for i in range(0, len(tds)):
        print("td:", tds[i])
        td = tds[i]
        print("td's text:", td.text)
        print("\n")
        a_s = td.find_all('a')
        for j in range(0, len(a_s)):
            a = a_s[j]
            if a is not None:
                print("a" + "[" + str(j) + "]" + ": ", a)
                print("a's text:", a.text)
                if a["href"] is not None:
                    print("a" + "[" + str(j) + "]" + "'s href: ", a["href"])
                if a["title"] is not None:
                    print("a" + "[" + str(j) + "]" + "'s title: ", a["title"])
            print("\n")
        print("--------------")


## 1. Set the URl that you want to scrape from, might not work if the website is using some front end framework such as React
URL = "https://yugipedia.com/wiki/History_Archive_Collection"

## 2. Calls the URL and store it in memory
response = requests.get(URL)
source = response.text

### Prints the response of your request, [200] refers to success
## You can visit https://developer.mozilla.org/en-US/docs/Web/HTTP/Status to see the meaning of each response
# print(response) ## 200 means OK

### print out text file of your response
# print(source)

### converts source text into a "soup"
soup = bs.BeautifulSoup(source, 'html.parser')

# find_all_tables(soup) ## find all tables
# look_for_one_specific_table(soup) ## find 1 table
look_for_one_specific_table_and_find_individual_attributes_inside_the_table(soup)

### For more information on the beautiful soup library, you can go to https://www.crummy.com/software/BeautifulSoup/bs4/doc/
