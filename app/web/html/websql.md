# Web SQL

Web SQL 数据库可以在最新版的 Safari, Chrome 和 Opera 浏览器中工作。

* 核心方法
    - openDatabase：这个方法使用现有的数据库或者新建的数据库创建一个数据库对象。
    - transaction：这个方法让我们能够控制一个事务，以及基于这种情况执行提交或者回滚。
    - executeSql：这个方法用于执行实际的 SQL 查询。

* 打开数据库

openDatabase() 方法来打开已存在的数据库，如果数据库不存在，则会创建一个新的数据库

```js
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
/* 数据库名称
版本号
描述文本
数据库大小
创建回调 */
// 第五个参数，创建回调会在创建数据库后被调用
```

* 执行查询操作

```js
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
});
```

* 插入数据

```js
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "菜鸟教程")');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "www.runoob.com")');
});
```

* 读取数据

```js
var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);

db.transaction(function (tx) {
   tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "菜鸟教程")');
   tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "www.runoob.com")');
});

db.transaction(function (tx) {
   tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
      var len = results.rows.length, i;
      msg = "<p>查询记录条数: " + len + "</p>";
      document.querySelector('#status').innerHTML +=  msg;

      for (i = 0; i < len; i++){
         alert(results.rows.item(i).log );
      }

   }, null);
});
```

* 删除记录

```js
db.transaction(function (tx) {
    tx.executeSql('DELETE FROM LOGS  WHERE id=1');
});
```

* 更新记录

```js
db.transaction(function (tx) {
    tx.executeSql('UPDATE LOGS SET log=\'www.w3cschool.cc\' WHERE id=2');
});
```

___
> 共同学习，共同进步