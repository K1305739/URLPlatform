# URLValidation
This URL testing and validation program requires Python verson 2.7.14.

1) This program can be run through the Linux command line " python urlCheck.py " from the directory containing 'urlCheck.py'.
	- (Python v2.7 must be correctly installed on your system for the "python" command to be valid.

2) When prompted in the command line, type the name of the text file containing your address list (e.g. " tests_0.txt ").
	- (Your address list must be stored in the directory of the script 'urlCheck.py'.

3) Program will execute and stream results in JSON files to the folder '/output' within 'urlCheck.py's directory.

4) Data on individual web addresses are streamed to files with the 'GET_output_[num].json' naming standard.
	- The list of Status Codes discovered and counted are streamed to the 'output/STATUS_output.json' file.