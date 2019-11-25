# 工具包

主要介绍本人在开发中常用工具包

## pm2

[pm2](https://pm2.keymetrics.io/)内建负载均衡（使用Node cluster 集群模块）
后台运行
0秒停机重载
开机自启动脚本
停止不稳定的进程（避免无限循环）
控制台检测
提供远程控制和实时的接口API (允许和PM2进程管理器交互)

### pm2常用命令

* 安装

```bash
npm install -g pm2
```

* 查看版本

```bash
pm2 -v
```

* pm2更新

```bash
pm2 save # 保存当前应用列表
npm install pm2 -g
pm2 update
```

* 单个启动

```bash
pm2 start app.js # 启动
pm2 start app.js -i 4 # 启动４个应用实例，自动负载均衡
pm2 start app.js --name app_name # 指定别名

# 监听文件变化，配合pm2 logs，方便本地开发
pm2 start app.js --watch
```

pm2启动的服务都是在后台运行，如需部署docker上需加--no-daemon参数
，而node默认前台运行，可通过以下方式实现原生支持

```bash
$ pm2 start app.js --no-daemon
# 或
$ nohup node app.js &
```

* 批量启动

新建.json文件如server.json，配置如下：

```json
{
    "apps": [{
        "name": "appA",
        "script": "./appA.js",
        "watch": false
    }, {
        "name": "appB",
        "script": "./appB.js",
        "watch": false
    }]
}
```

在执行

```bash
pm2 start server.json
```

> 批量启动是以restart模式启动，可以多次执行

* 重启

```bash
pm2 restart app_name|app_id  # 重启
pm2 restart all  # 重启所有进程，相当stop+start
pm2 reload all  # 0秒停机重载进程 (用于不间断进程)
```

* 查看

```bash
pm2 list # 查看进程
pm2 logs # 查看日志
pm2 show app_name|app_id # 查看进程详情
pm2 monit  # 查看CPU和内存资源占用
```

* 停止

```bash
pm2 stop app_name|app_id
pm2 stop all  # 停止所有
```

* 删除

```bash
pm2 delete app_name|app_id  # 从列表中删除指定的进程
pm2 delete all # 从列表中删除全部进程
pm2 kill # 杀死守护进程
```

* 开机自动启动

```bash
pm2 startup  # 创建开机自启动命令
pm2 save  # 保存当前应用列表
pm2 resurrect  # 重新加载保存的应用列表
pm2 unstartup  # 移除开机自启动
```

___
> 共同学习，共同进步