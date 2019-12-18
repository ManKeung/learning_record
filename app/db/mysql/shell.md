# 基本使用

## 数据库的设计

* 三范式

经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式(Normal Form)
目前有迹可寻的共有8种范式，一般需要遵守3范式即可

1. 第一范式（1NF）：强调的是列的原子性，即列不能够再分成其他几列。

2. 第二范式（2NF）：首先是 1NF，另外包含两部分内容，一是表必须有一个主键；二是没有包含在主键中的列必须完全依赖于主键，而不能只依赖于主键的一部分。

3. 第三范式（3NF）：首先是 2NF，另外非主键列必须直接依赖于主键，不能存在传递依赖。即不能存在：非主键列 A 依赖于非主键列 B，非主键列 B 依赖于主键的情况。

## 数据库的操作

* 链接数据库

```bash
# 方式一
mysql -uroot -p
# 方式二
mysql -uroot -p123456
```

* 退出数据库

```bash
exit/quit/ctrl+d
```

* 显示数据库版本

```sql
select version();
```

* 显示时间

```sql
select now();
```

* 查看所有数据库

```sql
show databases;
```

* 创建数据库

```sql
create database mktest charset=utf8;
```

* 查看创建数据库

```sql
show create database mktest;
```

* 使用数据库

```sql
use mktest;
```

* 删除数据库

```sql
drop database mktest;
```

## 数据完整性

### 数据类型

* 数值型

类型 | 大小 | 范围(有符号) | 用途
--- | --- | --- | ---
TINYINT |1字节 | (-128，127) | 小整数值
SMALLINT | 2字节 (-32768，32767) | 大整数值
MEDIUMINT | 3字节 | (-8388608，8388607) | 大整数值
INT或INTEGER | 4字节 | (-2147483648，2147483 647) | 大整数值
BIGINT | 8字节 | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807) | 极大整数值
FLOAT | 4字节 (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 单精度浮点数值
DOUBLE | 8字节 | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) 双精度浮点数值
DECIMAL | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 小数值

* 日期和时间类型

类型 | 大小(字节) | 范围 | 格式 | 用途
--- | --- | --- | --- | ---
DATE | 3 | 1000-01-01/9999-12-31 | YYYY-MM-DD | 日期值
TIME | 3 | '-838:59:59'/'838:59:59' | HH:MM:SS | 时间值或持续时间
YEAR | 1 | 1901/2155 | YYYY | 年份值
DATETIME | 8 | 1000-01-01 00:00:00/9999-12-31 23:59:59 | YYYY-MM-DD HH:MM:SS | 混合日期和时间值
TIMESTAMP | 4 | 1970-01-01 00:00:00/2038 结束时间是第 2147483647 秒，北京时间 2038-1-19 11:14:07，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS | 混合日期和时间值，时间戳

* 字符串


类型 | 大小 | 用途
CHAR | 0-255字节 | 定长字符串
VARCHAR | 0-65535字节 | 变长字符串
TINYBLOB | 0-255字节 | 不超过 255 个字符的二进制字符串
TINYTEXT | 0-255字节 | 短文本字符串
BLOB | 0-65535字节 | 二进制形式的长文本数据
TEXT | 0-65535字节 | 长文本数据
MEDIUMBLOB | 0-16777215字节 | 二进制形式的中等长度文本数据
MEDIUMTEXT | 0-16777215字节 | 中等长度文本数据
LONGBLOB | 0-4294967295字节 | 二进制形式的极大文本数据
LONGTEXT | 0-4294967295字节 | 极大文本数据

### 约束

* 主键primary key：物理上存储的顺序
* 非空not null：此字段不允许填写空值
* 惟一unique：此字段的值不允许重复
* 默认default：当不填写此值时会使用默认值，如果填写时以填写为准
* 外键foreign key：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，如果存在则填写成功，如果不存在则填写失败并抛出异常

