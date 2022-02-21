from asyncio import sleep
from inspect import Parameter
from click import password_option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from parsel import Selector
import csv
import time
import parameter
from textwrap import indent
from googlesearch import search

# name = sel.xpath('//*[starts-with(@class,"text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()
def browose(name):
    query = name + "Owner LinkedIn"

    for j in search(query, tld="co.in",num=2,stop=2,pause=2,verify_ssl=False):
        # url = sel.xpath('//*[starts-with(@class,"iUh30 qLRx3b tjvcx"]/)
        return j
            

# writer = csv.writer(open(parameter.file_name,'wb'))
# writer.writerow(['Name','Job Title','Company','College','Location','URL'])

driver = webdriver.Chrome('/Users/shriyanshvishwakarma/Downloads/chromedriver') 
driver.get('https://www.linkedin.com')

username = driver.find_element_by_id('session_key')
username.send_keys(parameter.linkedin_uername)
time.sleep(0.5)

password = driver.find_element_by_id('session_password')
password.send_keys(parameter.linkedin_password)
time.sleep(0.5)

log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()
time.sleep(0.5)

driver.get('http:www.google.com')
time.sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameter.search_query)
# time.sleep(0.5)

# search_query.send_keys(Keys.RETURN)
# time.sleep(0.5)
# linkedin_urls = driver.find_element_by_name('iuh30')


with open('Sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    feildnames = ['No','Name','Main phone','City','Main email','Website Url','Address','Owner Name' ,'Owner Linkedin' ,'Owner Email' ]
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.DictWriter(new_file,feildnames,delimiter = ',') 
        csv_writer.writeheader()
        for lines in csv_reader:
            Cname = lines["Name"]
            linkedin_urls = browose(Cname)
            driver.get(linkedin_urls)
            time.sleep(5)
            sel = Selector(text = driver.page_source)
            # print(sel)

            name = sel.xpath('//*[starts-with(@class,"text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()
            if name:
                name = name.strip()

            lines["Owner Name"]  = name  
            lines["Owner Linkedin"] = linkedin_urls
            
            csv_writer.writerow(lines)


# linkedin_urls = parameter.search_query

# for linkedin_url in linkedin_urls:


# job_title = sel.xpath('//*[starts-with(@class,"pv-top-card-section__headline")]/text()').extract_first()
# if job_title:
#     job_title = job_title.strip()

linkedin_url = driver.current_url

print('\n')
print('Name: ' + str(name))
# print('Job Title: ' + str(job_title))
# print('Company: ' + company)
# print('College: ' + college)
# print('Location: ' + location)
print('URL: ' + linkedin_url)
print('\n')

driver.quit()