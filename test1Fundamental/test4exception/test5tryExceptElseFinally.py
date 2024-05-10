"""
完整异常写法
"
try:
except:
else:
    没有异常时执行的code
finally:
    最终一定会执行的code，无论有无异常
"
"""
file = None
try:
    file = open('11.txt','w',encoding='utf-8')
    file.write('fuck you')
    file.write([1,2,3])
    print('write completed')
except IOError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('write successful')
finally:
    file.close()
    print('file close')