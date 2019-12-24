# python

Python是一种跨平台的计算机程序设计语言。是一种面向对象的动态类型语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。

## 创建虚拟环境

* 安装

```bash
sudo pip3 install virtualenv
```

* 安装虚拟环境扩展包

```bash
sudo pip3 install virtualenvwrapper
```

* 修改用户目录下的.bashrc文件

```
source /usr/local/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export WORKON_HOME=$HOME/.virtualenvs
```

> virtualenvwrapper.sh的信息把python变python3

* 使配置文件生效

```bash
source .bashrc
```

* 创建python虚拟环境

```bash
# mkvirtualenv -p python3 虚拟环境名称
mkvirtualenv -p python3 python3.7
```

* 退出虚拟环境

```bash
deactivate
```

* 查看与使用

```bash
# workon 两次tab键
```

* 删除虚拟环境

```bash
# rmvirtualenv 虚拟环境名称
# 先退出：deactivate
rmvirtualenv python3.7
```

## pip3安装太慢

国内源：
新版ubuntu要求使用https源，要注意。
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/

* 命令

```bash
pip3 install XXX -i https://pypi.tuna.tsinghua.edu.cn/simple
```

* Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)

```bash
mkdir ~/.pip
cd ~/.pip
touch pip.conf
```

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

> 对于比较小的库，可以延时处理
> pip --default-timeout=100 install -U pip
> pip --default-timeout=100 install 第三方库名

### pip安装警告

WARNING: The directory '/home/zhex/.cache/pip/http' or its parent directory is not owned by the curr

```bash
sudo chown -R root /home/$USERNAME/.cache/pip/
sudo chown -R root /home/$USERNAME/.cache/pip/http/
```

___
> 共同学习，共同进步