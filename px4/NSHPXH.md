## 1.NSH

NuttX操作系统提供的类似Linux Shell的工具，称为NuttX Shell (NSH)，QGC地面站集成了NSH终端。

NSH命令的一般形式为

```
命令名  参数1 参数2 参数3 ... 参数n
```

## 2.PXH

PXH(PX4 shell)是仿真固件使用的命令行，除了不提供NuttX操作系统的内置命令外，对于应用程序的使用命令和NSH几乎一致

## 3.常用命令

`help` #获取系统中所有命令的信息

`ver all` #打印出px4系统相关软硬件信息

`free` #显示系统内存使用情况

`top` #查看运行的任务和cpu占用情况