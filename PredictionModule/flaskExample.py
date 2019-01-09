import requests, sys, json, jsonify
from flask import Flask
from flask import request

app = Flask(__name__)


def predict(gene):
  return "at4g40080-like protein"

def getEffectsJSON(protein):
    limit = 25

    protein = protein.replace(' ', '%20')

    url = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=" + str(
        protein) + "&limit=" + str(limit) + "&" + "page=1"

    r = requests.get(url, headers={"Accept": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    return json.loads(r.text)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/effects', methods=['POST'])
def effects():
    gene = request.form.get("gene")
    print(gene)

    proteinName = predict(gene)

    results = getEffectsJSON(proteinName)
    effects = []

    for result in results["results"]:
        effect = "\t{\n"
        effect += "\t\t\"goId\": \"" + result["id"] + "\",\n"
        effect += "\t\t\"effect\": \"" + result["name"] + "\"\n"
        #  returnJSON += "\"aspect\": \"" + result["aspect"] + "\",\n"
        effect += "\t}"
        effects.append(effect)

    returnJSON = "[\n" + ",\n".join(effects) + "\n]"

    return returnJSON


app.run(debug=True)