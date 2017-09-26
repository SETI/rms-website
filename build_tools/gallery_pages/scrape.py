import re
"""
    script to scrape the image gallery data from the converted markdown
    versions of the old gallery pages

"""

path = '../../website/saturn/cassini'
f = path + '/index.html'
# f = path + '/2011-11.html'

with open(f, "rb") as myfile:
     page = "".join(myfile.readlines()[1:])

page = page.split('* * *')[0]  # trim the footer
page = ''.join(page.split('---')[2:])
page = page.replace("\n"," ")
data = [d for d in page.split('|') if d]  # list comprehension removes empty lines

for d in data:
    """
        d has this:
             May 2015 [ ![May 2015: Serene Saturn](http://photojournal.jpl.nasa.gov/thumb/PIA18314.jpg)](2015-05.html)

         want this:

          - title: Main Ring of Jupter
            href: ./PIA00538.html
            src: PIA00538-med.jpg
            caption: Image of the Main Ring of Jupiter taken through clear filter.

    """
    if not d.strip(): continue

    title = re.findall(r'\[[^()]*\]', d)[0].strip('[ ![').strip(']')
    href = re.findall(r'\([^()]*\)', d)[1].strip('(').strip(')')  # 2015-05.html
    src = re.findall(r'\([^()]*\)', d)[0].strip('(').strip(')')

    caption = title

    print """
            title: {}
            href: {}
            src: {}
            caption: {}
        """.format(title,href,src,caption)
