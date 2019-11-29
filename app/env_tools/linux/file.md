# 文件/文件夹管理

* 列出当前目录文件

```bash
ls # 不包括隐藏文件
ls -a # 包括隐藏文件
ls -l # 列出当前目录下文件的详细信息
ll # 详细细信息
```

* ll 命令来判断文件类型，主要是根据每行的首个字符来判断。

```
-rw-r—r— "-“开头的都是普通文件;
drw-r—r— "d"开头的是目录文件;
brw-r—r— "b"开头的文件都是块设备文件;
crw-r—r— "c"开头的文件都是字符设备文件;
srw-r—r— "s"开头的文件都是 socket 文件; (e.g. srwxrwxrwx 1 mysql mysql 0 Sep 9
13:49 mysql.sock)
prw-r—r— "p"开头的文件都是管道文件;
lrw-r—r— "l"开头的文件都是软链接文件;
```

* cd

```bash
cd .. # 回当前目录的上一级目录
cd - # 回上一次所在的目录
cd ~ # 或 cd 回当前用户的宿主目录
```

## 文件

* 创建文件

```bash
touch <文件>
```

* 删除文件

```bash
# -r：递归的删除目录下面文件以及子目录下文件。
# -f：强制删除，忽略不存在的文件，从不给出提示
rm -rf <文件>
```

* 修改文件名

```bash
mv <文件> <文件_改名>
```

* 查看文件内容

```bash
cat <文件>
cat <文件> | head -3 # 查看文件前３行
cat <文件> | tail -3 # 查看文件后３行
```

* 复制文件

```bash
cp <文件>　<文件_拷贝>
```

* 移动文件

```bash
mv <文件> <路径><文件>
```

* 编辑文件

```bash
vi <文件>
```

* 批量创建/删除文件

```bash
touch file{1..10}
rm -fr file{1..10}
```

* 查找文件

1. 第一种

```bash
find / -name txt.txt # find 目录 -name 文件名
```

2. 第二种

速度快

```bash
apt install mlocate # 安装
```

```bash
updatedb
locate txt.txt
```

* 查找文件里的内容

```bash
cat txt.txt | grep d
cat txt.txt | grep -i d # 忽略大小写
```

* vi搜索

```bash
vi txt.txt
/d # 搜索 d N 下一个
```

## 目录

* 创建

```bash
# mkdir -p a/b/c/d/e/f/g # 递归创建
mkdir <目录>
```

* 删除

```bash
# rmdir 空目录名 删除一个空目录
# rmdir 空目录名 删除一个空目录
rm -rf <目录>
```

* 重命名或移动

```bash
mv <目录> <目录_移动/改名>
```

* 复制

```bash
cp -rf <目录> <目录_拷贝>
```

* 递归查看目录

```bash
tree
```

___
> 共同学习，共同进步