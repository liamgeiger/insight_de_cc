# insight_de_cc
September 2020 Insight Data Engineering Coding Challenge application

To run the file simply run the shell script "run.sh" with a "complaints.csv" file in the main "input" directory.  Upon running the file a timer is started to compare speeds against previous attempts.

If the csv has a header the header must contain the following case sensitive strings. (Date received, Product, Company) These strings are used to define the column numbers for the future lists.  If a header is detected without those strings an error message will be printed.  If no header is detected default column numbers will be used.  After the date column is defined the code searches for and confirms that the date format is YYYY-MM-DD for use with the date time function. If the dates are in a different format an error is printed telling the user to adjust the format.

After the input csv file has been loaded into 3 lists a dictionary is defined.  This dictionary contains two sub dictionaries and a list.  This allowed me to "sort" through the data similar to excel.

Once the data has been sorted and counted from the master dictionary 5 lists were created and zipped (to remove zero rows (duplicates)) the final data was printed to a new csv file (report.csv) in the output folder.

To perform tests I wrote a simple script that would compare two .csv files line by line and print out if a line was different.  To build my own test I used a combination of excel on a dedicated input file and pen and paper to create my own report_answer to check my codes output against as well as utilizing the provided test.
I believe this logic can be condensed further so that the code doesn't have to step through every value numerous times. It would be for a future release as it is functional (although slow) now.
