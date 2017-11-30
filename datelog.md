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

##2017-11-22  

1.***用正则表达式替换，将\r\n替换为\n。其中\r指的是CR，\n指的是LF。***  
将CRLF替换成LF格式。git会智能的将这两种格式互换，但是很遗憾这个是有bug的  

##2017-11-23  

1.***fabric需要在python2的环境下运行***  
这是在是个麻烦的点，首先需要将2和3一起公用，先安装3再安装2，依照3配置2的  
环境变量，之后修改python.exe和pythonw.exe的名字，如：python3.exe，pythonw3.exe  
之后还要重新下载pip。在使用时python(2/3)+命令。fab.exe不能在3下面运行，而且  
所以需要如下命令打包：python2 -m fabric build,*不是fab，而是fabric，而且需要切到对应的打包路径！*  

2.***打包时的报错***  
tar: Exiting with failure status due to previous errors

Fatal error: local() encountered an error (return code 2) 
while executing 'tar --dereference -czvf ../dist/dist-awesome.tar.gz --exclude='test' --exclude='.*' --exclude='*.pyc' --exclude='*.pyo' static templates transwarp favicon.ico *.py'

Aborting.

##2017-11-30  

1.***nginx静态资源***  
静态资源403的问题，经常是user nobody导致的，换成root用户。然后需要确定nginx的配置位置  
使用nginx -s stop，nginx -c reload的时候发现读取的是/usr/share/nginx/nginx.conf目录  
但我们的配置放在了/etc/nginx/nginx.conf下，所以做一个软链，再此重启。get。  
给nginx指定配置文件/usr/sbin/nginx -c /etc/nginx/nginx.conf

