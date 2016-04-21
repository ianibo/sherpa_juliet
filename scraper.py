# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

#
# # Read in a page
html = scraperwiki.scrape("http://www.sherpa.ac.uk/juliet/index.php?la=en&mode=simple&page=browse")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)

print 'Process'

for row in root.cssselect("table.juliettable tr"):
    td_elements = row.cssselect("td")
    if td_elements is not None:
        if len(td_elements) > 1:
            i_elements = td_elements[0].cssselect("b i")
            if len(i_elements) == 1:
              print "See Row"
            else:
              a_elements = td_elements[0].cssselect("a")
              if len(a_elements) == 2:
                print a_elements[0].attrib["name"], a_elements[1].text, a_elements[1].attrib["href"]
    else:
        print "Missing"

    

#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
