

a=100

def change():
    global a
    a=200

print(a)

change()
print(a)

def get():
    a=300
    print(a)

    print(locals())
    print(globals())
    print('########################')
    for i in globals():
        print(i)

get()