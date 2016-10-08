# 数据库说明文档-老师用户

<font size = 4>

<p align="right"> 侯禺凡 </p>

## 接口

- createAccount(kwargs)
	- 创建一个老师用户
	- 参数：kwargs是一个字典，其键应当是所有的老师用户数据库字段，值为要设置的值
	- 返回值：返回是否成功创建的布尔值
	- 可能失败的原因：kwargs和数据库字段不完全相等、账户名已经存在或数据不符合要求

- checkAccount(\_account)
	- 检查账户名是否存在
	- 参数：\_account是要检测的账户名
	- 返回值：返回要检测的账户名是否与已有账户名重复

- getData(\_account,\_colomn)
	- 获取一个账户的某个字段信息
	- 参数：\_account是账户名，\_colomn是字段名
	- 返回值：返回的是信息
	- 可能失败的原因：账户名或字段名不存在，返回None

- setData(\_account,\_colomn,\_data)
	- 设置账户信息
	- 参数： \_account是账户名，\_colomn是字段名，\_data是要设置的信息
	- 返回值：是否成功设置的布尔值
	- 可能失败的原因：不允许修改账户名、要修改的字段不存在

## 字段

- account：账户名，字符串
- password：密码，字符串
- realName：真实姓名，字符串
- phone：电话，字符串
- email：邮箱，字符串
- area：负责的区域，字符串
- volunteerList：志愿者编号，列表

</font>