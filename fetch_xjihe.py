
import requests

# fetch data from http://www.xjihe.com/service/apidemo/56?urlId=47

def fetch_couplewords(output_file):
  api_key = 'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'
  query_type = 1
  url = 'http://www.xjihe.com/api/culture/couplewords'
  max_page = 31
  f = open(output_file, 'w')
  for page in range(0, max_page):
    params = {'query': '', 'querytype': query_type, 'page': page}
    headers = {'apiKey': api_key}
    r = requests.get(url, params=params, headers=headers)
    data = r.json()
    try:
      result = data['result']
      for item in result:
        f.write(item['uplink'] + '\n')
        f.write(item['bottom'] + '\n')
    except KeyError:
      print(data)
    print("Fetched page " + str(page))
  f.close()

fetch_couplewords('/data/dl-data/couplet/couplet.txt')
