# [安装](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

* 导入公钥

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
```

* 创建源列表文件

```bash
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
```

* 更新本地系统软件包数据库

```bash
sudo apt update
```

* 安装mongodb

```bash
sudo apt install -y mongodb-org
```

* 防止版本更新

```bash
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
```

* 启动mongod

```bash
sudo service mongod start
```

* 查看状态

```bash
sudo service mongod status
```

* 停止服务

```bash
sudo service mongod stop
```

* 重启

```bash
sudo serice mongod restart
```

* 使用mongidb

```bash
mongo
```

## 删除

* 关闭服务

```bash
sudo service mongod stop
```

* 删除包

```bash
sudo apt purge mongodb-org*
```

* 删除文件

```bash
sudo rm -fr /var/log/mongodb
sudo rm -fr /var/lib/mongodb
```

___
> 共同学习，共同进步