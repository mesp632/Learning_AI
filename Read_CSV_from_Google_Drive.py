#Practice exercise Ch.3 Data for AI Exercise 1 from The Fundamentals of 
# Artificial Intelligence Volume 1 by Dr. Nisha Talagala and Dr. Sindhu Ghanta

#import pandas module to read the CSV file
import pandas as pd

#import gdown module to download fields from google drive
import gdown

url="https://drive.google.com/file/d/1sQGqysf7HFPngnKgumOlzSmyI0CHgGkF/view"

#Derive the file id from the url
file_id = url.split('/')[-2]

#Derive the download url of the file
download_url = 'https://drive.google.com/uc?id=' + file_id

#save the file name
file_name = "child_vs_adult.csv"

#Derive file location
file_location = file_name

#Download the file from drive
gdown.download(download_url, file_location, quiet=False)

#Read CSV File
data = pd.read_csv(file_location)

#Print a sample (first row) from the tabular data
print('---- The first row from the data set ----')
print(data.head(1))

#See the column names in the table
column_names = data.columns
print('---- Column Names in Table ----')
for column in column_names:
    print(column)

#change the column name
column_name = "height"

#Print specific column
print('---- Data from Column ----')
column = data[[column_name]]
print(column)