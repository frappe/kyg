import os

loksabha = '''1st Lok Sabha	May 1952
2nd Lok Sabha	April 1957
3rd Lok Sabha	April 1962
4th Lok Sabha	March 1967
5th Lok Sabha	March 1971
6th Lok Sabha	March 1977
7th Lok Sabha	January 1980
8th Lok Sabha	December 1984
9th Lok Sabha	December 1989
10th Lok Sabha	June 1991
11th Lok Sabha	May 1996
12th Lok Sabha	March 1998
13th Lok Sabha	October 1999
14th Lok Sabha	May 2004
15th Lok Sabha	May 2009
16th Lok Sabha 	May 2014'''

def make_folders():
	for row in loksabha.split('\n'):
		label, month_year = row.split('\t')
		path = os.path.join(os.path.dirname(__file__), 'data', label)
		os.makedirs(path)
		with open(os.path.join(path, 'config.json'), 'w') as f:
			f.write('{ "label": "%s", "from": "%s", "wikipedia_page_id": "%s"}' % (label, month_year, label.replace(' ', '_')))

if __name__ == '__main__':
	make_folders()