> 说明：虽然外键约束可以保证数据的有效性，但是在进行数据的crud（增加、修改、删除、查询）时，都会降低数据库的性能，所以不推荐使用，那么数据的有效性怎么保证呢？答：可以在逻辑层进行控制

## 数据表的操作

* 查看当前数据库中的所有表

```sql
show tables;
```

* 创建表

```sql
create table xxxx(id int, name varchar(30));
create table yyyyy(id int primary key not null auto_increment, name varchar(30));
    create table zzzzz(
        id int primary key not null auto_increment,
        name varchar(30)
    );
```

* 查看表结构

```sql
desc xxxx;
```

* 查看表创建语句

```sql
show create table xxxx;
```

* 修改表添加字段

```sql
-- alter table 表名 add 列名 类型;
alter table xxxx add createtime datetime;
```

* 修改表修改字段-不重命名

```sql
-- alter table 表名 modify 列名 类型及约束;
alter table xxxx modify createtime date;
```

* 修改表修改字段-重命名

```sql
-- alter table 表名 change 原名 新名 类型及约束;
alter table xxxx change createtime addtime data default '2019-12-17';
```

* 修改表删除字段

```sql
-- alter table 表名 drop 列名;
alter table students drop high;
```

* 删除表

```sql
drop table xxxx;
```

## 增删改查(curd)

### 增加

```sql
-- 全列插入
-- insert into 表名 values(...)
-- 主键字段 可以用 0  null   default 来占位
-- 枚举中 的 下标从1 开始 1---“男” 2--->"女"....
insert into students values(0, "小李飞刀", 20, "女", 1, "1990-01-01");
insert into students values(null, "小李飞刀", 20, "女", 1, "1990-01-01");
insert into students values(default, "小李飞刀", 20, "女", 1, "1990-01-01");
```

```sql
-- 部分插入
-- insert into 表名(列1,...) values(值1,...)
insert into students (name, gender) values ("小乔", 2);
```

```sql
-- 多行插入
insert into students (name, gender) values ("大乔", 2),("貂蝉", 2);
insert into students values(default, "西施", 20, "女", 1, "1990-01-01"), (default, "王昭君", 20, "女", 1, "1990-01-01");
```

### 修改

```sql
-- update 表名 set 列1=值1,列2=值2... where 条件;
update students set gender=1; -- 全部都改
update students set gender=1 where name="小李飞刀"; -- 只要name是小李飞刀的 全部的修改
update students set gender=1 where id=3; -- 只要id为3的 进行修改
update students set gender=1 where id=3; -- 只要id为3的 进行修改
```
### 删除

```sql
-- 物理删除
-- delete from 表名 where 条件
delete from students; -- 整个数据表中的所有数据全部删除
delete from students where name="小李飞刀";
```
```sql
-- 逻辑删除
-- 用一个字段来表示 这条信息是否已经不能再使用了
-- 给students表添加一个is_delete字段 bit 类型
alter table students add is_delete bit default 0;
update students set is_delete=1 where id=6;
```

### 查询

* 查询所有字段

```sql
select * from students;
```

* 查询指定字段

```sql
select name, age from students;
```

* 使用as给字段起别名

```sql
select name as '姓名', age as '年龄' from students;
```

* 表名加字段查询

```sql
select students.name, students.age from students;
-- 通过 as 给表起别名
select s.name, s.age from students as s;
```

* 消除重复行

```sql
select distinct gender from students;
```

* 比较运算符查询(> >= < <= = != <>)

```sql
select * from students where age > 18;
```

* 逻辑运算符

```sql
-- and
select * from students where age>18 and age<28;
-- select * from students where age>18 and gender="女";
```

```sql
select * from students where age>18 or height>=180;
```

```sql
select * from students where not (age>18 and gender=2);
```

* 模糊查询

```sql
-- like
-- % 替换1个或者多个
-- _ 替换1个
select name from students where name like "小%";
select name from students where name like "__"; -- 查询有2个字的名字

-- 查询姓名中 有 "小" 所有的名字
select name from students where name like "%小%";

-- 查询姓名中 有 "小" 所有的名字
select name from students where name like "%小%";

-- rlike 正则
-- 查询以 周开始的姓名
select name from students where name rlike "^周.*";

-- 查询以 周开始、伦结尾的姓名
select name from students where name rlike "^周.*伦$";
```

