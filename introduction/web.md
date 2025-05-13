<h1 style="text-align: center;">Web</h1>

<hr>

### 网址组成

- protocol 协议

  - http://
  - https://
  - ftp://

- domain 域名

  - ipv4
  - www.xxx.com
  - 127.0.0.1
  - localhost

- port 端口

    :int(0~65535)

- path 路径

    /path1/path2

- query parameter 查询参数

    ?key1=value1&key2=value2

- anchor 锚点

    #anchor


### 状态码

- 1xx 信息
  - 100 Continue 客户端应当继续发送请求
  - 101 Switching Protocols 
  - 102 Processing
  - 103 Early Hints
- 2xx 成功
  - 200 OK 响应成功，并返回内容
  - 201 Created 服务端成功创建资源
  - 202 Accepted
  - 203 Non-Authoritative Information
  - 204 No Content 响应成功，但无内容
  - 205 Reset Content
  - 206 Partial Content
  - 207 Multi-Status
  - 208 Already Reported
- 3xx 重定向
  - 300 Multiple Choices 
  - 301 Moved Permanently 服务端将该资源已永久移动到新位置
  - 302 Found 服务端将资源临时移动到新位置
  - 303 See Other
  - 304 Not Modified 资源未修改，客户端应当使用已缓存的资源
  - 305 Use Proxy
  - 306 Switch Proxy
  - 307 Temporary Redirect
  - 308 Permanent Redirect
  - 309 Unused
  - 310 Use Subscription
- 4xx 客户端错误
  - 400 Bad Request 客户端请求格式错误
  - 401 Unauthorized 客户端用户未认证
  - 402 Payment Required
  - 403 Forbidden 客户端用户信息认证未通过
  - 404 Not Found 被请求的资源不存在
  - 405 Method Not Allowed 客户端请求方法不允许
  - 406 Not Acceptable
  - 407 Proxy Authentication Required
  - 408 Request Timeout
- 5xx 服务器错误
  - 500 Internal Server Error 服务端内部代码运行错误
  - 501 Not Implemented
  - 502 Bad Gateway
  - 503 Service Unavailable 服务端无法处理请求
  - 504 Gateway Timeout
  - 505 HTTP Version Not Supported
  - 506 Variant Also Negotiates

### word

- DNS 服务器
- 以太网
- IPv4地址
- 子网掩码
- 默认网关
- 局域网
- VPN
- 端口号
- 代理
- 协议
- 网络频段
- 网络通道
- 物理地址

### cmd

- `ipconfig` 显示网络信息
- `ping [ip]` 测试网络连接
- `tracert [ip]` 测试网络路径
- `nslookup [ip]` 域名解析
- `whois [ip]` 域名查询