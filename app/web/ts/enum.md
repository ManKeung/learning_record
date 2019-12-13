# 枚举

* 数字枚举

```ts
// Up使用初始化为 1。 其余的成员会从 1开始自动增长。
// Up不给值　默认就是从０开始
enum Direction {
    Up = 1,
    Down,
    Left,
    Right
}
```

* 字符串枚举

```ts
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT",
}
```

* 异构枚举

```ts
enum BooleanLikeHeterogeneousEnum {
    No = 0,
    Yes = "YES",
}
```
> 不建议，一般枚举数据类型一样

___
> 共同学习，共同进步