* 范围查询

```sql
-- in (1, 3, 8)表示在一个非连续的范围内
-- 查询 年龄为18、34的姓名
select name,age from students where age in (12, 18, 34);

-- not in 不非连续的范围之内
select name,age from students where age not in (12, 18, 34);

-- between ... and ...表示在一个连续的范围内
select name, age from students where age between 18 and 34;

-- not between ... and ...表示不在一个连续的范围内
select * from students where age not between 18 and 34;
```

* 空判断

```sql
-- 判空is null
select * from students where height is null;

-- 判非空is not null
select * from students where height is not null;
```

* 排序

```sql
-- order by 字段
-- asc从小到大排列，即升序
-- desc从大到小排序，即降序
select * from students where (age between 18 and 34) and gender=1 order by age asc;

-- order by 多个字段
select * from students where (age between 18 and 34) and gender=2 order by height desc,age asc,id desc;
```

* 聚合函数

```sql
-- 总数
-- count
select count(*) as 男性人数 from students where gender=1;
select count(*) as 女性人数 from students where gender=2;
```

```sql
-- 最大值
-- max

-- 最小值
-- min

select max(age) from students;

-- 查询女性的最高 身高
select max(height) from students where gender=2;
```

```sql
-- 求和
-- sum
select sum(age) from students;
```

```sql
-- avg
-- 计算平均年龄
select avg(age) from students;

-- 计算平均年龄 sum(age)/count(*)
select sum(age)/count(*) from students;
```

```sql
-- 四舍五入 round(123.23 , 1) 保留1位小数
-- 计算所有人的平均年龄，保留2位小数
select round(sum(age)/count(*), 2) from students;

-- 计算男性的平均身高 保留2位小数
select round(avg(height), 2) from students where gender=1;
```

* 分组

```sql
select gender from students group by gender;

-- 计算每种性别中的人数
select gender,count(*) from students group by gender;

-- 计算男性的人数
select gender,count(*) from students where gender=1 group by gender;
```

```sql
-- group_concat(...)
-- 查询同种性别中的姓名
select gender,group_concat(name) from students where gender=1 group by gender;
select gender,group_concat(name, age, id) from students where gender=1 group by gender;
select gender,group_concat(name, "_", age, " ", id) from students where gender=1 group by gender;
```

```sql
-- having
-- 查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
select gender, group_concat(name),avg(age) from students group by gender having avg(age)>30;

-- 查询每种性别中的人数多于2个的信息
select gender, group_concat(name) from students group by gender having count(*)>2;
```

* 分页

```sql
-- limit start, count
-- 限制查询出来的数据个数
select * from students where gender=1 limit 2;

-- 查询前5个数据
select * from students limit 0, 5;
```

* 连接查询

```sql
-- inner join ... on

-- 查询 有能够对应班级的学生以及班级信息
select * from students inner join classes on students.cls_id=classes.id;

-- 按照要求显示姓名、班级
select students.*, classes.name from students inner join classes on students.cls_id=classes.id;
select students.name, classes.name from students inner join classes on students.cls_id=classes.id;

-- 给数据表起名字
select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;

-- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;

-- 在以上的查询中，将班级姓名显示在第1列
select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id;

-- 查询 有能够对应班级的学生以及班级信息, 按照班级进行排序
-- select c.xxx s.xxx from student as s inner join clssses as c on .... order by ....;
select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name;

-- 当时同一个班级的时候，按照学生的id进行从小到大排序
select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name,s.id;

-- left join
-- 查询每位学生对应的班级信息
select * from students as s left join classes as c on s.cls_id=c.id;

-- 查询没有对应班级信息的学生
-- select ... from xxx as s left join xxx as c on..... where .....
-- select ... from xxx as s left join xxx as c on..... having .....
select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;
select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;

-- right join   on
-- 将数据表名字互换位置，用left join完成
```

