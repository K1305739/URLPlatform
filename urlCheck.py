import urllib2
import json
import sys
import os

filename = raw_input("Please type the file name of your list of web addresses (must be in this script's directory: ")
input = open(os.path.join(sys.path[0], filename));
getInput = input.read().splitlines()

list = []
for line in getInput:
	list.append(line)
print list

input.close()
output = 'output.json'
out_file = open(output,'w')

for item in list:
	try:
		getUrl = urllib2.urlopen(item, timeout = 10)
	except:
		sys.stderr.write("ERROR: Web address "+item+" timed out after 10 seconds.\n")
		json_dict = {
						'Url': item,
						'Error': 'invalid url'
					}
	else:
		json_dict = {
						'Url': item,
						'Status_code': getUrl.getcode(),
						'Content_length': getUrl.headers.get('content-length'),
						'Date': getUrl.headers.get('date')
					}
	print json_dict
	json.dump(json_dict,out_file,indent=4)
out_file.close()

