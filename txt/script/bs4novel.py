

from bs4 import BeautifulSoup
fnm = '人欲.html'
prs = 'html.parser'
prs = 'lxml'
with open(fnm, encoding='u8') as fin:
	soup = BeautifulSoup(fin, prs)
