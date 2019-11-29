# 使用systemctl

systemctl 就是 service 和 chkconfig 这两个命令的整合， 在 CentOS 7 就开始被使用了,systemctl是系统服务管理器命令，它实际上将 service 和 chkconfig 这两个命令组合到一起。

任务 | 旧指令 | 新指令
--- | --- | ---
使某服务自动启动 | chkconfig --level 3 httpd on | systemctl enable httpd.service
使某服务不自动启动 | chkconfig --level 3 httpd off | systemctl disable httpd.service
检查服务状态 | service httpd status | systemctl status httpd.service(服务详细信息) systemctl is-active httpd.service(仅显示是否Active)
显示所有已启动的服务 | chkconfig --list | systemctl list-units --type=service
启动某服务 | service httpd start | systemctl start httpd.service
停止某服务 | service httpd stop | systemctl stop httpd.service
重启某服务 | service httpd restart | systemctl restart httpd.service

* 显示系统状态

```bash
systemctl status
```

* 输出激活的单元

```bash
systemctl # systemctl list-units
```

* 输出执行失败的单元

```bash
systemctl --failed
```

> 全部可用的单元文件存放在 /usr/lib/systemd/system/ 和 /etc/systemd/system/ 文件夹（后者优先级更高）。

* 查看全部已安装服务

```bash
systemctl list-unit-files
```

## 使用单元

一个单元配置文件能够描写叙述例如以下内容之中的一个：系统服务（.service）、挂载点（.mount）、sockets（.sockets） 、系统设备（.device）、交换分区（.swap）、文件路径（.path）、启动目标（.target）、由 systemd 管理的计时器（.timer）。

使用 systemctl 控制单元时，通常须要使用单元文件的全名，包括扩展名（比如 sshd.service）。可是有些单元能够在systemctl中使用简写方式。

1. 假设无扩展名，systemctl 默认把扩展名当作 .service。

2. 比如 netcfg 和 netcfg.service 是等价的。

3. 挂载点会自己主动转化为对应的 .mount 单元。比如 /home 等价于 home.mount。
设备会自己主动转化为对应的 .device 单元，所以 /dev/sda2 等价于 dev-sda2.device。

* 激活单元

```bash
systemctl start <单元>
```

* 停止单元

```bash
systemctl stop <单元>
```

* 重新启动单元

```bash
systemctl restart <单元>
```

* 又一次载入配置

```bash
systemctl reload <单元>
```

* 输出单元执行状态

```bash
systemctl status <单元>
```

* 检查单元是否配置自己主动启动

```bash
systemctl is-enabled <单元>
```

* 开机主动激活单元

```bash
systemctl enable <单元>
```

* 取消开机主动激活

```bash
systemctl disable <单元>
```

* 禁用一个单元(禁用后，间接启动也是不可能的)

```bash
systemctl mask <单元>
```

* 取消禁用一个单元

```bash
systemctl unmask <单元>
```

* 显示单元的手冊页（必须由单元文件提供）

```bash
systemctl help <单元>
```

* 又一次载入 systemd，扫描新的或有变动的单元

```bash
systemctl daemon-reload
```

## Firewalld防火墙的设置

从 CentOS7(RHEL7)开始，官方的标准防火墙设置软件从 iptables 变更为 firewalld，相信不少习惯使用iptables 的人会感到十分不习惯，但实际上 firewalld 更为简单易用。

firewalld的基本使用
```
启动： systemctl start firewalld
关闭： systemctl stop firewalld
查看状态： systemctl status firewalld
开机禁用 ： systemctl disable firewalld
开机启用 ： systemctl enable firewalld
```

配置firewall-cmd:
```
显示状态： firewall-cmd --state
查看所有打开的端口： firewall-cmd --zone=public --list-ports
更新防火墙规则： firewall-cmd --reload
```

那怎么开启一个端口呢:
```
firewall-cmd --zone=public --add-port=80/tcp --permanent （–permanent 永久生效，没有此参数重
启后失效）
重新载入:
firewall-cmd --reload 修改 firewall-cmd 配置后必须重启
查看:
firewall-cmd --zone=public --query-port=80/tcp
删除:
firewall-cmd --zone=public --remove-port=80/tcp --permanent
```

## SELinux

安全增强型 Linux（Security-Enhanced Linux）简称 SELinux，它是一个Linux 内核模块，也是 Linux 的一个安全子系统。
SELinux 主要由美国国家安全局开发。2.6 及以上版本的 Linux 内核都已经集成了 SELinux 模块。
SELinux 的结构及配置非常复杂， 而且有大量概念性的东西， 要学精难度较大。 很多 Linux 系统管理员嫌麻烦都把 SELinux关闭了。阿里云安装的 centos 默认已经关闭了。西部数码云服务器默认也是关闭的。

查看 SELinux  状态:
```
1、/usr/sbin/sestatus -v ##如果 SELinux status 参数为 enabled 即为开启状态
SELinux status: enabled
2、getenforce  ##也可以用这个命令检查
```

关闭SELinux：

1、临时关闭（不用重启机器）：
```
setenforce 0 ##设置 SELinux 成为 permissive 模式
setenforce 1 设置 SELinux 成为 enforcing 模式
```

2 、修改配置文件需要重启机器：
修改/etc/selinux/config  文件
`将 SELINUX=enforcing 改为 SELINUX=disabled`

___
> 共同学习，共同进步