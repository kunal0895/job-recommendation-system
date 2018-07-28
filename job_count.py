import requests
import operator
import matplotlib.pyplot as plt
import collections
import re
from bs4 import BeautifulSoup


def job_count(query, location):
	"""Returns the number of jobs for a query and location on indeed"""
    url = 'https://www.indeed.com/jobs?q={}&l={}&radius=25'.format('+'.join(query.split(
    )), '%2C+'.join(['+'.join(location.split(',')[0].split()), location.split(',')[1].strip()]))
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    pattern = r'\d+,?\d+'
    s = soup.find('div', {'id' : 'searchCount'}).text
    return int(re.search(pattern, s).group().replace(',', ''))

queries = [
    'data engineer',
    'machine learning',
    'data analyst',
    'data scientist',
    'software engineer',
    'web developer',
    'deep learning']	#List of queries

locations = [
    'NYC, NY',
    'Chicago, IL',
    'Philadelphia, PA',
    'Seattle, WA',
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
    'Houston, TX']	#List of locations


# Plotting visualizations for job count for different queries and locations
for query in queries:
    d = dict()
    for location in locations:
        d[location] = job_count(query, location)
    arr = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    cut = min(arr[:10], key = operator.itemgetter(1))[1]
    d = {k : v for k, v in arr if v >=  cut}
    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), [k.split(',')[0] for k in d.keys()], rotation=45)
    plt.title('Top locations for {} jobs in the USA'.format(query))
    plt.savefig(query, bbox_inches='tight')
    plt.clf()
