t = """ markdown cruft """

def simplify(t):
    images = [i.strip() for i in t.split('|')]

    for img in images:
        attrs = [i.strip() for i in images[0].split("\n")]

        cap_title_list = attrs[0].split(' ')
        title = ''
        for k,word in enumerate(cap_title_list):
            print k,word
            new_title = []
            new_title[k] = word
            if k == 0:
                new_title[k] = word.capitalize()
                continue
            if k not in ('and','the','an'):
                new_title[k] = word.capitalize()
        title = ' '.join(new_title)


        alt = re.search(r'\[(.*?)\]',attrs[1]).group(1)
        img_url, page_url = re.findall(r'\((.*?)\)',attrs[1])
        img_id = attrs[2]
        print title, alt, img_url, page_url, title
