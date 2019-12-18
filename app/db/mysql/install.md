# 安装

* 命令

```bash
sudo apt install mysql-server mysql-client
```

* 初始密码

```bash
sudo cat /etc/mysql/debian.cnf
```

* 进入

```bash
mysql -u*** -p***
use mysql;
```

* 修改root密码

```bash
alter user 'root'@'localhost' identified with mysql_native_password by '123456';
```

* 使配置生效

```bash
flush privileges;
```

* 重启mysql服务

```bash
sudo service mysql start
```

___
> 共同学习，共同进步