import re
import sys
import os 

def main(argv = sys.argv):
	directory = argv[1]
	searches = {}
for kw in argv[2:]:
  searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
 
title_search = re.compile(r'(title:\s*)(?P<title>(.*)[ ]*\n[ ]*(.*))', re.IGNORECASE|re.MULTILINE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

meta_data_search = dict(title_search,author_search,translator_search,illustrator_search)


def meta_search(meta_data_search, full_text):
	results = {}
	for key in meta_data_search:
		result = re.search(meta_data_search[key], full_text)
		if result:
			results[key] = results.group(key)
		else:
			results[key] = None
	return results

def file_path(fl_path):
	with open(fl_path, 'r') as f:
		return f.read()

def file_path_join(directory,fl):
	return os.path.join(directory, fl)

def search_doc_key(kw):
	for kw in sys.argv[2:]:
  		return re.compile(r'\b' + kw + r'\b', re.IGNORECASE)