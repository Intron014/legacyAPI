# The Almighty I014 API
###### By Jorge Benjumea ©2023

- [The Almighty I014 API](#the-almighty-i014-api)
          - [By Jorge Benjumea ©2023](#by-jorge-benjumea-2023)
  - [The API](#the-api)
  - [/modify-clipboard-link](#modify-clipboard-link)
          - [Name still in the works](#name-still-in-the-works)


## The API
This API is something to help me achieve stuff easily with command shortcuts, and it's tailored to my stuff. If you want to use it for something else, go for it! But I doubt you can get use out of it. (Except you, @IbaIBuR. You'll want the ?forcedownload=0 in your life)

## /modify-clipboard-link
###### Name still in the works
Given the Header X-API-Key and the body of the request being a JSON with the following format:
```json
{
  "link": "https://example.com?forcedownload=1",
}
```
It will return a JSON with the following format:
```json
{
  "link": "https://example.com?forcedownload=0",
}
```

Magic! And if the link doesn't have the ?forcedownload=1, it will return an "Invalid Request!", how fun.