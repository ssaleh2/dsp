import csv
import string
import re

def read_data(data):
	"""read csv file and return list"""
	faculty = []
  	file = open(data, 'rb')
  	reader = csv.reader(file)
  	faculty = list(reader)
  	return faculty[1:]

def num_diff_degrees(faculty_list):
	"""get different degrees from faculty list and count how many have that degree by going line by line"""
 	diff_degrees = {}
 	for person in faculty_list:
 		person = filter(lambda x: x not in string.punctuation, person[1])
		current_degrees = person.strip().split(' ')
 		for y in current_degrees:
 		 	if y in diff_degrees:
 		 		diff_degrees[y] += 1
 		 	else:
 		 		diff_degrees[y] = 1
 	return diff_degrees

def num_diff_titles(faculty_list):
	"""get different titles from faculty list and count how many have that titles by going line by line"""
	diff_titles = {}
	for person in faculty_list:
 		if person[2] in diff_titles:
			diff_titles[person[2]] += 1
		else:
			diff_titles[person[2]] = 1
 	return diff_titles

def email_list(faculty_list):
	"""create email list from faculty list"""
	emails = []
	for person in faculty_list:
		emails.append(person[3])
	return emails

def num_diff_email_domains(email_list):
	"""get different email domains from faculty list"""
	domains = set()
	for email in email_list:
		index_at = email.find("@")
		domains.add(email[index_at+1:])
	return domains

faculty = read_data('faculty.csv')
print num_diff_degrees(faculty)
print num_diff_titles(faculty)
emails = email_list(faculty)
print emails
print num_diff_email_domains(emails)