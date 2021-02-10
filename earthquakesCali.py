# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def caliCheck(data):
  theJSON = json.loads(data)
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  for i in theJSON["features"]:
    loc = i["properties"]["place"]
    if "CA" in loc:
      print("%2.1f" % i["properties"]["mag"], loc)
    
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    caliCheck(data)
  else:
    print("received error, cannot parse results")
  

if __name__ == "__main__":
  main()
