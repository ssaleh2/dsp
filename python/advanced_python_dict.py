import csv

def read_data(data):
	"""read csv file and return list"""
	faculty = []
  	file = open(data, 'rb')
  	reader = csv.reader(file)
  	faculty = list(reader)
  	return faculty[1:]

def dict_q6(faculty_list):
	"""form dictionary with key being last name"""
	dict_last_name = {}
	for person in faculty_list:
		last_name = person[0].rsplit(None,1)[-1]
		if last_name not in dict_last_name:
			dict_last_name[last_name] = person[1:]
		else:
			dict_last_name[last_name].append(person[1:])
	return dict_last_name

def dict_q7(faculty_list):
	"""form dictionary with key being tuple of first and last name"""
	dict_full_name = {}
	for person in faculty_list:
		name_tuple = (person[0].split(None,1)[0], person[0].rsplit(None,1)[-1])
		if name_tuple not in dict_full_name:
			dict_full_name[name_tuple] = person[1:]
		else:
			dict_full_name[name_tuple].append(person[1:])
	return dict_full_name

faculty = read_data('faculty.csv')
print {key:value for key,value in dict_q6(faculty).items()[0:3]}
dict_full_name = dict_q7(faculty)
print {key:value for key,value in dict_full_name.items()[0:3]}

#question 8 - prints out sorted dictionary based on last name
sorted_last_name = sorted(dict_full_name.keys(), key = lambda x:x[-1])
for name in sorted_last_name:
    print name,':',dict_full_name[name]
