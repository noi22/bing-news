import requests
import lxml.html
import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#set keyfile name 
service_account_keyfile = 'editspreadsheet.json' 

#setting credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_keyfile, scope)

# login to Google API by OAuth2 credentials 
gc = gspread.authorize(credentials)

#setting spreadsheet_key
SPREADSHEET_KEY = '1eczkYDtVv8Xac-WbtgcGl0DADykQECrsPAYKQXzW9JE'

#open sheet1
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#get response from bing.com 
response = requests.get('https://www.bing.com/news')

# get html
root = lxml.html.fromstring(response.content.decode('utf-8'))
root.make_links_absolute(response.url)

#get a list of <a> tag 
elems = root.cssselect('#mainfeed  div > div > div.caption > div.t_s > div.t_t > a')

# get url and title from each <a> tag
i = 3
for elem in elems:
  if (i > 22 ):
      break   
  url = elem.get('href')
  title = elem.text
  worksheet.update_cell(i,3, title)
  worksheet.update_cell(i,4, url)
  i += 1


