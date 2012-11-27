import re
import nltk.data

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

sab = open('short_abstracts_en.ttl','r')

sab.readline()
#line = ab.readline()
for line in sab:
	m = re.search(r'(resource\/)(.*)(> <)',line)
	if m:
		title = m.group(2)
		print "["+title+"]"
		m1 = re.search(r'(> ")(.*)("@en \.)',line)
		if m1:
			#print m1.group(2)
			text = m1.group(2)
			#print text.split(". ")
			sentences = sent_detector.tokenize(text.strip())
			
			for s in sentences:
				print s
			