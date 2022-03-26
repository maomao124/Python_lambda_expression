"""
 * Project name(项目名称)：Python_lambda表达式
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 14:37
 * Version(版本): 1.0
 * Description(描述)：lambda 表达式，又称匿名函数，常用来表示内部仅包含 1 行表达式的函数。
 如果一个函数的函数体仅有 1 行表达式，则该函数就可以用 lambda 表达式来代替。
lambda 表达式
name = lambda [list] : 表达式
其中，定义 lambda 表达式，必须使用 lambda 关键字；[list] 作为可选参数，等同于定义函数是指定的参数列表；value 为该表达式的名称。

对于单行函数，使用 lambda 表达式可以省去定义函数的过程，让代码更加简洁；
对于不需要多次复用的函数，使用 lambda 表达式可以在用完之后立即释放，提高程序执行的性能。
 """


def add(x, y):
    return x + y


add1 = lambda x, y: x + y

if __name__ == '__main__':
    print(add(3, 4))
    print(add1(3, 4))
    add2 = lambda x, y: x + y
    print(add2(3, 4))

