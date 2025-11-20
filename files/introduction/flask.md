<h1 style="text-align: center;">Flask</h1>

<hr>

### flask启动

```
import flask
app = flask.Flask(__name__)
@app.route('/')  # 此处配置路由
def index():
  return 'hello world'
if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)
```

### 路由
- / 根路由 url = host:port
- /route 路由 url = host:port/route, 不支持 host:port/route/
- /route/ 路由 url = host:port/route/ or host:port/route
- /<int:id> int路由 /123
- /<float:float> float路由 /1.23
- /<string:name> str路由，不支持/ /zhan
- /<path:path> path路由，可以带有/ /liu/gao/zhan


