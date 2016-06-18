import csv

def email_list(data):
	"""read csv file and return email list"""
	faculty = []
  	file = open(data, 'rb')
  	reader = csv.reader(file)
  	faculty = list(reader)[1:]
  	emails = [i[3] for i in faculty]
  	return emails

def email_write_csv(email_list):
	"""write emails out to csv file"""
	with open('email.csv', 'wrb') as file:
		writer = csv.writer(file)
		for i in email_list:
			writer.writerow([i])

emails = email_list('faculty.csv')
email_write_csv(emails)
