### class Line implements Sequence,Statistic,Calculate,Print

一维数据类

- get() -> list
  获取为list
- length() -> int
  获取长度
- replace(old, new) -> self
  old替换为new
- interpolate(old=None, method='slinear') -> self
  将old清除，并插值
    - method: 'zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic'
- toSet() -> self
  去重
- reverse() -> self
  颠倒
- sort() -> self
  排序
- has(e) -> bool
  是否包含元素e
- hasList(l:list) -> bool
  是否包含list，且不间断
- removeElement(e) -> self
  去除元素e
- removeIndex(index:int) -> self
  去除第index个元素
- insertElement(e, index:int) -> self
  在第i个位置插入元素e，原本元素后移
- insertList(l:list, index:int) -> self
  在第index个位置插入list，原本元素后移
- replaceElement(index, e) -> self
  替换第index个元素为e
- replaceList(index, l:list) -> self
  替换第i个元素之后长度与list相同的切片为list
- seqMerge(l:list, index:int=0) -> self
  将list一维化，然后插入到index位置
- shuffle() -> self
  打乱
- getitem(key:int)
- getitem(key:slice) -> Line
- getitem(key:[bool]) -> Line
- setitem(key:Union[int, slice, [bool]], value)
- str
- copy
- deepcopy
- iter
- len
- eq

- toFlat(row:int, col:int=None, fill=none) -> Flat
- toCol() -> Flat

#### Interface Statistic

统计计算类

- mode() -> Line
  众数
- medan() -> float
  中位数
- mean() -> float
  平均值
- sum() -> float
  求和
- max() -> float
  最大值
- min() -> float
  最小值
- variance() -> float
  方差
- standardDeviation() -> float
  标准差
- cv() -> float
  变异系数
- cs() -> float
  偏度系数
- countOfElement(e) -> int
  统计元素个数
- elementOfCount(n:int) -> Line
  统计有n个的元素
- statistic() -> {int:element}, {element, int}
  统计元素
  return
    - {int:element}:有int个element元素
    - {element, int}:元素element有int个

#### Interface Water

水文计算类

- guaranteeValue(r:float) -> float
- guaranteeRate(v:float) -> float

#### Interface Calculate

基本运算类

- calc(sign:str,x,create=False) -> self,Calculate
  所有元素计算
    - sign: '+', '-', '*', '/', '//', '**', '%', 'int', 'str'
    - create: 是否创建新对象
- compare(sign:str, x) -> [bool]
  比较元素，符合为True
    - sign: '==', '!=', '>', '<', '>=', '<=', 'random'

#### Interface Print

控制台打印类

- print() -> self
  简洁打印
- printAll() -> self
  清晰打印全部

#### class Random

随机数类

- random(col:int=1, row:int=1) -> float, Line, Flat
  生成col列row行的随机数

#### class Series

序列类，可以生成各种序列

- range(start:float, end:float, step=1) -> Line
  生成从start开始，步长为step，到end结束的序列
- linespace(start:float, end:float, num:int) -> Line
  生成从start开始，到end结束，步长相等，共num个元素的序列

#### class Flat implements Sequence,Statistic,Calculate,Print,Matrix

二维数组类

- get() -> [[]]
  转化为list对象
- _isRect() -> bool
  是否为矩形
- row() -> int
  行数
- col() -> int
  列数
- size() -> int
  元素个数
- resize(row:int, col:int) -> self
  重置形状
- _checkIndex(row:int=None, col:int=None) -> bool
  检查索引是否合法
- getRow(row:int) -> Line
  获取一行数据
- getCol(col:int) -> Line
  获取一列数据
- insertRow(row:int, l:Line=row()) -> self
  在第row行插入Line，原本行后移
- insertCol(col:int, l:Line=col()) -> self
  在第col列插入Line，原本列后移
- replaceRow(row:int, l:Line) -> self
  替换第row行为l
- replaceCol(col:int, l:Line) -> self
  替换第col列为l
- removeRow(row:int) -> self
  移除第row行，后面行前移
- removeCol(col:int) -> self
  移除第col列，后面列前移

- selfAdd(horizontal:bool=False) -> Line
  水平方向自加
    - horizontal: 改为竖直方向
- toLine() -> Line
  二维数据排列为一维

- getitem
- setitem
- eq
- len
- str
- copy
- deepcopy
- iter

#### class Matrix implements Sequence,Print

矩阵类，实现了矩阵运算，也有其他矩阵操作

- transpose(backslash:bool=False, create:bool=False) -> self, Flat
  转置
    - backslash: 对称轴改为'\'方向
- mirror(horizontal:bool=False, create:bool=False) -> self, Flat
  水平方向镜像
    - horizontal: 改为竖直方向
- rotate(degree:[90,180,270], create:bool=False) -> self, Flat
  旋转90度、180度、270度数据

- _mIsSquare() -> bool
  矩阵是否是方阵
- mValue() -> float
  矩阵求行列式的值
- mRank() -> int
  矩阵阶数
- mNorm() -> float
  矩阵范数
- mEigen()
  矩阵特征值
- mTrace() -> float
  矩阵的迹
- mIsSymmetry(anti:bool=False) -> bool
  矩阵是否是对称矩阵
    - anti: 是否为反对称矩阵
- mIsExchangeable(other:Matrix) -> bool
  与other矩阵是否可交换

- mInverse() -> Flat
  矩阵求逆
- mCofactor() -> Flat
  矩阵余子式
- mAdjoint(row:int, col:int) -> Flat
  伴随矩阵
- mUpTriStep() -> Flat
  上三角阶梯型矩阵
- mDowmTriStep() -> Flat
  下三角阶梯型矩阵

- mSolveLinearEquation()
  线型方程组求解

#### class SheetReader

表格读取器，支持xlsx、csv格式

- sheetNames() -> Line
  获取该文件所有sheet名称
- getSheetData(sheet:str=sheetNames()[0]) -> Flat:
  获取该sheet中的数据

#### class SheetWriter

表格写入器，支持xlsx、csv格式

- appendSheet(dss=[[]],sheet=f'sheet{len(sheetNames())}')
- removeSheet(sheet:str)

#### class Function

基本函数类

- sign(x) -> int
  符号函数
- linear(xs:Sequence, ys:Sequence) -> (k, b, r)
  线性回归
- entropyWeight(dss: Sequence[Sequence], distincts: Sequence[bool] = None, move: float = 1e-9)

#### class Figure

图表绘制类 

- point()
- point3d()
- pointSize()
- pointPolar()

- bar(horizon)
- barGroup(horizon)
- barStack(horizon)
- barPolar()
- bar3d()
- barHist()

- pie()
- pieStack()
- pieNest()

- hot()
- hotBorder()
- hinton()

- line()
- lineMultiple()
- lineStack()
- lineStem()
- linePolar()

- box()
- violin()

- error()
- errorArrow()
- errorBox()

- voronoi()