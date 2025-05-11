<h1 style="text-align: center;">SVG</h1>

### 链接

- [SVG规范](https://www.w3.org/TR/SVG/)
- [菜鸟svg示例](https://www.runoob.com/svg/svg-examples.html)

### 示例

<svg xmlns="http://www.w3.org/2000/svg"
  width=100 height=100 
  version=1.1 
  viewBox="0 0 100 100" 
  style = "border: 1px solid #0ff;">
  <circle cx=50 cy=50 r=40 fill="red"/>
  <text x=50 y=50 text-anchor="middle" fill="white" font-size=20>SVG</text>
  <path  d="M 0 0 L 100 100" stroke="black" stroke-width="2" fill="none"/>
</svg>

### svg属性

- xmlns: 命名空间, 默认是 http://www.w3.org/2000/svg
- width、height: 宽度、高度 (px)
- viewBox: 显示区域, 默认是 "0 0 100 100"
- version: 版本, 默认是 1.1

### svg元素

- circle: 圆形
  - cx cy: 圆心坐标
  - r: 半径
  - fill stroke stroke-width: 填充颜色 描边颜色 描边宽度
  - stroke-linecap: 描边端点样式
    - butt 直角
    - square 方形
    - round 圆形
    - bevel 斜角
  - stroke-dasharray: 虚线样式 "实线长 虚线间隔 实线长 虚线间隔 ..."
  - transform: 旋转 rotate(θ, x, y) 绕点(x,y)旋转θ度

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;"><circle cx="50" cy="50" r="30" fill="#f0f"/></svg>

- rect: 矩形
  - x y: 矩形左上角坐标
  - rx/ry: 圆角半径
  - width height: 矩形宽高
  - fill stroke stroke-width transform

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;"><rect x="20" y="20" rx="10" width="60" height="60" fill="#f0f"/></svg>

- ellipse: 椭圆
  - cx cy: 圆心坐标
  - rx ry: 椭圆半径
  - fill stroke stroke-width transform

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;"><ellipse cx="50" cy="50" rx="30" ry="20" fill="#f0f"/></svg>

- polygon: 多边形
  - points: 多边形顶点坐标
  - fill stroke stroke-width transform
  - fill-rule: nonzero/evenodd: 填充规则, 默认是 nonzero, nonzero表示奇数填充, evenodd表示偶数填充

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;"><polygon points="50 20 80 50 50 80 20 50" fill="#f0f"/></svg>

- polyline: 折线
  - points: 折线点坐标

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;"><polyline points="20 80 50 20 80 80" stroke="#f0f"/></svg>

- line: 线段
  - x1 y1: 起始点坐标
  - x2 y2: 结束点坐标
  - stroke stroke-width: 线条颜色 线条宽度

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;">
      <line x1="20" y1="20" x2="80" y2="80" stroke="#f0f"/>
      <line x1="80" y1="20" x2="20" y2="80" stroke="#f0f"/>
    </svg>

- path: 路径
  - d: 路径表达式
    - M x y: 移动到绝对点坐标 (x,y)
    - m dx dy: 移动到相对与当前点坐标 (dx,dy)

    - L x y: 画直线到绝对点坐标 (x,y)
    - l dx dy: 画直线到相对与当前点坐标 (dx,dy)
    - H x: 画水平线到绝对点坐标 x
    - h dx: 画水平线到相对与当前点坐标 dx
    - V y: 画垂直线到绝对点坐标 y
    - v dy: 画垂直线到相对与当前点坐标 dy

    - Q x1 y1 x2 y2: 画二次贝塞尔曲线
    - q dx1 dy1 dx2 dy2: 画二次贝塞尔曲线
    - C x1 y1 x2 y2 x3 y3: 画三次贝塞尔曲线
    - c dx1 dy1 dx2 dy2 dx3 dy3: 画三次贝塞尔曲线
    - T x y: 继续画二次贝塞尔曲线
    - t dx dy: 继续画二次贝塞尔曲线

    - A rx ry xAxisRotation largeArcFlag sweepFlag x y: 画椭圆圆弧
      1. rx ry: 椭圆的长轴和短轴的半径
      2. xAxisRotation: 椭圆的旋转角度
      3. largeArcFlag: 是否画大弧，0表示画小弧，1表示画大弧
      4. sweepFlag: 是否顺时针画弧，0表示逆时针，1表示顺时针
      5. x y: 终点坐标

    - Z/z: 闭合路径

- text: 文本
  - x y: 文本坐标
  - text-anchor: 文本对齐方式, start/middle/end

    <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;">
      <text x="50" y="50" text-anchor="middle" fill="#f0f" font-size=50>SVG</text>
      <text x="50" y="100" text-anchor="middle" fill="#f0f" font-size=50>SVG</text>
    </svg>

- 路径上的文本
  - defs path id="...id" d="...d"
  - text textPath  xlink:href="#...id"

- g: 组合元素，减少代码

  <svg width=24 viewBox="0 0 100 100" style = "border: 1px solid #0ff;">
    <g transform="rotate(45, 50, 50)" fill="#0000" stroke="#f0f" stroke-width="3">
      <rect x="20" y="20" rx="10" width="60" height="60"/>
      <ellipse cx="50" cy="50" rx="30" ry="20"/>
    </g>
  </svg>

### svg净化

### svg贴边

### 注意点

- 属性值为单个纯数字时，可以省略""，直接写数字
