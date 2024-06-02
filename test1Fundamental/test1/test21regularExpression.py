"""
正则表达式

    一、
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释

    二、
.	匹配任意1个字符（除了\n）
[ ]	    匹配[ ]中列举的字符
\d	                匹配数字，即0-9	                可以写在字符集[...]中
\D	                匹配⾮数字，即不是数字	            可以写在字符集[...]中
\s	                匹配空⽩，即空格，tab键	            可以写在字符集[...]中
\S	                匹配⾮空⽩字符	                    可以写在字符集[...]中
\w	                匹配单词字符，即a-z、A-Z、0-9、_	可以写在字符集[...]中
\W	                匹配⾮单词字符	                    可以写在字符集[...]中
\w	\w              匹配单词字符，即a-z、A-Z、0-9、_
\W	                匹配⾮单词字符
[\u4e00-\u9fa5]     中文

    三、
*	    匹配前⼀个字符出现0次或者⽆限次，即可有可无	                            用在字符或(...)之后
+	    匹配前⼀个字符出现1次或者⽆限次，即⾄少有1次	                        用在字符或(...)之后
?	    匹配前⼀个字符出现1次或者0次，即要么有1次，要么没有	                    用在字符或(...)之后
{m}	    匹配前⼀个字符出现m次	                                            用在字符或(...)之后
{m,n}	匹配前⼀个字符出现从m到n次，若省略m，则匹配0到n次，若省略n，则匹配m到无限次	用在字符或(...)之后

    四、
^	匹配字符串开头
$	匹配字符串结尾

    五、
|	        匹配左右任意⼀个表达式
(ab)	    将括号中字符作为⼀个分组
\num	    引⽤分组num匹配到的字符串
(?P<name>)	分组起别名，匹配到的子串组在外部是通过定义的 name 来获取的
(?P=name)	引⽤别名为name分组匹配到的字符串

"""

import re

p1 = '\d\.\d+'
s = '2.21, I am study python 3.9.0 today'
# match只查找开头，没有则返回None
print(re.match(p1, s))
# search从开头开始查找，查到一个为止
print(re.search(p1, s, re.I))
# findall查找所有,返回列表
print(re.findall(p1,s))
# sub替换，常用于隐藏和屏蔽
print(re.sub(p1,'***',s))
# split分割
print(re.split(p1,s))