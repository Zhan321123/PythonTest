<h1 style="text-align: center;">MySQL</h1>
<hr>

```
MySQL 服务器
├── Databases（数据库）
│   ├── Tables（表）
│   │   ├── Rows（行）
│   │   └── Columns（列）
│   └── ...
├── Users（用户）
│   └── Roles（角色）
└── Privileges（权限）
```

### 初始化

#### 初始化数据库
- show databases 获取所有数据库
- create database [databaseName] 创建数据库databaseName
- show tables 获取所有表
- use [databaseName] 使用databaseName数据库
- show grants 查看权限
- grant [privilege] on [databaseName].[tableName] to [userName]@[hostName] 授予用户userName权限
- revoke [privilege] on [databaseName].[tableName] from [userName]@[hostName] 撤销用户userName权限
- flush privileges 刷新权限
#### 初始化用户
- create user [userName]@[hostName] identified by [password] 创建用户userName，密码为password，允许连接的host为hostName
- select * from mysql.user 获取所有用户
- set password for [userName] = [password] 修改用户userName的密码为password
- drop user [userName]@[hostName] 删除用户userName
#### 初始化角色
- create role [roleName] 创建角色roleName
- grant all on *.* to [userName]@[hostName] 授予用户userName所有权限
- grant [roleName] to [userName]@[hostName] 授予用户userName角色roleName
- set default role all to [userName]@[hostName] 激活角色roleName
- drop user [userName]@[hostName] 删除用户userName

#### 表操作
- create table [tableName] ([columnName] [columnType] [TypeConstraints],) 创建tableName表，有columnNames列，各个列属性为columnType，其他限制为TypeConstraints
- drop table [tableName] 删除tableName表
- alter table [tableName] rename [newTableName] 重命名tableName表为newTableName

#### 查询表
- select * from [tableName] 获取tableName表所有行数据

#### 列操作
- alter table [tableName] add [columnName] [columnType] [columnOption] [position]在tableName表最后添加一列columnName
  [position]
  - 不填 默认在表最后添加
  - first 在表开头添加
  - after [columnName] 在columnName列之后添加
- alter table [tableName] modify [columnName] [columnType] [TypeConstraints] 修改表某列的类型
- alter table [tableName] change [oldColumnName] [newColumnName] [columnType] [TypeConstraints] 修改表某列的名称和类型
- alter table [tableName] drop [columnName] 删除表某列

- alter table [tableName] add constraint [constraintName] [constraintType] [constraintOption] 添加约束
- alter table [tableName] modify [columnName] [columnType] [TypeConstraints] 修改表某列的类型

#### 行操作
- insert into [tableName] values ([value1], [value2], ...) 插入一行数据
- insert into [tableName] values (...),(...),... 批量插入多行数据
- insert into [tableName] ([columnName1], [columnName2], ...) values ([value1], [value2], ...) 指定列插入一行数据
- update [tableName] set [columnName1] = [value1] where [condition] 修改行数据
- delete from [tableName] 删除所有行数据
- delete from [tableName] where [condition] 删除行数据
- constraint 

#### conditions
- [columnName] =><! [value]
- and、or、

#### 类型
- int(11) 整数
- double(x,y) 浮点数，x为整数部分长度，y为小数部分长度
- varchar(n) 字符串，字符长度范围0-n
- char(n) 字符串，字符长度固定为n，不足时填充空格
- date 日期，格式为 yyyy-mm-dd、yyyy/mm/dd、yyyy.mm.dd
  - now() 当前日期

#### 内联TypeConstraints
- not null 非空
- auto_increment 自增
- primary key 主键
- default [value] 默认值
- unique 唯一
- check [condition] 检查

#### 命名TypeConstraints
- 约束位置
  ```
  create table [tableName] (
    sno int auto_increment,
    ...,
  
    constraint [constraintName] [constraintType],
  )
  ```
- 约束
  - constraint [pk_tableName_columnName] primary key [columnName] 主键约束
  - constraint [ck_tableName_columnName] check [condition] 检查约束
  - constraint [uk_tableName_columnName] unique [columnName] 唯一约束
  
  - constraint [fk_tableName_columnName] foreign key [columnName] references [referencedTableName] ([referencedColumnName]) 外键约束
- 删除一条命名约束
  - alter table [tableName] drop constraint [constraintName]

#### 复制表