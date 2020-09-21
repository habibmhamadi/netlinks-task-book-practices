# pip3 install bs4
import requests,bs4

def get_latest_jobs():
    """Reads and parses jobs.af homepage and extracts job titles with link
    using beautifulsoup library
    """
    
    res = requests.get('https://www.jobs.af/')
    res.raise_for_status()
    bs = bs4.BeautifulSoup(res.content,'html.parser')
    elems = bs.select('#featured ul li div .media-body .row .col-lg-12 div h2 bdi a')

    for i in elems:
        print('*'*100+'\n')
        print(i.getText()+'\n')
        print('link: https://jobs.af'+i.get('href')+'\n')
        

# get_latest_jobs()