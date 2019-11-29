# 用户管理

Linux系统同时可以支持多个用户，每个用户对自己的文件设备有特殊的权利，能够保证用户之间互不干扰。就像手机开了助手一样，同时登陆多个 qq 账号，当硬件配置非常高时，每个用户还可以同时执行多个任务，多个线程同时工作，提高效率。多用户是Linux优于其他操作系统的一大特点。

* 添加用户

```bash
useradd lisi
```

* 设置密码

```bash
passwd lisi
```

* 删除用户

```bash
userdel -r lisi
```

> -r：递归的删除目录下面文件以及子目录下文件。
> 备注：删除用户的时候用户组被删除

* 查看用户

```bash
id lisi
```

* 把用户加入组

```bash
gpasswd -a lisi root
```
> 把用户lisi加入到root组，加入组后lisi获取到user组及root组所有权限

* 移除组

```bash
gpasswd -d lisi root
```

## 用户权限　用户分类

网站发布到 linux 服务器下面一般要设置权限，不然的话可能没法上传图片，或者没法写入文件。Windows 中权限没有那么明显可以含糊的过去，linux 里面对权限管控非常严格。

用户权限:

```
drwxr-x---. 2 root root 6 4 月 11 2018 mnt
d 表示目录
rwx root 对 mnt 目录具有读、写和执行的权限
r-x root 组内其他用户对mnt目录具有读和执行权限
--- other 其他所有用户对mnt目录没有任何权限
. 表示 ACL 的属性
2 mnt 里面的目录数量
root 当前目录所属用户
root 当前目录所属组
6 文件文件大小(以字节为单位) 这个字段表示文件大小,如果是一个文件夹,则表示该
文件夹的大小.请注意是文件夹本身的大小,而不是文件夹以及它下面的文件的总大小!很多
人不能理解文件夹是一个特殊的文件的含义,这样的话理解文件夹大小的含义就比较困难了.
4 月 文件创建月份
11 2018 文件创建时间
mnt 目录名称
```

权限：就是人对文件所拥有权限，权限就是是哪个 读、写、执行
用户群体：所有者user u 、所属组 group g 、其他用户 other o 、所有用户 all a

权限:
```
r 读
w 写
x 执行
```

用户:
```
所有者 user u
所属组 group g
其他用户 other o
所有用户 all a u+g+o=a(表示所有人)
```

目录的 rwx
```
r 查看目录里面的文件(4)
w 在目录里创建或删除文件(2)
x 切换进目录(1)
```

文件的 rwx
```
r 查看文件内容
w 在文件里写内容
x 执行该文件(文件不是普通文件，是程序或脚本)
```

## chmod权限分配

* + 增加权限 - 删除权限

```bash
chmod u+x my.sh 给当前用户分配执行 my.sh 的权限
chmod o+r,o+w file.txt 给其他用户分配对 file.txt 的读写权限
chmod o+r,o+w,o+x mnt 给所有其他用户分配对 mnt 目录的进入、读取、写入权限
chmod -R o+r,o+w,o+x mnt 修改目录下的所有文件的权限为可读、可修改、可执行
chmod 755 file
chmod -R 777 wwwroot/ 修改目录下的所有文件的权限为可读、可修改、可执行
755 表示-rwxr-xr-x
```

## 用户权限管理ACL

用户权限管理 ACL
```
-m 修改
[root@localhost /]# setfacl -m u:zhangsan:rx opt/
[root@localhost /]# setfacl -m u:lisi:rwx opt/
1. 查看 opt  拥有的 acl  权限
getfacl opt
2. 设置 opt 的 的 acl  权限
setfacl -m u:zhangsan:rwx opt
3. 删除 opt 的 的 user1  拥有的 acl  权限
setfacl -x u:zhangsan opt -x 删除权限
4. 删除 opt  上所设置过的所有 acl  权限
setfacl -b opt/
```

## 用户权限管理visudo

which 命令
`which useradd`

sbin 下面的命令执行权
```
1. 设置
输入： visudo
编辑 %zhangsan localhost=/usr/sbin/useradd
%zhangsan localhost=/usr/sbin/userdel
2. 使用 普通用户家 sudo
sudo useradd wangwu
sudo userdel wangwu
```
___
> 共同学习，共同进步