* 自关联

```sql
-- 查询所有省份
select * from areas where pid is null;

-- 查询出山东省有哪些市
select * from areas as province inner join areas as city on city.pid=province.aid having province.atitle="山东省";
select province.atitle, city.atitle from areas as province inner join areas as city on city.pid=province.aid having province.atitle="山东省";

-- 查询出青岛市有哪些县城
select province.atitle, city.atitle from areas as province inner join areas as city on city.pid=province.aid having province.atitle="青岛市";
select * from areas where pid=(select aid from areas where atitle="青岛市")
```

* 子查询

```sql
-- 标量子查询
-- 查询出高于平均身高的信息

-- 查询最高的男生信息
select * from students where height = 188;
select * from students where height = (select max(height) from students);

-- 列级子查询
-- 查询学生的班级号能够对应的学生信息
-- select * from students where cls_id in (select id from classes);
```

## 视图

对于复杂的查询，往往是有多个数据表进行关联查询而得到，如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同，则需要在多个地方进行修改，维护起来非常麻烦

> 解决办法：定义视图

* 视图是什么

通俗的讲，视图就是一条SELECT语句执行后返回的结果集。所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。

视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；

方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性；

* 定义视图

```sql
-- 建议以v_开头
create view 视图名称 as select语句;
```

* 查看视图

```sql
show tables;
```

* 使用视图

```sql
select * from v_stu_score;
```

* 删除视图

```sql
drop view 视图名称;
```

* 视图的作用
    1. 提高了重用性，就像一个函数
    2. 对数据库重构，却不影响程序的运行
    3. 提高了安全性能，可以对不同的用户
    4. 让数据更加清晰

## 事务

* 为什么要有事务

事务广泛的运用于订单系统、银行系统等多种场景

正常的流程走下来，A账户扣了500，B账户加了500，皆大欢喜。

那如果A账户扣了钱之后，系统出故障了呢？A白白损失了500，而B也没有收到本该属于他的500。

以上的案例中，隐藏着一个前提条件：A扣钱和B加钱，要么同时成功，要么同时失败。事务的需求就在于此

所谓事务,它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。

例如，银行转帐工作：从一个帐号扣款并使另一个帐号增款，这两个操作要么都执行，要么都不执行。所以，应该把他们看成一个事务。事务是数据库维护数据一致性的单位，在每个事务结束时，都能保持数据一致性

### 事务四大特性(简称ACID)

* 原子性（atomicity）
> 一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作，这就是事务的原子性

* 一致性（consistency）
> 数据库总是从一个一致性的状态转换到另一个一致性的状态。（在前面的例子中，一致性确保了，即使在执行第三、四条语句之间时系统崩溃，支票账户中也不会损失200美元，因为事务最终没有提交，所以事务中所做的修改也不会保存到数据库中。）

* 隔离性（isolation）
> 通常来说，一个事务所做的修改在最终提交以前，对其他事务是不可见的。（在前面的例子中，当执行完第三条语句、第四条语句还未开始时，此时有另外的一个账户汇总程序开始运行，则其看到支票帐户的余额并没有被减去200美元。）

* 持久性（durability）
> 一旦事务提交，则其所做的修改会永久保存到数据库。（此时即使系统崩溃，修改的数据也不会丢失。）

### 事务命令

表的引擎类型必须是innodb类型才可以使用事务，这是mysql表的默认引擎

```sql
-- 查看表的创建语句，可以看到engine=innodb
-- 选择数据库
use jing_dong;
-- 查看goods表
show create table goods;
```

* 开启事务

```sql
begin;
-- 或者
-- start transaction;
```

* 提交事务

```sql
commit;
```

* 回滚事务

```sql
rollback;
```

## 索引

一般的应用系统对比数据库的读写比例在10:1左右(即有10次查询操作时有1次写的操作)，而且插入操作和更新操作很少出现性能问题，遇到最多、最容易出问题还是一些复杂的查询操作，所以查询语句的优化显然是重中之重

