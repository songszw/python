# python
python笔记

### 退出    exit()

### 输出（打印指定内容）    print('')
    想要输出结果就必须用print()打印出来
    
### 输入     input()

### 字符编码转换
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
eg: 
ord('a')    ---97
chr(97)     ---'a'
    
Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示：
eg:
x = b'ABC'

要计算str包含多少个字符，可以用len()函数
eg:
len('ABC')    ---3
len('中文')   ---2

1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

### 格式化

#####在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
--- 'Hello, %s' % 'world'
'Hello, world'
--- 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.

%d	整数

%f	浮点数

%s	字符串

%x	十六进制整数

#####在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

### list

list是一种有序的集合，可以随时添加和删除其中的元素。


--- classmates = ['Michael', 'Bob', 'Tracy']

--- classmates

['Michael', 'Bob', 'Tracy']


#####变量classmates就是一个list。用len()函数可以获得list元素的个数：

--- len(classmates)
3


#####用索引来访问list中每一个位置的元素，记得索引是从0开始的：

--- classmates[0]

'Michael'

--- classmates[1]

'Bob'

--- classmates[2]

'Tracy'


#####如果超出范围会报错

--- classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range


#####如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

--- classmates[-1]

'Tracy'


###增删改查：

#####增加

--- classmates.append('Adam')

--- classmates

['Michael', 'Bob', 'Tracy', 'Adam']

#####也可以把元素插入到指定的位置，比如索引号为1的位置：

--- classmates.insert(1, 'Jack')

--- classmates

['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

#####要删除list末尾的元素，用pop()方法：

--- classmates.pop()

'Adam'

--- classmates

['Michael', 'Jack', 'Bob', 'Tracy']


#####要删除指定位置的元素，用pop(i)方法，其中i是索引位置：

--- classmates.pop(1)

'Jack'

--- classmates

['Michael', 'Bob', 'Tracy']


#####要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

--- classmates[1] = 'Sarah'

--- classmates

['Michael', 'Sarah', 'Tracy']


### tuple

#####tuple是一个有序列表，与list类似，但是tuple一旦初始化不可修改。
因为元组一旦生成不能改变，所以它没有append和insert，pop等方法，但是相对list来说，也更加安全。


###条件判断

基本语法

if 条件 :         冒号必不可少
    条件成立后执行的demo
else:             冒号必不可少
    条件不成立时候所需要执行的demo
    
    
    
eg: age = 3

if age >= 18:

    print('your age is', age)
    
    print('adult')
    
else:

    print('your age is', age)
    
    print('teenager')
    
#####elif  else if的简写，在写if判断时候，可以有多个elif，

if 条件判断1:

    执行1
    
elif 条件判断2:

    执行2
    
elif 条件判断3:

    执行3
    
else:

    执行4
    
    
##### if判断条件还可以简写，比如写：

if x:

    print('True')
    
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
    

### 循环
#####Python的循环有两种，一种是for...in循环，另一种是while循环

eg：

names = ['Michael', 'Bob', 'Tracy']

for name in names:

    print(name)
    
执行这段代码，会依次打印names的每一个元素：

Michael

Bob

Tracy

#####所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

#### range（）就可以生成整数序列的函数

eg：
sum = 0
for x in range(5):
    sum = sum + x
    print(sum)
    
0

1

3

6

10



    

###注意


* 在python缩进方面，按照约定俗成的管理，应该始终坚持使用4个空格的缩进
* 在python中是区分大小写的，如果写错了大小写那么程序就会报错

