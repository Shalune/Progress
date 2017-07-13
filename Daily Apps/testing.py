from lxml.html import fromstring
import requests

webAddress = 'https://www.washingtonpost.com/politics/state-department-spent-more-than-15000-for-rooms-at-new-trump-hotel-in-vancouver/2017/07/12/5eba5d0c-61bf-11e7-84a1-a26b75ad39fe_story.html?utm_term=.27750d03c07e'

title = fromstring(requests.get(webAddress).content).findtext('.//title')

print(title)