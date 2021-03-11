# attack-code
自己编写的代码
&
攻击有用的代码

------------



# glibc 切换问题
官网下载源码后编译安装
https://www.gnu.org/software/libc/manual/html_node/Configuring-and-compiling.html

## gcc10编译安装glibc 2.23
    ../glibc-2.20/configure --prefix=/usr --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin --disable-werror
`--disable-werror` 这项是忽略错误

## gcc10编译安装glibc 2.27
    CFLAGS="-g -fcommon -Og" CXXFLAGS="-g -fcommon -Og" ../glibc-2.27/configure --prefix=/glibc/2.27 --with-headers=/usr/include --with-binutils=/usr/bin --disable-werror 

我编译的时候报了重复定义的错误，加`-fcommon` 忽视

## patchelf
github里的项目

`chlibc.sh`大佬写的脚本，方便使用
https://bbs.pediy.com/thread-254868.htm#msg_header_h2_0
