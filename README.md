# insight_de_cc
September 2020 Insight Data Engineering Coding Challenge application

To run the file simply run the shell script "run.sh" with a "complaints.csv" file in the main "input" directory.  Upon running the file a timer is started to compare speeds against prvious attempts.

If the csv has a header the header must contain the following case sensitive strings. (Date recieved, Product, Company) These strings are used to define the column numbers for the future lists.  If a header is detected without those strings an error message will be printed.  If no header is detected default column numbers will be used.  After the date column is defined the code searches for and confirms that the date format is YYYY-MM-DD for use with the date time function. If the dates are in a diffrent format an error is printed telling the user to adjust the format.

After the input csv file has been loaded into 3 lists a dictionary is defined.  This dictionary contains two sub dictionarys and a list.  This allowed me to "sort" through the data similar to excel.

Once the data has been sorted and counted from the master dctionary 5 lists were created and zipped(to remove zero rows(duplicates)) the final data was printed to a new csv file (report.csv) in the output folder.

I believe this logic can be condensed furthe so that the code doesn't have to step through every value numerous times. It would be for a future release as it is functional(although slow) now.
