Directory/workflow information:

./Content - each file contains the text extracted from a unique job posting on indeed.
./Results - contains graphs generated from analyzing the data.
./Resumes - Contains sample resumes. A user can put his resume in this directory and run predict.py to know which domain he is suitable for.
./Common data.csv - Contains link, job title, location and search query for 42,000+ jobs on indeed.
./graphs.py - Generates graphs for the popular languages/technologies used in each domain.
./job_count.py - Generates graphs for which major cities in USA are hubs for different domains.
./Languages_Tech.csv - Contains data of different languages and technologies for several thousands of jobs on indeed.
./New.csv - Langueges_Tech.csv after cleansing required for prediction. Used as input in prediction.py
./predict.py - Predicts which domain is more suitable for each resume in ./Resumes using SVM classifier with Languages_Tech.csv dataset as training dataset.
./Programming_languages.csv - Contains data of different programming languages for several thousands of jobs on indeed.
./scraping.py - Program to scrap job links on indeed. Output is stored to ./Common data.csv
./scraping_sublinks.py - Scraps every link in ./Common data.csv and extracts important keywords for programming languages and technologies. Output is stored in ./Programming_languages.csv and ./Technologies.csv
./Technologies.csv - Contains data of different technologies for several thousands of jobs on indeed.
