import re
from typing import Sequence


def rgba1ToHex(rgba: Sequence):
    """
    rgba(0~1) to hex(#0-f)
    """
    rgba = [int(val * 255) for val in rgba]
    return rgba255ToHex(rgba)



def rgba255ToHex(rgba: Sequence):
    """
    rgba(0~255) to hex(#0-f)
    """
    # 使用格式化字符串将 RGB 值转换为十六进制颜色代码
    if len(rgba) == 3:
        r, g, b = rgba
        return f'#{r:02x}{g:02x}{b:02x}'
    elif len(rgba) == 4:
        r, g, b, a = rgba
        return f'#{r:02x}{g:02x}{b:02x}{a:02x}'
    else:
        raise ValueError("颜色序列必须为[R,G,B,A] or [R,G,B]")


def hexToRgba255(hexc: str)->Sequence:
    """
    hex(#0-f) to rgba(0~255)
    """
    if len(hexc) == 7:
        match = re.match(r'#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})', hexc)
        if match:
            r, g, b = [int(val, 16) for val in match.groups()]
            return r, g, b
    elif len(hexc) == 9:
        match = re.match(r'#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})', hexc)
        if match:
            r, g, b, a = [int(val, 16) for val in match.groups()]
            return r, g, b, a
    else:
        raise ValueError("颜色序列必须为 #RRGGBB or #RRGGBBAA")


if __name__ == '__main__':
    l = [[65, 90, 155],
         [223, 191, 117],
         [113, 180, 144],
         [144, 5, 61],
         [164, 105, 189],
         [198, 95, 16],
         [36, 153, 16], ]
    for i in l:
        print(f'"{rgba255ToHex(i)}"')
