import requests
from bs4 import BeautifulSoup
import csv
print("\n\n\t\t\t\t\t\t\t\t\tWelcome to Grade Finder",)
rollno = input("Enter roll number: ")
url = requests.get('https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno=' + rollno)
soup_data = BeautifulSoup(url.text)
print("\n")
mylist = soup_data.find_all('tr',{"bgcolor":"#FFF3FF"})
for data in mylist:
	td_item=data.find_all('td') 
	if len(td_item[0].text)==7:  
		print("Subject: {}    Grade: {}".format(td_item[1].text,td_item[4].text))
	