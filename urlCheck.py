import urllib2
import urlparse
import json
import sys
import os

if not os.path.exists('./output'): #If an output folder doesn't currently exist, create
	os.makedirs('./output')

filename = raw_input("\nPlease type the file name of your list of web addresses, eg. test_0.txt (must be in this script's directory):\n")
input = open(os.path.join(sys.path[0], filename));
getInput = input.read().splitlines()
list = []

for line in getInput:
	list.append(line)

print 'Addresses found:'
print list
input.close()
output_code = './output/STATUS_output.json'
status_file = open(output_code,'w')
code_arr = []
enum = 0;

for item in list:
	output = './output/GET_output_'+str(enum)+'.json'
	out_file = open(output,'w')
	x = item.split('://')
	charCheck = urlparse.urlparse(item)

	if x[0]!='http' and x[0]!='https': #Start with check for 'obviously' incorrect addresses that are not appended with 'http' or 'https'
		sys.stderr.write("ERROR: Web address "+item+" timed out after 10 seconds.\n")
		json_dict = {
						'Url': item,
						'Error': 'Invalid URL: Address was not prefixed with \"http\" or \"https\".'
					}
	elif bool(charCheck.scheme)==False: #Parse the URL to identify addresses with incorrect characters or format
		sys.stderr.write("ERROR: Web address "+item+" contains characters or a format invalid for a URL.\n")
		json_dict = {
						'Url': item,
						'Error': 'Invalid URL: Address invalid.'
					}
	else:
		try:
			getUrl = urllib2.urlopen(item, timeout = 10) #Attempt HTTP Get, with timeout of 10 seconds
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
			#ADDITIONAL REQUIREMENT - Status code count
			#########
			if not code_arr:
				code_arr.append({'Status_code': getUrl.getcode(),'Number_of_responses': 1})
			else:
				code_found = False
				for i in code_arr:
					if  i['Status_code'] == getUrl.getcode():
						code_found = True
						temp = i['Number_of_responses']
						i['Number_of_responses'] = temp+1
						break

				if code_found==False:
					code_arr.append({'Status_code': getUrl.getcode(),'Number_of_responses': 1})
			##########
	print json_dict
	json.dump(json_dict,out_file,indent=4)
	enum=enum+1
	print "\nAddress data saved in JSON document: "+output+".\n"	
	out_file.close()

print code_arr
json.dump(code_arr,status_file,indent=4)
print "\nStatus Code count saved in JSON document: "+output_code+".\n"
status_file.close()
