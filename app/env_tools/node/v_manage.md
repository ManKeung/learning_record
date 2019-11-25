# 版本管理

对于开发可能我们需要不同的node版本环境，所以需要版本管理器，更好的切换版本。

## nvm

* 安装node版本

```bash
nvm install <version>
```

* 列出可用的版本

```bash
nvm ls-remote
```

* 查看当前版本

```bash
nvm current
```

* 列出安装的node

```bash
nvm ls
```

* node版本切换

```bash
nvm use <version>
```

* 卸载node

```bash
nvm uninstall <version>
```

## n

* 安装node版本

```bash
n stable # 安装稳定的官方版本
n lts # 安装最新的LTS官方版本
n latest # 安装最新的node版本
n <version> # 安装指定node版本
```

* 列出可用的版本

```bash
n ls-remote
```

* 列出安装的node

```bash
n ls
```

* node版本切换

```bash
n # 上下箭头选择，回车切换
```

* 卸载node

```bash
n rm <version> # n - <version> 删除缓存版本
n uninstall <version> # 删除node&npm
n prune # 删除除当前版本外所有其他版本
```
___
> 共同学习，共同进步