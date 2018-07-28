import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Languages_Tech.csv')  # Reading CSV file

del df['Title']  # Removing useless column
del df['Link']  # One more useless column

# Frequency of a particular language or technology for each query
s = df.groupby('Query').sum()


# Time to plot the data
for index, row in s.iterrows():
    # Only keeping the 10 most common languages/technologies in the
    # visualization. No need to keep the outliers.
    row.nlargest(n=10, keep='first').plot(kind='bar', color='g')
    plt.xlabel('Languages & Technologies')
    plt.ylabel('Frequency')
    plt.xticks(rotation=30)
    plt.title(index.title())
    plt.savefig('{}_frequency'.format(index), bbox_inches='tight')
    plt.clf()
