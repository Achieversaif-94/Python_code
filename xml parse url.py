import urllib.request
import xml.etree.ElementTree as ET

url = "https://feeds.bbci.co.uk/news/rss.xml"

with urllib.request.urlopen(url) as response:
    xml_data = response.read()

root = ET.fromstring(xml_data)
channel = root.find('channel')

print("Feed Title:", channel.find('title').text)
print()

for item in channel.findall('item')[:5]:
    title = item.find('title').text
    link  = item.find('link').text
    print("Headline:", title)
    print("Link    :", link)
    print()