import requests
import csv
from nltk import word_tokenize
from bs4 import BeautifulSoup

present_links = set()


def scrap_links(base_url, page_count, location, search_term):
    """Adds page count to base_url and scraps all the job links from the page"""
    base_url += '&start={}'.format(page_count)
    key_words = [
        'data',
        'science',
        'analyst',
        'developer',
        'research',
        'engineer',
        'stat',
        'machine',
        'learning',
        'web',
        'software',
        'deep',
        'analytics',
        'scientist']
    r = requests.get(base_url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    for x in soup.findAll('a'):
        try:
            if x['href'] not in present_links and any(w in key_words for w in word_tokenize(
                    x.text.lower())) and 'clk' in x['href']:  # Checking whether the link is usable or not
                yield ['https://www.indeed.com/{}'.format(x['href']), x.text, location, search_term]
                present_links.add(x['href'])
        except Exception:
            pass


def create_url(query, location):
    return 'https://www.indeed.com/jobs?q={}&l={}'.format('+'.join(query.split()), '%2C+'.join(
        ['+'.join(location.split(',')[0].split()), location.split(',')[1].strip()]))


queries = [
    'data engineer',
    'machine learning',
    'data analyst',
    'data scientist',
    'software engineer',
    'web developer',
    'deep learning']

locations = [
    'NYC, NY',
    'Seattle, WA',
    'Philadelphia, PA',
    'Chicago, IL',
    'San Jose, CA',
    'Raleigh, NC',
    'Portland, OR',
    'San Francisco, CA',
    'St. Louis, MO',
    'Denver, CO',
    'Austin, TX',
    'Boston, MA',
    'Sacramento, CA',
    'Atlanta, GA',
    'Dallas, TX',
    'Phoenix, AZ',
    'Salt Lake City, UT',
    'San Antonio, TX',
    'Charlotte, NC',
    'San Diego, CA',
    'Pittsburgh, PA',
    'Houston, TX']

# To store combined data for all the locations
common_data = [['Link', 'Title', 'Location', 'Search query']]

for query in queries:
    for location in locations:
        for i in range(1, 51):
            common_data += scrap_links(create_url(query,
                                                  location), i, location, query)
            print(location, query, i)

# Writing combined data to CSV
with open('Common data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(common_data)
