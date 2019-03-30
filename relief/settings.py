import json

settingsFile = 'relief/config.json'
configDefaultSettings = {
    "filenamePrefix": "relief",
    "trafficLightDefault": "AMBER",
    "dataMarkingFooter": "For Internal Use Only",
    "presentationAuthor": "",
    "presentationCategory": "High-level Threat Report Presentation",
    "presentationTitle": "relief",
    "presentationSubject": "Executive report of a cyber security threat event",
    "presentationKeywords": "threat intel report"
}

def write_default_settings():
    with open(settingsFile, 'w') as configFile:
        try:
            json.dump(configDefaultSettings, configFile)
        except:
            return False
        else:
            return True

def read_settings():
    with open(settingsFile, 'r') as configFile:
        cs = json.load(configFile)
    #for k in cs:
    #    print(k, "   ::   ", cs[k])
    return cs

def write_settings():
    with open(settingsFile, 'w') as configFile:
        json.dump(newConfigSettings, configFile)
