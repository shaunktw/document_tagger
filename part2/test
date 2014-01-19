import sys
import os
import re
 
# supply path to directory housing PG docs at run time
directory = sys.argv[1]
 
# we're getting the keywords via sys.argv and
# what a dictionary comprhension.
# dictionary comprehensions are a lot like list comprehensions,
# which you've already learned about.
# Dictionary comprehensions have the following form:
#
#   d = {key: value for (key, value) in sequence}
#
# Source: http://stackoverflow.com/a/1747827/1264950
#
kws =  {kw: re.compile(r'\b' + kw + r'\b') for kw in sys.argv[2:]}
 
title_search = re.compile(r'(?:title:\s*)(?P<title>((\S*( )?)+)' + 
                          r'((\n(\ )+)(\S*(\ )?)*)*)', 
                          re.IGNORECASE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
 
for fl in (os.listdir(directory)): 
    if fl.endswith('.txt'):       
        fl_path = os.path.join(directory, fl)
        with open(fl_path, 'r') as f:
            full_text = f.read()
        author = re.search(author_search, full_text)
        if author:
            author = author.group('author')
        translator = re.search(translator_search, full_text)
        if translator:
            translator = translator.group('translator')
        illustrator = re.search(illustrator_search, full_text)
        if illustrator:
            illustrator = illustrator.group('illustrator')
        title = re.search(title_search, full_text).group('title')
        print "***" * 25
        print "Here's the info for {}:".format(fl)
        print "Title:  {}".format(author)
        print "Author(s): {}".format(title)
        print "Translator(s): {}".format(translator)
        print "Illustrator(s): {}".format(illustrator)
        print "\n****KEYWORD REPORT****\n\n"
        for kw in kws:
            print "\"{0}\": {1}".format(kw, len(re.findall(kws[kw], full_text)))
        print '\n\n'