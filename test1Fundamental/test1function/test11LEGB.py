"""
类同名属性的寻找规则
就近原则
"""
print(str)
# str = 'global'
print(str)


def outer():
    # str = 'outer'
    print(str)

    def inner():
        # str = 'inner'
        print(str)

    inner()


outer()
