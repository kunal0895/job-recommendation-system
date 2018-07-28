import requests
import pandas as pd
import signal
from collections import defaultdict
from bs4 import BeautifulSoup
from nltk import word_tokenize


def handler(signum, frame):
    """This is to stop scraping a specific page when it's taking too long"""
    print('Forever is over')
    raise Exception('End of time')


def is_included(content, words):
	"""Returns 1s and 0s based on whether words are included in content or not"""
    return [int(w in word_tokenize(content)) for w in words]


def find_content(link):
    """To extract textual data and remove tags from the page"""
    try:
        r = requests.get(link)
        data = r.text
        soup = BeautifulSoup(data, 'lxml')
        for script in soup(['script', 'style']):
            script.extract()
        return soup.get_text().lower()
    except Exception:
        return ''


programming_languages = [
    'python',
    'html',
    'css',
    'ajax',
    'php',
    'r',
    'scala',
    'java',
    'javascript',
    'c++',
    'matlab',
    'haskell',
    'ruby',
    'sas',
    'perl',
    'c#',
    'sql',
    'julia',
    'lua',
    'octave']  # List of programming languages

technologies = [
    'django',
    'laravel',
    'rails',
    'hadoop',
    'asp.net',
    'spark',
    'aws',
    'mongodb',
    'tensorflow',
    'numpy',
    'pandas',
    'mvc',
    'angular',
    'node',
    'hive',
    'pig',
    'react',
    'jquery',
    'mysql',
    'linux',
    'postgresql',
    'hbase',
    'cassandra',
    'nltk']  # List of technologies

# To store data about programming language and technology requirement
data_pl, data_tech = defaultdict(list), defaultdict(list)

# Reading the previously scrapped data about data science jobs
df = pd.read_csv('Common data.csv')
c = 0

for link, title in zip(list(df['Link']), list(
        df['Title'])):  # This is where the scraping happens
    # To stop scraping a particular page if it's taking too long
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(10)
    try:
        content = find_content(link)
        is_included_pl = is_included(content, programming_languages)
        is_included_tech = is_included(content, technologies)
        if not any(is_included_pl) and not any(is_included_tech):
            raise Exception()
        for x, y in zip(programming_languages, is_included_pl):
            if x == 'c#':
                y = 'c#' in content
            data_pl[x].append(y)
        for x, y in zip(technologies, is_included_tech):
            if x == 'asp.net':
                y = 'asp.net' in content
            data_tech[x].append(y)
        data_tech['Title'].append(title)
        data_pl['Title'].append(title)
        data_pl['Link'].append(link)
        data_tech['Link'].append(link)
        with open('./Content/{}.txt'.format(c), 'w') as f:
            f.write(content)
        c += 1
        print(c, title)
        if c % 100 == 0:
            df1 = pd.DataFrame(data_pl)  # Converting data to dataframe
            df2 = pd.DataFrame(data_tech)  # Converting data to dataframe
            df1.to_csv(
                'Programming_languages.csv',
                index=False)  # Saving dataframe to CSV
            # Saving dataframe to CSV
            df2.to_csv('Technologies.csv', index=False)
    except Exception:
        pass

df1 = pd.DataFrame(data_pl)  # Converting data to dataframe
df2 = pd.DataFrame(data_tech)  # Converting data to dataframe

df1.to_csv('Programming_languages.csv', index=False)  # Saving dataframe to CSV
df2.to_csv('Technologies.csv', index=False)  # Saving dataframe to CSV
