# 安装

```bash
sudo apt-get update
sudo apt-get install redis-server
```

* 启动redis

```bash
redis-server
```

```bash
systemctl start redis
systemctl restart redis
systemctl enable redis
```

* 查看是否启动成功

```bash
redis-cli
```

* redis配置文件

`/etc/redis/`

核心配置选项
绑定ip：如果需要远程访问，可将此⾏注释，或绑定⼀个真实ip
bind 127.0.0.1

端⼝，默认为6379
port 6379

是否以守护进程运⾏

如果以守护进程运⾏，则不会在命令⾏阻塞，类似于服务
如果以⾮守护进程运⾏，则当前终端被阻塞
设置为yes表示守护进程，设置为no表示⾮守护进程
推荐设置为yes
daemonize yes

数据⽂件
dbfilename dump.rdb

数据⽂件存储路径
dir /var/lib/redis

⽇志⽂件
logfile /var/log/redis/redis-server.log

数据库，默认有16个
database 16

主从复制，类似于双机备份。
slaveof

* 查看配置

```bash
# 语法 redis 127.0.0.1:6379> CONFIG GET CONFIG_SETTING_NAME
CONFIG GET * # 查看所有
# CONFIG GET loglevel # 查看 loglevel
```

* 编辑

```bash
# 语法 redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE
redis 127.0.0.1:6379> CONFIG SET loglevel "notice"
```

* 运行测试

```bash
127.0.0.1:6379> ping
PONG
```

* 切换数据库

```bash
# 数据库没有名称，默认有16个，通过0-15来标识，连接redis默认选择第一个数据库
127.0.0.1:6379> select n # 0-15
```

* 清屏

```bash
27.0.0.1:6379> clear
```

___
> 共同学习，共同进步