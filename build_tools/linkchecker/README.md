UMMMM this doesn't seem to work

use python LinkChecker to verify links

From the repository root, execute:

	linkchecker -f build_tools/linkchecker/linkcheckerrc http://lisas-mbp:8000/saturn/


-v flag will show all links, not just failures

	linkchecker -f build_tools/linkchecker/linkcheckerrc -v http://lisas-mbp:8000/saturn/


haven't tried this but: 

Generate a sitemap graph and convert it with the graphviz dot utility: 

	linkchecker -f build_tools/linkchecker/linkcheckerrc -odot -v http://lisas-mbp:8000/saturn/ | dot -Tps > sitemap.ps
