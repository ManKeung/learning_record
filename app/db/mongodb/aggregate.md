# MongoDB的高级查询aggregate

## MongoDB Aggregation  管道操作符与表达式

管道操作符 | Description
--- | ---
$project | 增加、删除、重命名字段
$match | 条件匹配。只满足条件的文档才能进入下一阶段
$limit | 限制结果的数量
$skip | 跳过文档的数量
$sort | 条件排序。
$group | 条件组合结果 统计
$lookup | $lookup 操作符 用以引入其它集合的数据 （表关联查询）

SQL和NOSQL对比

SQL | NOSQL
--- | ---
WHERE | $match
GROUP BY | $group
HAVING | $match
SELECT | $project
ORDER BY | $sort
LIMIT | $limit
SUM() | $sum
COUNT() | $sum
join | $lookup

## MongoDB Aggregation  管道操作符与表达式

管道操作符 | Description
--- | ---
$project | 增加、删除、重命名字段
$match | 条件匹配。只满足条件的文档才能进入下一阶段
$limit | 限制结果的数量
$skip | 跳过文档的数量
$sort | 条件排序。
$group | 条件组合结果 统计
$lookup | $lookup 操作符 用以引入其它集合的数据 （表关联查询）

SQL和NOSQL对比

SQL | NOSQL
--- | ---
WHERE | $match
GROUP BY | $group
HAVING | $match
SELECT | $project
ORDER BY | $sort
LIMIT | $limit
SUM() | $sum
COUNT() | $sum
join | $lookup

## 数据模拟

```bash
db.order.insert({"order_id":"1","uid":10,"trade_no":"111","all_price":100,"all_num":2})
db.order.insert({"order_id":"2","uid":7,"trade_no":"222","all_price":90,"all_num":2})
db.order.insert({"order_id":"3","uid":9,"trade_no":"333","all_price":20,"all_num":6})
db.order_item.insert({"order_id":"1","title":"商品鼠标 1","price":50,num:1})
db.order_item.insert({"order_id":"1","title":"商品键盘 2","price":50,num:1})
db.order_item.insert({"order_id":"1","title":"商品键盘 3","price":0,num:1})
db.order_item.insert({"order_id":"2","title":"牛奶","price":50,num:1})
db.order_item.insert({"order_id":"2","title":"酸奶","price":40,num:1})
db.order_item.insert({"order_id":"3","title":"矿泉水","price":2,num:5})
db.order_item.insert({"order_id":"3","title":"毛巾","price":10,num:1})
```

## $project

修改文档的结构，可以用来重命名、增加或删除文档中的字段。

* 要求查找 order 只返回文档中 trade_no 和 all_price 字段

```bash
db.order.aggregate([{$project: {trade_no: 1, all_price: 1}}])
```

## $match

用于过滤文档。用法类似于 find() 方法中的参数。

```bash
db.order.aggregate([{$project:{ trade_no: 1, all_price: 1}}, {$match: {all_price: {$gte: 90}}}])
```

# ## $group

将集合中的文档进行分组，可用于统计结果。
统计每个订单的订单数量，按照订单号分组

```bash
db.order_item.aggregate([{$group: {_id: '$order_id', toal: {$sum: '$num'}}}])
```

## $sort

将集合中的文档进行排序。

```bash
db.order.aggregate([{$project: {trade_no: 1, all_price: 1}}, {$match: {all_price: {$gte:90}}}, {$sort: {all_price: -1}}])
```

## $limit

```bash
db.order.aggregate([{$project: {trade_no: 1, all_price: 1}}, {$match: {all_price: {$gte:90}}}, {$sort: {all_price: -1}}, {$limit: 1}])
```

## $skip

```bash
db.order.aggregate([{$project:{ trade_no: 1, all_price: 1}}, {$match: {all_price: {$gte: 90}}}, {$sort: {all_price: -1}}, {$skip: 1}])
```

## $lookup 表关联

```bash
db.order.aggregate([{$lookup: {from: 'order_item', localField: 'order_id', foreignField: 'order_id', as: 'items'}}])
```

```bash
db.order.aggregate([{$lookup: {from: 'order_item', localField: 'order_id', foreignField: 'order_id', as: 'items'}}, {$match:{"all_price":{$gte:90}}}])
```
___
> 共同学习，共同进步