import re
import sys
import os 


title_search = re.compile(r'(title:\s*)(?P<title>(.*)[ ]*\n[ ]*(.*))', re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

metadata_search = dict(author=author_search,
                    title=title_search,
                    translator=translator_search,
                    illustrator=illustrator_search,
                    )

def meta_search(metadata_search, full_text):
	results = {}
	for key in metadata_search:
		result = re.search(metadata_search[key], full_text)
		if result:
			results[key] = result.group(key)
		else:
			results[key] = None
	return results

def file_path_join(directory, file_name):
	return os.path.join(directory, file_name)

def file_path_opener(fl_path):
	with open(fl_path, 'r') as f:
		return f.read()

def key_word_search(kws):
	result = {kw: re.compile(r'\b' + kw + r'\b') for kw in kws}
	return result

def find_all_search(search, full_text):
	match = re.findall(search, full_text)
	return len(match)

def doc_tag_reporter(directory, search):
	for fl in os.listdir(directory):
		if fl.endswith('.txt'):
			fl_path = file_path_join(directory, fl)
			text = file_path_opener(fl_path)
			meta_searches = meta_search(metadata_search, text)
			keyword = key_word_search(search)
			print "Here's the info for doc {}:".format(fl)
	       	for k in meta_searches:
	       		print "{0}: {1} ".format(k.capitalize(), meta_searches[k])
	        print "*****KEY WORD REPORT*****"
	        for search in keyword:
	        	print "\"{0}\": {1}".format(search, find_all_search(keyword[search],text))
	        print '\n\n'
	        print "***" * 25 

def main():
	directory = sys.argv[1]
	search = [i for i in sys.argv [2:]]
	doc_tag_reporter(directory,search)

if __name__ == '__main__':
    main()

