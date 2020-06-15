import csv

def get_cs_words(tr_words, cs_words):
	l = []
	for t in tr_words:
		if t in cs_words:
			l.append(a)
	return l

# removing all special characters except spaces
def rem_spc_char(s):
    s = s.lower()
    return ''.join(e for e in s if e.isalnum() or e == ' ')

# reading a transcript file
def read_file(file):
    f = open(file)
    s = f.read().replace("\n", " ")
    f.close()
    return s


transcript_words = read_file("transcript.txt")
transcript_words = rem_spc_char(transcript_words)
cs_words = read_file("tech_words.txt")
dictionary = dict()
transcript_words = transcript_words.split(" ")
cs_words = cs_words.split(" ")
words = get_cs_words(transcript_words, cs_words)

# computing the word count
for i in words:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

# sorting dictionary based on values
dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}

# writing into a csv file
with open('test.csv', 'w') as f:
    for key in dictionary.keys():
        f.write("%s,%s\n"%(key,dictionary[key]))

