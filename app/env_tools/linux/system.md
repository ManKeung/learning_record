# 系统命令

## 别名管理

* 添加别名

```bash
alias chttp='cat /etc/httpd/conf/httpd.conf'
```

* 删除别名

```bash
unalias chttp
```

* 查看别名

```bash
alias
```

## 内存、cup管理top命令

```bash
top
```

1. top  命令的第一行：
`top - 15:31:47 up 9:30, 3 users, load average: 0.00, 0.02, 0.05`
依次对应：系统当前时间 up 系统到目前为止运行的时间， 当前登陆系统的用户数量， load average后面的三个数字分别表示距离现在 一分钟，五分钟，十五分钟的负载情况。

2. top命令的第二行：
`Tasks: 133 total, 1 running, 132 sleeping, 0 stopped, 0 zombie`
依次对应：tasks 表示任务（进程），133 total 则表示现在有 133 个进程，其中处于运行中的有 1 个，132 个在休眠（挂起），stopped 状态即停止的进程数为 0，zombie 状态即僵尸的进程数为 0 个。

3. top  命令的第三行，cpu  状态：
`%Cpu(s): 0.2 us, 0.4 sy, 0.0 ni, 99.3 id, 0.0 wa, 0.0 hi, 0.1 si, 0.0 st`
只看空闲就可以了：cpu 空闲率为 99.3%
依次对应：
us:user 用户空间占用 cpu 的百分比
sy:system 内核空间占用 cpu 的百分比
ni:niced 改变过优先级的进程占用 cpu 的百分比
空闲 cpu 百分比
wa:IO wait IO 等待占用 cpu 的百分比
hi:Hardware IRQ 硬中断 占用 cpu 的百分比
si:software 软中断 占用 cpu 的百分比
st:被 hypervisor 偷去的时间

4. top  命令的第四行，内存状态：
`KiB Mem : 2897496 total, 1995628 free, 191852 used, 710016 buff/cache`
总内存:2.76g 空闲： 1995628/1024/1024=1.9g 已经使用 0.18g 缓存区内存 0.67g
缓冲区是从主内存中特地预留出的内存，用来存放特定的一些信息，例如从磁盘中取得的文件表，程序正
在读取的内容等等

5. top  命令第七行，各进程的监控：
`PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND`
依次对应：
PID — 进程 id
USER — 进程所有者
PR — 进程优先级
NI — nice 值。负值表示高优先级，正值表示低优先级
VIRT — 进程使用的虚拟内存总量，单位 kb。VIRT=SWAP+RES
RES — 进程使用的、未被换出的物理内存大小，单位 kb。RES=CODE+DATA
SHR — 共享内存大小，单位 kb
S — — 进程状态。D=不可中断的睡眠状态 R=运行 S=睡眠 T=跟踪/停止 Z=僵尸进程
%CPU — 上次更新到现在的 CPU 时间占用百分比
%MEM — 进程使用的物理内存百分比
TIME+ — 进程使用的 CPU 时间总计，单位 1/100 秒
COMMAND — 进程名称（命令名/命令行）

## 内存、cup 理 管理 uptime命令

```bash
uptime
```

`top - 15:31:47 up 9:30, 3 users, load average: 0.00, 0.02, 0.05`

1. 服务器工作时间
2. 在线用户
3. 平均负载 一分钟，五分钟，十五分钟的负载情况

## 看当前登录的账户 who 、查看最新操作电脑的用户last

who命令:
显示当前正在系统中的所有用户名字，使用终端设备号，注册时间。
whoami:
显示出当前终端上使用的用户。
last:
last 作用是显示近期用户或终端的登录情况

## 进程管理查看、杀死

1. 查看进程
```bash
pstree 查看进程树
pstree -ap 显示所有信息
pstree | grep httpd
pstree -ap | grep httpd
ps -au
ps -au |grep httpd
ps -aux
```
ps中aux 的含义:
显示现行终端机下的所有程序，包括其他用户的程序（a）
以用户为主的格式来显示程序状况。 （x）
显示所有程序，不以终端机来区分（u）

2. 关闭进程
```
pkill httpd // pkill 进程的名字
kill 2245 // kill 进程号
kill -9 1234 // kill -9 进程号 强制杀死
```

kill ：执行 kill 命令，系统会发送一个 SIGTERM 信号给对应的程序。当程序接收到该 signal 信号后，将会发
生以下事情：
程序立刻停止
当程序释放相应资源后再停止
程序可能仍然继续运行
大部分程序接收到 SIGTERM 信号后，会先释放自己的资源，然后再停止。但是也有程序可能接收信号后，
做一些其他的事情（如果程序正在等待 IO，可能就不会立马做出响应，我在使用 wkhtmltopdf 转 pdf 的项
目中遇到这现象），也就是说，SIGTERM 多半是会被阻塞的。

kill -9: kill -9 命令，系统给对应程序发送的信号是 SIGKILL，即 exit。exit 信号不会被系统阻塞，所以 kill -9能顺利杀掉进程。

## 查看端口

```bash
netstat -tunpl | grep httpd
```

1. -t 或--tcp 显示 TCP 传输协议的连线状况。
2. -u 或--udp 显示 UDP 传输协议的连线状况。
3. -n 或--numeric 直接使用 IP 地址，而不通过域名服务器。
4. -p 或--programs 显示正在使用 Socket 的程序识别码和程序名称。
4. -l 或--listening 显示监控中的服务器的 Socket。

关闭防火墙：
```
Firewalld 关闭：systemctl stop firewalld
SELinux 关闭：setenforce 0
```

## 查看硬盘信息

df 命令作用是列出文件系统的整体磁盘空间使用情况。可以用来查看磁盘已被使用多少空间和还剩余多少
空间。

```
df
df -h 以人们易读的方式显示，总共多少g用了多少g
df /home 查看该文件夹所在磁盘的使用情况
```

## which

shows the full path of (shell) commands  ＃从PATH变量所在路径查找二进制命令

```bash
which cat # 示例
```

## in

创建链接

* 创建文件硬链接

```bash
ln oldboy.txt oldboy_hard_link
```

* 创建文件软链接

```bash
ln -s oldboy.txt oldboy_soft_link
```

___
> 共同学习，共同进步