import re
import sys
import os 


directory = sys.argv[1]
# PREPARE OUR REGEXES FOR METADATA SEARCHES #
# we'll use re.compile() here, which allows you to assign a regex pattern
# to a variable. We'll do this for each our metadata fields.
# 
# Also note how we're using paretheses to create two search groups. Looking
# at title_search, see how we use one group to match on the presence of "title:".
# 
# Also, note how in the second group is a named group -- we use ?p<name> .
# 
# Finally, note that we're passing the re.IGNORECASE flag as an optional
# argument to re.compile. We're doing this because it's human beings who create
# the metadata headers at the top of Project gutenberg docs, and we want to account 
# for possibility of "title: Some Title", "Title: Some Title", and "TITLE: Some Title").
searches = {}
for kw in sys.argv[2:]:
  searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
 

title_search = re.compile(r'(title:\s*)(?P<title>(.*)[ ]*\n[ ]*(.*))', re.IGNORECASE|re.MULTILINE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# now iterate over the documents and extract and print output about metadata
# for each one. Note the use of enumerate here, which gives you a counter variable
# (in this case 'i') that keeps track of the index of the list (in this case documents)
# your currently on in your loop. You should memorize how enumerate works, and google it
# if you need more explanation. It's a highly productive built in function, and there are
# common problems that you'll encounter as a programmer that enumerate is great for.
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
        print "Here's the info for doc {}:".format(fl)
        print "Title:  {}".format(title)
        print "Author(s): {}".format(author)
        print "Translator(s): {}".format(translator)
        print "Illustrator(s): {}".format(illustrator)
        print "\n"
        print "*****KEY WORD REPORT*****"
        for search in searches:
            print "\"{0}\": {1}".format(search, len(re.findall(searches[search], full_text)))
        print '\n\n'