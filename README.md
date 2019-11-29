This was created during my time as a student at Code Chrysalis.

# bing-news

This app scrapes the [Japanese bing news page](https://www.bing.com/news) and gets the latest 20 sets of title and URL of each news. The results are written to google spread sheets.


## How it looks

![gif](/bing-news.gif)

## How to set

- Enable Google Drive API and Google Sheets API
- Generate a credential and put the JSON file to the root directory. set the filename to variable  `service_account_keyfile`
- Create a googlesheet and set the key to variable `SPREADSHEET_KEY`
- Share the googlesheet with the email in the JSON file

## How to run

```
python getbingnews.py
```
