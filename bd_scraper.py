#!/usr/bin/python

import os
from bs4 import BeautifulSoup
import urllib2

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

os.system('clear')
url = 'https://backdoor.sdslabs.co/users/'
username = raw_input(bcolors.OKBLUE + 'Enter the username: ' + bcolors.ENDC)

response = urllib2.urlopen(url + username)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

problem_count = 0
for link in soup.find_all('a'):
	if '/challenges/' in link.get('href'):
		problem_count = problem_count + 1

print bcolors.OKBLUE + '\nProblems Solved: ' + bcolors.ENDC + str(problem_count)

for text in soup.strings:
	if 'Score: ' in text:
		print bcolors.OKGREEN + text + bcolors.ENDC
	if 'Rank: ' in text:
		print bcolors.OKGREEN + text + bcolors.ENDC

print bcolors.OKBLUE + '\nNames of all problems: ' + bcolors.ENDC

for link in soup.find_all('a'):
	if '/challenges/' in link.get('href'):
		challenge_url = link.get('href')
		print bcolors.WARNING + '- ' + challenge_url[12:] + bcolors.ENDC