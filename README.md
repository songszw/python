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

在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
--- 'Hello, %s' % 'world'
'Hello, world'
--- 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.

在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
###注意

* 在python缩进方面，按照约定俗成的管理，应该始终坚持使用4个空格的缩进
* 在python中是区分大小写的，如果写错了大小写那么程序就会报错

