import os

loksabha = '''First	May 1952
Second	April 1957
Third	April 1962
Fourth	March 1967
Fifth	March 1971
Sixth	March 1977
Seventh	January 1980
Eighth	December 1984
Ninth	December 1989
Tenth	June 1991
Eleventh	May 1996
Twelfth	March 1998
Thirteenth	October 1999
Fourteenth	May 2004
Fifteenth	May 2009
Sixteenth 	May 2014'''

def make_folders():
    for row in loksabha.split('\n'):
        label, month, year = row.split()
        path = os.path.join(os.path.dirname(__file__), 'data', label.lower())
        os.makedirs(path)
        with open(os.path.join(path, 'config.json'), 'w') as f:
            f.write('{ "label": "%s", "from": "%s" }' % (label, month + ' ' + year))

if __name__ == '__main__':
    make_folders()