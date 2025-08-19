import http.client
import json
from pprint import pprint
from urllib.parse import quote


def code(s):
  s.decode('utf-8').encode().decode('unicode_escape')
  try:
    result = json.loads(s)
  except ValueError:
    raise ValueError(s, '\n ***is not json***')
  return result


connect = http.client.HTTPConnection('localhost:5000')

if __name__ == '__main__':
  connect.request("get", "/api/province", headers={}, )
  res = connect.getresponse()
  data = res.read()
  r = code(data)
  pprint(r)
  print(r['message'])

  connect.request("get", f"""/api/city?province={quote('浙江')}""", headers={})
  pprint(code(connect.getresponse().read()))

  connect.request('get', f"""/api/area?city={quote('杭州')}&province={quote("浙江")}""")
  pprint(code(connect.getresponse().read()))

  connect.request("get", "/api/news", headers={})
  pprint(code(connect.getresponse().read()))

  connect.request("post", "/api/register",
    headers={'Content-Type': 'application/json'},
    body=json.dumps({
      'username': 'zhan_sir',
      'password': '123456',
    }))
  pprint(code(connect.getresponse().read()))

  connect.request("post", "/api/login",
    headers={'Content-Type': 'application/json'},
    body=json.dumps({
      'username': 'zhan_sir',
      'password': '666666',
    }))
  pprint(code(connect.getresponse().read()))
