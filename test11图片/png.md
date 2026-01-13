<h1 style="text-align: center;">PNG</h1>

  压缩一张mc的texture图，设为P模式，并将transparency的索引放在第0个位置，一般可以最大程度压缩


## color mode

- `RGBA(red, green, blue, alpha)`
- `RGB(red, green, blue)` 
- `GrayAlpha/GA/LA(grayscale with alpha)` 灰度+透明度
- `Gray/G/L(grayscale)` 单通道8位灰度图
- `1(binary)` 黑白模式，0为黑，1为白
- `I` 单通道16位灰度图
- `P(palette)` 调色板
  P模式下的调色板是RGB，info中存储transparency的索引

# info

- `transparency: int/color` 透明度索引
- `gamma: float`
- `srgb:`
- `dpi: tuple(float, float)`

## 位

- `8位` 0-255
- `16位` 0-65535

## 颜色表示

- hex颜色表示(16进制, rgba:(0~9a~f))
  - #rrggbb
  - #rrggbbaa
  - #rgb = #rrggbb
- rgb颜色表示(rgb:(0~255), a:(0~1))
  - rgb(r, g, b)
  - rgba(r, g, b, a)
- 灰度表示(gray:(0~255))
  - gray(gray)
