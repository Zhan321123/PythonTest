"""
艺术字

暂不妙
"""

import pyfiglet
text = "Hello, everyone!"
art = pyfiglet.figlet_format(text, font="slant")
print(art)
