import sys
import os
import re
 
title_ptn = re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + 
                          r'((\n(\ )+)(\S*(\ )?)*)*)', 
                          re.IGNORECASE)
author_ptn = re.compile(r'(author:)(?P<author>.*)', 
    re.IGNORECASE)
translator_ptn = re.compile(r'(translator:)(?P<translator>.*)', 
    re.IGNORECASE)
illustrator_ptn = re.compile(r'(illustrator:)(?P<illustrator>.*)', 
    re.IGNORECASE)
 
meta_search_dict = dict(author=author_ptn,
                    title=title_ptn,
                    translator=translator_ptn,
                    illustrator=illustrator_ptn,
                    )
 
def meta_search(meta_search_dict, text):
    """Returns results of search for metadata from text"""
    results = {}
    for k in meta_search_dict:
        result = re.search(meta_search_dict[k], text)
        if result:
            results[k] = result.group(k)
        else:
            results[k] = None
    return results
 
 
def file_opener(fl_path):
    """Given a full path to a file, opens that file and returns its contents"""
    with open(fl_path, 'r') as f:
        return f.read()
 
def file_path_maker(directory, fl_name):
    return os.path.join(directory, fl_name)
 
def kw_pattern_maker(kws):
    """Returns ditionary of keyword regular expression patterns"""
    result = {kw: re.compile(r'\b' + kw + r'\b') for kw in kws}
    return result
 
def kw_counter(pattern, text):
    """Returns the number of matches for a keyword in a given text"""
    matches = re.findall(pattern, text)
    return len(matches)
 
def doc_tag_reporter(directory, kws):
    """
    Iterates over a directory of Project Gutenberg documents
    and gives info on title, author, illustrator, translator and count of 
    user supplied keywords.
    """
    for fl in os.listdir(directory):
        if fl.endswith('.txt'):
            fl_path = file_path_maker(directory, fl)
            text = file_opener(fl_path)
            meta_searches = meta_search(meta_search_dict, text)
            kw_searches = kw_pattern_maker(kws)
            print "Here's the info for {}:".format(fl)
            for k in meta_searches:
                print "{0}: {1}".format(k.capitalize(), meta_searches[k])
            print "\n****KEYWORD REPORT****\n\n"
            for kw in kw_searches:
                print "\"{0}\": {1}".format(kw, kw_counter(kw_searches[kw], text))
            print '\n\n'
            print "***" * 25
 
def main():
    directory = sys.argv[1]
    kws = [i for i in sys.argv[2:]]
    doc_tag_reporter(directory, kws)
 
if __name__ == '__main__':
    main()