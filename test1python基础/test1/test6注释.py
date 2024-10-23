"""
注释
    # 单行注释
    '''模块、方法注释''' 多行文本，特殊位置是文档注释

标记注释
    # TODO 需要完成
    # FIXME 请完善
    # HACK 待处理
    # XXX 警告
    # NOTE 提示

添加方法 in
    pycharm：文件 -> 设置 -> 编辑器 -> TOD0
    idea：

方法相关的文档注释
    :param 参数名: 参数的注释
    :return: 返回值的注释
    :raise: 异常的注释
    示例
    example:
        >>> add(1,2)
        3

文档注释中的数学表达式 :math:`表达式`
    分数          \\frac{a}{b}
    根号          \sqrt{a}
    n次开根号      \sqrt[3]{a}
    乘方、上标      a^b
    积分符号       \int_{a}^{b}
    求和          \sum_{i=1}^{n} i
    求积          \prod_{i=1}^{n} i
    下标           a_b



"""


def add(a: int, b) -> int:
    """
    方法的文档注释

    :param a:
        参数1的文档注释
    :param b:
        参数2的文档注释
    :return:
        返回值的文档注释

    example:
        >>> add(1,2)
       3
    """
    return a + b


def f():
    """
    这里需要这样（注意这里后面有空格） :math:`\sum_{i=1}^n i^2`，然后这样
    :math:`\\frac{a}{b}`
    :math:`\sqrt[3]{a^3}`
    :math:`\int_{}^{}xdx`
    :math:`\sum_{i=1}^{n} i`
    :math:`\prod_{i=1}^{n} i`
    """
