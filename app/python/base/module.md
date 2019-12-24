# 模块

.py文件就是一个模块,注意命名不要和关键字有冲突

* 导入

```python
import 模块

# 限制模块名字
import 模块 as a

# from
# from 模块 import 子 as a
from 模块 import 子

# 导入所有
# 不建议这样
import *
from 模块 import *
```

* 搜索模块

```python
import random

print(random.__file__)
```

* 模块

```bash
mkdir mk_msg
cd mk_msg
touch __init__.py
touch msg.py
```

```python
msg = 'hello module'

if __name__ == '__main__':
    print(msg)
```

## 发布模块

* 文件目录结构

```
├── mk_msg
│   ├── __init__.py
│   ├── receive_msg.py
│   └── send_msg.py
├── setup.py
```

```python
# setup.py
from distutils.core import setup

setup(
    name='mk_msg',  # 包名
    version='1.0',  # 版本号
    description='mankeung"s 发送和接收消息模块',  # 描述信息
    long_description='完整的发送和接收消息模块',  # 完整描述信息
    author='mankeung',  # 作者
    author_email='mankeung1011@gmail.com',  # 作者邮箱
    url='www.mkimq.com',  # 主页
    py_modules=['mk_msg.send_message', 'mk_msg.receive_message']
)
```

* 构建

```bash
python setup.py build
```

* 发布压缩包

```bash
python setup.py sdist
```

* 安装模块

```bash
tar -zxvf mk_msg-1.0.tar.gz
sudo python setup.py install
```

* 卸载模块

```bash
cd /urs/local/lib/python3.7/dist-packages/
sudo rm -r hm_msg*
```

___
> 共同学习，共同进步