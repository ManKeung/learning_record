# 包管理工具

本文介绍[npm](https://www.npmjs.com/package/npm)、[yarn](https://www.yarnpkg.com/lang/en/)两个包管理工具

## npm常用命令

* 查看版本信息

```bash
npm -v
```

* 换成淘宝镜像

```bash
npm get registry # 查看
npm config set registry http://registry.npm.taobao.org # 设置
```

* 项目初始化

```bash
npm init # 问答方式生存
npm init -yes # 参数走默认配置
```

生成package.json

package.json

```json
{
  "name": "npm-demo", # 模块名
  "version": "1.0.0",　# 版本
  "description": "npm包管理初始化",　# 描述
  "main": "index.js", # 入口
  "scripts": { # 脚本
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [ # 关键字
    "npm"
  ],
  "author": "mankeung", # 作者
  "license": "ISC"
}

```

* 安装模块

```bash
npm install # 安装项目的全部依赖，package.json　
npm install <Module Name> # install可简写i 默认安装在本地
npm install <Module Name>@<version> # 下载指定版本
npm install <Module Name> -g # 全局安装
npm install <Module Name> --save # 生产　可简写 -S
npm install <Module Name> --save-dev # 开发　可简写 -D
```

* 查看安装信息

```bash
npm list -g # 查看全局安装的模块信息
npm list -g --depth 0 # 查看全局安装模块名
npm list <Module Name> # 查看某个版本号
```

* 更新模块

```bash
npm update <Module Name>
```

* 卸载

```bash
npm uninstall <Module Name> # uninstall可简写u
```

* 运行脚本

```bash
npm run/test
```

## yarn

快速、可靠、安全的依赖管理工具。

### 安装

* npm全局安装

```bash
npm i -g yarn
```

### 常用命令

* 查看版本

```bash
yarn -v
```

* 换成淘宝镜像

```bash
yarn config set registry https://registry.npm.taobao.org
```

* 项目初始化

```bash
yarn init
```

> package.json文件同`npm init`，在此不做过多介绍

* 安装模块

```bash
yarn # 或者　yarn install 安装全部项目依赖
yarn add <Module Nmae>
```

* 更新模块

```bash
yarn upgrade <Module Name>
```

* 卸载

```bash
yarn remove <Module Nmae>
```

* 运行脚本

```bash
yarn run/test
```

> 提示：yarn命令参数可对照npm

___
> 共同学习，共同进步