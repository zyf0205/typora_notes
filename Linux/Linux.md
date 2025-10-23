### 1.shell命令和path路径

**linux命令**

**命令           选项          参数**

command [-options] [parameter]

------

**如何添加path路径?**

1. 在~/.bashrc中设置path路径,添加后home/book里面的东西就可以被shell找到了

```plain
export PATH=$PATH:/home/book
```

1. 修改/etc/environment,在后面添加新的路径

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1746880119227-45a7d90f-81f1-4d33-ad20-84cc298c41e4.png)

```plain
sudo gedit /etc/environment #编辑指定文件
:/home/book #在后面添加这种目标目录
```

------

### 2目录和文件操作命令

/:根目录    ~:home目录(当前用户路径)

```plain
cd -       #回到上一次在的目录
mkdir <name> #创建文件夹
rm -rf <目录路径> #删除文件/文件夹
rm <name> #删除文件
ls -l #列出文件详细信息
cp 1.txt 2.txt #将1.txt拷贝到2.txt
mv 1.txt 2.txt #将1.txt改名(移动)为2.txt
mv 1.txt ../ #将1.txt移动到上一目录
mv ../1.txt . #将上一目录的1.txt移动到当前目录
cat 1.txt #将1.txt文件内容显示出来
```

------

### 3.文件权限与属性

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1746881485760-0768c232-7440-464e-a765-7578a0a39ec1.png)

4 2 1

7 7 5

-:常规文件

r:读  -不可读

w:写 -不可写

x:可执行 不可执行

```plain
chmod 675 <name> #改变权限为:-rw-rwxr-x
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1746881816762-cced62d6-1906-46fc-b272-6f1263defff6.png)改变过后就不可以执行了

```plain
chmod -x hello #去除所有用户的x权限
chmod +x hello #添加所有用户的x权限
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1746881983181-32ceff9a-5f2d-4288-8aac-f396a26e9290.png)

------

### 4.find和grep命令

```plain
find abc -name 2.txt #查找abc目录中的2.txt
find abc -name "*2.txt" #通过通配符查找abc目录中的东西
grep "abc" * -nwr #查找当前目录下内容中有abc的文件
```

------

### 5.压缩和解压缩命令

```plain
gzip -k <name> #将指定文件压缩为.gz文件,并保留源文件
bzip2 -k <name> #.bz2相比于gzip,压缩率更高
gzip -dk test.gz #
bzip2 -dk test.bz2 #
```

使用tar命令:

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1746882920255-ea685c84-c57b-4f50-adad-1a45238a35d9.png)

```plain
tar czf test.tar.gz test #将test->test.tar.gz
tar xzf test.tar.gz #解压
tar cjf test.tar.bz2 test #test->test.tar.bz2
tar xjf test.tar.bz2 #解压
tar cjf abc.tar.bz2 abc #压缩abc目录
tar xjf abc.tar.bz2 #解压abc目录到当前目录
tar xjf abc.tar.bz2 -C <目录> #解压到指定目录
```

------

### 6.vi编辑器

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1746883863686-9793df79-71d1-441f-878d-352dfb4c4b93.png)

快捷键:

G:跳到文件结尾

O:跳到行首

$:跳到行尾

```plain
:set number #显示行号
:set nonumber #去掉行号
:250 #跳到250行
ctrl+f #向前翻页
ctrl+b #向后翻页
dd #删除整行
ndd #删除当前行及后面n-1行
o #在当前行下面新增一行
u #撤销上一步操作

yy #复制当前行
nyy #复制当前行及后面n-1行
p #粘贴

/custom #从光标开始处向文件尾搜索custom,按n向下查找,按N向前查找
:%s/custom/Custom/g #将全局custom替换为Custom
:%s/custom/Custom/gc #将全局custom替换为Custom,不过需要每一个确认是否替换
```







































```plain
sudo service NetworkManager stop
sudo rm /var/lib/NetworkManager/NetworkManager.state
sudo service NetworkManager start
sudo dpkg -i (要安装的包名)
sudo dpkg -l | grep "clash"
sudo dpkg -r clash-verge
sudo gedit /etc/default/grub
sudo update-grub
```