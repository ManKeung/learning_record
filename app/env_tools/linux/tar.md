# 打包压缩命令

目前 linux 中打包和压缩的命令很多，最常用的方法有 zip、gzip、bzip2、xz、tar

## zip压缩包

* 制作

```bash
# -r 递归 表示将指定的目录下的所有子目录以及文件一起处理
zip -r public.zip public
```

* 解压

```bash
unzip public.zip
unzip public.zip -d dir # 在dir文件下解压
```

* 查看

```bash
unzip -l public.zip
```

## gz压缩包

Linux下最常用的打包程序就是tar了，使用tar程序打出来的包我们常称为tar包，tar包文件的命令通常都是以.tar结尾的。生成tar包后，就可以用其它的程序来进行压缩了，所以首先就来讲讲tar命令的基本用法

* 制作gz包

```bash
tar czvf public.tar.gz public
```

* 解压gz包

```bash
tar xzvf public.tar.gz
```

* 查看gz包

```bash
tar tf public.tar.gz
```

* 制作tar包

```bash
# 仅打包不压缩
tar cvf public.tar public
```

* 解压tar包

```bash
tar xvf public.tar
```

* 参数

特别注意，在参数的下达中， c/x/t 仅能存在一个！不可同时存在！因为不可能同时压缩与解压缩。

参数 | 描述
--- | ---
-c | 建立一个压缩档案的参数指令(create 的意思)
-x | 解开一个压缩档案的参数指令！
-t | 查看 tarfile 里面的档案！
-z | 是否同时具有 gzip 的属性？亦即是否需要用 gzip 压缩？
-j | 是否同时具有 bzip2 的属性？亦即是否需要用 bzip2 压缩？
-v | 压缩的过程中显示档案！这个常用，但不建议用在背景执行过程！
-f | 使用档名，请留意，在 f 之后要立即接档名喔！不要再加参数！

## xz压缩包

对于xz这个压缩相信很多人陌生，但xz是绝大数linux默认就带的一个压缩工具，xz格式比 7z 还要小。


* 制作

```bash
# 先创建xxx.tar
tar cvf xxx.tar xxx
# 压缩成xxx.tar.xz 删除原来的tar包
xz xxx.tar
# 将 xxx.tar 压缩成为 xxx.tar.xz 保留原来的tar包
xz -k xxx.tar
```

* 解压

```bash
xz -d ***.tar.xz # 先解压 xz 删除原来的 xz 包
xz -dk ***.tar.xz # 先解压 xz 保留原来的 xz 包
tar -xvf ***.tar # 再解压 tar
```

* 查看

```bash
# 先解压 xz
xz -l ***.tar.xz
```

___
> 共同学习，共同进步