* 解决办法

当数据库中数据量很大时，查找数据会变得很慢
> 优化方案：索引

* 索引是什么

索引是一种特殊的文件(InnoDB数据表上的索引是表空间的一个组成部分)，它们包含着对数据表里所有记录的引用指针。

更通俗的说，数据库索引好比是一本书前面的目录，能加快数据库的查询速度

* 索引目的

索引的目的在于提高查询效率，可以类比字典，如果要查“mysql”这个单词，我们肯定需要定位到m字母，然后从下往下找到y字母，再找到剩下的sql。如果没有索引，那么你可能需要把所有单词看一遍才能找到你想要的，如果我想找到m开头的单词呢？或者ze开头的单词呢？是不是觉得如果没有索引，这个事情根本无法完成？

* 索引原理

除了词典，生活中随处可见索引的例子，如火车站的车次表、图书的目录等。它们的原理都是一样的，通过不断的缩小想要获得数据的范围来筛选出最终想要的结果，同时把随机的事件变成顺序的事件，也就是我们总是通过同一种查找方式来锁定数据。

数据库也是一样，但显然要复杂许多，因为不仅面临着等值查询，还有范围查询(>、<、between、in)、模糊查询(like)、并集查询(or)等等。数据库应该选择怎么样的方式来应对所有的问题呢？我们回想字典的例子，能不能把数据分成段，然后分段查询呢？最简单的如果1000条数据，1到100分成第一段，101到200分成第二段，201到300分成第三段……这样查第250条数据，只要找第三段就可以了，一下子去除了90%的无效数据。

### 使用索引

* 查看索引

```sql
show index from 表名;
```

* 创建索引

```sql
-- 如果指定字段是字符串，需要指定长度，建议长度与定义字段时的长度一致
-- 字段类型如果不是字符串，可以不填写长度部分
create index 索引名称 on 表名(字段名称(长度))
```

* 删除索引

```sql
drop index 索引名称 on 表名;
```

> 要注意的是，建立太多的索引将会影响更新和插入的速度，因为它需要同样更新每个索引文件。对于一个经常需要更新和插入的表格，就没有必要为一个很少使用的where字句单独建立索引了，对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。

> 建立索引会占用磁盘空间

## 账户管理

### 授予权限

* 查看所有用户

```sql
-- 查看user表结构
use mysql;
desc user;
```

```sql
-- 查看所有用户
select host,user,authentication_string from user;
```

* 创建账户/授权

需要使用实例级账户登录后操作，以root为例
常用权限主要包括：create、alter、drop、insert、update、delete、select
如果分配所有权限，可以使用all privileges

```sql
-- grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';
```

```sql
-- 查看用户有哪些权限
show grants for laowang@localhost;
```

### 账户操作

* 修改权限

```sql
grant 权限名称 on 数据库 to 账户@主机 with grant option;
```

* 修改密码

```sql
update user set authentication_string=password('123') where user='laowang';
```

* 远程登录

修改 /etc/mysql/mysql.conf.d/mysqld.cnf 文件

```
bind-address = 127.0.0.1 # 注释掉 或者修改成 0.0.0.0
```

最后重启mysql

```bash
sudo service mysql restart
```

* 删除账户

```sql
-- drop user '用户名'@'主机';
drop user 'laowang'@'%';

-- delete from user where user='用户名';
-- 操作结束之后需要刷新权限
-- flush privileges
```

> 注意修改完成后需要刷新权限 `flush privileges`


## 备份与恢复数据库

* 备份

```bash
mysqldump -uroot -p 数据库名 > mktest.sql
# 按提示输入mysql的密码
```

* 恢复

连接mysql，创建新的数据库
退出连接，执行如下命令

```bash
mysql -uroot –p 新数据库名 < python.sql
# 按提示输入mysql的密码
```

* 导入sql文件

```sql
source /home/test.sql
```
___
> 共同学习，共同进步