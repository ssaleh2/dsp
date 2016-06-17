# -*- coding: utf-8 -*-
#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):
	EPL = []
  	file = open(data, 'rb')
  	reader = csv.reader(file)
  	EPL = list(reader)
  	return EPL[1:]

def get_min_score_difference(parsed_data):
	min_diff = 100000
	team = 0
	for x in parsed_data:
		if abs(int(x[5]) - int(x[6])) < min_diff:
			min_diff = abs(int(x[5]) - int(x[6]))
			team = parsed_data.index(x)
	return team

def get_team(index_value, parsed_data):
    return parsed_data[index_value][0]

EPL = read_data('football.csv') 
print "Team with smallest difference in goals was: " + get_team(get_min_score_difference(EPL),EPL)