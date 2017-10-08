import urllib2
import urlparse
import json
import sys
import os

filename = raw_input("Please type the file name of your list of web addresses (must be in this script's directory: ")
input = open(os.path.join(sys.path[0], filename));
getInput = input.read().splitlines()

list = []
for line in getInput:
	list.append(line)

print 'Addresses found:'	
print list

input.close()
output = 'output.json'
out_file = open(output,'w')

for item in list:
	x = item.split('://')
	charCheck = urlparse.urlparse(item)
	
	if x[0]!='http' and x[0]!='https':
		sys.stderr.write("ERROR: Web address "+item+" timed out after 10 seconds.\n")
		json_dict = {
					'Url': item,
					'Error': 'Invalid URL: Address was not prefixed with \"http\" or \"https\".'
				}
	elif bool(charCheck.scheme)==False:
		sys.stderr.write("ERROR: Web address "+item+" contains character invalid for a URL.\n")
		json_dict = {
					'Url': item,
					'Error': 'Invalid URL: Address contains invalid characters.'
				}
	else:
		try:
			getUrl = urllib2.urlopen(item, timeout = 10)
		except:
			sys.stderr.write("ERROR: Web address "+item+" timed out after 10 seconds.\n")
			json_dict = {
							'Url': item,
							'Error': 'HTTP GET timed out after 10 seconds.'
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

print '\nOutput saved in JSON document '+output+'.'	
out_file.close()

