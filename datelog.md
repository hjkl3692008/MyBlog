# GM的bolg
![Title img](./www/static/img/user.png)
##2017-11-02
1.***加强***  
`select * from tb_user_agent`

1. 样式
- 分割
* 继续分割
2.
>引用
>>二级引用  
[baidu](http://www.baidu.com)  
产生分割线


##2017-11-03

1.***插入错误***  
- 在执行 execute 时遇到 IntegrityError: (1062, Duplicate entry for key)问题，分析发现应该是数据库已经存在该数据导致的。但  
email这个字段并不是主键，很奇怪，在此记录下来。
- 找到原因：这个字段是unique键。


##2017-11-06  

1.***建立框架***

2.***建立前端页面***
