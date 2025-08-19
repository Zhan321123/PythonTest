"""
req = requests.request(method, url, headers, params, json, stream:bool=False, allow_redirects:bool=True, timeout:tuple)

Image.open(io.BytesIO(req.content))

ses = requests.session()
"""
import io
from pathlib import Path
from pprint import pprint

import requests
from PIL import Image


def getRequestInfo(method: str, url: str, headers: dict = {}, params: dict = {},
    json: dict = {}, files = {}, auth=(), cookies: dict = {}) -> dict:
  """
  :param method: [GET, POST, PUT, DELETE, PATCH, OPTIONS]
  :param url:
  :param headers:
  :param params: == url?key=value&...
  :param json: 携带数据
  :param auth: (username, password)
  :param cookies:
  :param files:
  :return:
  """
  try:
    req = requests.request(method, url, headers=headers, params=params, json=json,
      files=files, auth=auth, cookies=cookies, timeout=(3, 10), allow_redirects=True)
  except requests.exceptions.RequestException as e:
    print(e)
  result = {
    "StatusCode-请求状态码": req.status_code,
    "Reason-状态": req.reason,
    "Ok-状态码是否正常": req.ok,
    "Headers-请求头": dict(req.headers),
    "Text-请求结果": req.text,
    "Url-请求网址": req.url,
    "Cookies-请求cookies": dict(req.cookies),
    "Request-请求对象": req.request,
    "Elapsed-请求耗时": req.elapsed,
    "Encoding-编码": req.encoding,
    "History-历史请求": req.history,
    "Content-未解析内容": req.content,
    "ApparentEncoding-响应编码": req.apparent_encoding,
    "IsRedirect-服务端啊资源是否重定向": req.is_redirect,
    "IsPermanentRedirect-服务端资源是否永久重定向": req.is_permanent_redirect,
    "Links-响应头链接": req.links,
    "Next-下一跳": req.next,
    "Raw-原始内容": req.raw,
    "RaiseForStatus-响应短语": req.raise_for_status()
  }
  pprint(result)
  return result


if __name__ == '__main__':
  thisPath = Path(__file__).parent.resolve()

  # getRequestInfo("get", "http://localhost:5000/api/city", params={"province": "浙江"})

  # getRequestInfo("POST", "http://localhost:5000/api/avatar",
  #   files={"file": open(r"C:\Users\刘高瞻\Desktop\Fantastic\texture\item\thorn_chakram.png", "rb")})

  # getRequestInfo("GET", 'http://localhost:5000/api/avatar', params={"filename": "thorn_chakram.png"})
  # image = Image.open(io.BytesIO(req.content))
  # image.show()

  # getRequestInfo("POST", "http://localhost:5000/ap/login", auth=("admin", "123456"))

  # getRequestInfo("GET", "http://localhost:5000")
  # session = requests.session()
  # session.auth = ("admin", "123456")
  # r = session.request("GET", "http://localhost:5000/api/login")
  # print(r.text)

  getRequestInfo('post', "http://localhost:5000/api/article", files=[
    ("file", ("new.txt", open(r"C:\Users\刘高瞻\Desktop\新建 文本文档.txt", "rb"), 'text/plain')),
    ("images", ("ram.png", open(r"C:\Users\刘高瞻\Desktop\Fantastic\texture\item\thorn_chakram.png", 'rb'), 'image/png'))
  ])
