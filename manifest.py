import json
import requests

def getLatestVersion():
    manifestFileUrl = "https://raw.githubusercontent.com/mangofanfan/FanToolsInstaller/master/manifest.json"
    response = requests.get(manifestFileUrl)
    jsonData = json.loads(response.text)

    latestVersion = jsonData["latest"]
    versionUrl = jsonData["version"][latestVersion]
    dataUrl = jsonData["data"][latestVersion]
    return {1: versionUrl, 2: dataUrl, 3: latestVersion}
