# 基本配置

## ubuntu基本命令

* 安装软件

```bash
sudo apt install 软件名
```

* 卸载软件

```bash
sudo apt remove 软件名
```

* 查看更新

```bash
sudo apt update
```

* 更新软件

```bash
sudo apt upgrade
```

* 安装.dep

```bash
sudo dpkg -i 软件名.deb
```

apt 命令 |	取代的命令|	命令的功能
---- | ---- | ----
apt install	| apt-get install |	安装软件包
apt remove	| apt-get remove	| 移除软件包
apt purge	| apt-get purge	| 移除软件包及配置文件
apt update	| apt-get update	| 刷新存储库索引
apt upgrade	| apt-get upgrade	| 升级所有可升级的软件包
apt autoremove	| apt-get autoremove	| 自动删除不需要的包
apt full-upgrade	| apt-get dist-upgrade	| 在升级软件包时自动处理依赖关系
apt search	| apt-cache search	| 搜索应用程序
apt show	| apt-cache show	| 显示装细节

## 切换root

1. 给root设置密码

```bash
sudo passwd root
```

2. 切换root

```bash
su root
```

3. 切换普通用户

```bash
su 用户名
```

## 虚拟机中全屏显示

### 方式一

1、打开虚拟机，并点击要更改成全屏的那个ubuntu系统的电源，我的虚拟机名字就叫ubuntu，那么就点击【打开此虚拟机电源】

2、等虚拟机打开之后，我们点击虚拟机软件上面工具栏中的【虚拟机(V)】，会展现出一个下拉菜单。

3、在下拉菜单中，我们找到并使用鼠标左键单击【安装Vmware工具】，如果你这里是灰色的，那么可能是 因为你的虚拟机版本比较低！

4、点击以上选项后，我们进入到系统里面，找到在桌面上出现的wmware tools的光盘！我们点击进入其中。

5、在vmware tools虚拟光盘里面，我们双击【`vmware****.tar.gz`】这个文件，注意我这里的****是任意字符的意思哦，每个虚拟机的版本可能不一。

6、复制这个【vmware****.tar.gz】文件，到【文件】--->【home】文件夹里面。


7、然后按【Ctrl+Alt+T】调出命令界面，然后在里面输入【tar -zxvf v】后按【Tab】键，自动补全整个工具的名字。然后按enter执行。

8、然后在终端里面

输入【cd V】，再按一次TAB键补全被解压后的那个工具目录名字。回车后进入到该工具解压后的目录里面！最后输入【sudo ./vmware-install.pl】执行即可安装成功，安装成功后，按【CTRL+Alt+enter】键就能给ubuntu全屏啦。如果还有疑问，可以提问我，我会第一时间回答的。

### 方式二

解决ubuntu18黑屏去掉3d勾选，勾选后屏幕不能全屏铺满

１．终端输入

```bash
sudo apt install open-vm-tools
```

2. 安装依赖，这一步很关键，必不可少

```bash
sudo apt install open-vm*
```

3. 重启

```bash
reboot
```

## 安装ssh

便于ssh链接

```bash
sudo apt install openssh-server
```

## 卸载火狐

1. 查找火狐浏览器的安装包内容

```bash
dpkg --get-selections | grep firefox # dpkg --get-selections  | grep 为查找安装包内容的指令，后面加上安装包名称
```

2. 卸载安装小包

```bash
sudo apt-get purge firefox firefox-locale-en firefox-locale-zh-hans unity-scope-firefoxbookmarks # sudo apt-get purge 为卸载安装小包的指令，后面要加上安装小包的名称。
```

## 安装sogo

先安装

```bash
apt --fix-broken install
```

## 解决vscode空格距离极小问题

* firacode字体安装

```bash
sudo apt update # 更新可用软件包列表
sudo apt upgrade # 通过安装/升级软件来更新系统
sudo apt install font-manage # 安装字体管理器　注意有就不用安装
sudo apt install fonts-firacode # 安装firacode字体
sudo apt autoremove # 卸载多余软件包
```

* 更改VScode中的字体设置

在settings.json中添加如下配置

```json
{
    "editor.fontFamily": "Fira Code",
    "editor.fontLigatures": true,
}
```

___
> 共同学习，共同进步