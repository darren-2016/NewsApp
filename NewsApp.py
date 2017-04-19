print "NewsApp"

import requests
import json


def News():
    r = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=a75fa57d45b045f8857f6c2ee117dff6")

    print r.status_code

    #print r.text

    jsonResponse = json.loads(json.dumps(r.json(), indent=2))

    #print "JSON Response:"
    #print json.dumps(r.json(), indent=2)

    print "Headlines"
    print "========="
    print
    for message in jsonResponse['articles']:
        print message['description']
        print
News()
