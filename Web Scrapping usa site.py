from bs4 import BeautifulSoup as bs
import requests
import time
print('Enter a skill in small letter,\nwhich is not compitable to you')
excluded=input('>>> ')
print('Removing your unfamilliars...')
def job_searching():
    html_text=requests.get('https://www.flexjobs.com/search').text
    soup=bs(html_text,'lxml')
    job=soup.find_all('li',class_='m-0 row job')
    for index,jobs in enumerate(job):
        post_time=jobs.find('div',class_='job-age').text.replace(' ','').replace('!','').lower()
        if 'new' in post_time:
            job_title_lower=jobs.find('a',class_='job-title job-link').text.lower()
            if excluded not in job_title_lower:
                job_title=jobs.find('a',class_='job-title job-link').text
                country_name=jobs.find('div',class_='col pe-0 job-locations text-truncate').text.strip()
                job_tag=jobs.find('div',class_='col-sm-auto pe-sm-0 job-tags').text.strip().replace('\n',',')
                job_description=jobs.div.a['href']
                with open(f'Flex Job Text/{index}.txt','w') as txt:
                    txt.write(f'Job Heading: {job_title}\n')
                    txt.write(f'Country: {country_name}\n')
                    txt.write(f'Tags: {job_tag}\n')
                    txt.write(f'Job Details Link: {job_description}')
                print(f'File Saved: {index}')

if __name__=='__main__':
    while True:
        job_searching()
        waiting_time= 5
        print(f'Programme runs after {waiting_time} minuites...')
        time.sleep(waiting_time*50)