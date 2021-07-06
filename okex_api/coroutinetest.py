# 最早的时候 python 提供了yield 关键字 
# 包含有yield的函数，都是一个生成器
# yield 语法规则：在yield这里暂停函数的执行，并返回yield后面表达式的值，默认为None，直到被next()方法再次调用
# 从上次暂停的yield代码处继续往下执行
# yield 在初次使用的时候，相当于初始化了一个generator，首次运行 卡在yield那里， next()之后 返回第一次的值, 
# yield 在初次使用的时候，相当于 for i in (): 没有运行
# 而不是 首次运行就返回一个东西
# 首次运行的时候 yield就卡住程序

def mytest1(n):
    b = 1
    i = 0
    while i < n:
        yield b
        b += 1
        i += 1


def mytest2():
    print(f"-> 启动协程")
    y = 10
    while True:
        x = yield y
        print(f'-> 协程接受到了x的值 {x}')


import asyncio
import datetime
@asyncio.coroutine
def mytest3(num, loop):

    i = 10
    i = 0
    while True:
        print(f"Loop: {num}  {i}  Time: {datetime.datetime.now()}")
        i += 1
        if i >= 10:
            break
        # 阻塞直到协程 返回一个结果
        # 模拟一个网络获取，一个I/O过程
        yield from asyncio.sleep(num)


async def mytest4(num, loop):
    end_time = loop.time() + 10
    while True:
        print(f"Loop: {num} Time: {datetime.datetime.now()}")
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)

        



if __name__ == "__main__":
    # f = mytest1(5)
    # next(f)

    # f = mytest2()
    # ret = next(f)
    # print(ret)
    # f.send(15)
    
    # 获取一个event_loop 也就是说 哪些东西参与到这个协程里面来
    loop = asyncio.get_event_loop()
    # 设立两个任务
    tasks = [mytest3(1, loop), mytest3(5, loop)]
    # 阻塞直到所有的任务结束
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    print("done")



