# 安装

[Node](https://nodejs.org/en/)安装，可以直接去官网下载对应系统安装包进行安装。

## ubuntu安装

* 安装

```bash
sudo apt install nodejs
```

* 验证是否安装成功

```bash
sudo node -v
```

## nvm安装

[nvm](https://github.com/nvm-sh/nvm)详细介绍看版本管理工具。

* 安装

```bash
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash
```

* 设置环境变量

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

* 验证是否安装成功

```bash
nvm -v
```

* 安装node

```bash
nvm install node # nvm install 10.16.0
```

## n安装

[n](https://github.com/tj/n)详细介绍看版本管理工具。

* 首先安装npm包管理工具

```bash
sudo apt install npm
```

* 安装

```bash
sudo npm install -g n
```

* 验证是否安装成功

```bash
n -V
```

* 安装node

```bash
n lts # n 10.16.0
```
___
> 共同学习，共同进步