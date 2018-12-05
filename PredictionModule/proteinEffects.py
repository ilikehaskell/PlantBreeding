#Get a json which contains all efects for a specific protein name
# proteinName is the name of the protein and limit is the limit of effects that will be in JSON
#you should use python 3 to run this

import requests, sys, json

proteinName = "GO:0000001"
limit = 5


proteinName = proteinName.replace(' ', '%20')

requestURL = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=" + str(proteinName) + "&limit=" + str(limit) + "&" + "page=1";

print(requestURL)

r = requests.get(requestURL, headers={ "Accept" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()

responseBody = r.text
parsed = json.loads(responseBody)

for result in parsed["results"]:
  print("Id: " + result["id"])
  print("- Aspect: " + result["aspect"])
  print("- Name: " + result["name"] + "\n")
#  print("- Definition" + result["definition"]["text"])
