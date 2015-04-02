import urllib2
import json


def get_page_data(page_id):
    endpoint = "https://graph.facebook.com"
    graph_url = endpoint + '/' + page_id
    try:
        request = urllib2.Request(graph_url)
        response = urllib2.urlopen(request)

        try:
            return json.loads(response.read())

        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

# username or id
page_id = "AdvancedITSolutions.net"

data = get_page_data(page_id)

for key,items in data.iteritems():
    print str(key) + ' : ' + str(items) + '\n'