#Practice exercise Ch.3 Data for AI Exercise 2 from The Fundamentals of 
# Artificial Intelligence Volume 1 by Dr. Nisha Talagala and Dr. Sindhu Ghanta

# Import gdown module to download from google drive
import gdown

# url to txt file
url = 'https://drive.google.com/file/d/1HdBNGe8FgwAeHUpMvlshzxxDi7OXqyze/view'

#Derive file id from URL
file_id = url.split('/')[-2]

#download url
download_url = 'http://drive.google.com/uc?id=' + file_id

#save location for downloaded file
file_location = r"about us.txt"

#download file
gdown.download(download_url, file_location, quiet=False)

#open file
with open(file_location, 'r') as file:

        #Read File
        lines = file.readlines()

        #initialize line_count
        line_count=0

        #print each line
        for line in lines:
            line_count += 1
            print(f'line{line_count}: {line}') 