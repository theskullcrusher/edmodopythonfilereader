# EdmodoPythonReader
This is a project for a Python log file reader 

Assumptions Made:

1. Default encoding used is utf-8.
2. The date-time string is assumed to have the format YYYY-MM-DD:hh:mm:ss
   since example did not convey if it was YYYY-MM-DD or YYYY-DD-MM.
   If input date-time is in another format, it will invalidate the record. 
   To change the default format if needed, change it in the DATE_TIME_FORMAT 
   variable at the top of the utils.py file.
3. The double quotes used in the example are the LEFT_DOUBLE_QUOTE = '“' and
   RIGHT_DOUBLE_QUOTE = '”' which (in utf-8 encoding) are different than the
   DOUBLE_QUOTE = '"'. I've assumed that the double quotes used in the example
   are valid and designed by regex around it. If testing on DOUBLE_QUOTE = '"'
   is needed to, please let me know and I'll quickly push a parallel version
4. For ID, positive integers are allowed, I've considered the whole number
   series (0,1,2...) to be valid. 
5. If the quotation marks are not balanced, it will be considered an invalid input
   in all except one case.
6. The one case where I try to validate the input is if there are multiple LEFT_DOUBLE_QUOTE
   for a single RIGHT_DOUBLE_QUOTE. Here all inner LEFT_DOUBLE_QUOTEs will be ignored
   and considered a part of the string.
7. I've used pep8 standards in the project along with pylint to generate a score between -10 to 10
   for all my python files, which gives me a 9+/10 in each one.


Instructions to run the package:

1. The root folder of this package/project is what needs to be used to execute
   all the commands.
2. run_app.py is the entry point into the system, and it can be run as follows:
   python python_file_reader/run_app.py -f data_logs.txt
3. The above command will run on the sample input file in the python_file_reader/
   log_files directory. Please put your input file sample in the same log_files directory
   and mention the file name (without the entire path). Also note that if no filename
   is specified, all files inside the log_files directory will be used.