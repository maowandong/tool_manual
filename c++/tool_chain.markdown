
# 编译执行
  c++代码使用g++进行编译， g++ main.cpp -o main, 生成可执行文件main.
  如果住文件main.cpp里面依赖了一些头文件，如下：
  
  main.cpp
  ```javascript {.theme-peacock}
#include<iostream>
#include<new>

#include "test.h"

using namespace std;

int main(void) {
    int sum_all = 0;

    Test * obj_test = new (nothrow)Test();
    obj_test->add(1,2);

    sum_all = obj_test->getSum();

    cout<<"sum: " << sum_all << endl;

    return 0;
}
  ```

依赖的头文件test.h
```
#ifndef TEST_H
#define TEST_H


class Test{
        public:
              int getSum();
              int add(int left, int right);

        private:
            int sum;

};

#endif
```

头文件的部分函数实现在test.cpp中
```
#include "test.h"

int Test::getSum() {
    return sum;
}

int Test::add(int a, int b) {
    sum = a + b;

    return 0;
}
```

此时，如果直接编译g++ main.cpp -o main会提示以下错误:
```
/tmp/ccnR33ly.o: In function `main':
main.cpp:(.text+0x3f): undefined reference to `Test::add(int, int)'
main.cpp:(.text+0x4b): undefined reference to `Test::getSum()'
collect2: error: ld returned 1 exit status
```

显然，是找不到依赖的头文件内容。

因此，需要将依赖的头文件一起编译，g++ main.cpp test.cpp -o main

或者，按照以下查找对应的头文件
1. g++ -c test.cpp -o test.o
2. g++  main.cpp -o main -I ./ ./test.o  



备注：g++编译参数
```
-l

表示：编译程序到系统默认路进搜索，如果找不到，到当前目录，如果当前目录找不到，则到LD_LIBRARY_PATH等环境变量置顶的路进去查找，如果还找不到，那么编译程序提示找不到库。
－L
表示：编译程序按照－L指定的路进去寻找库文件，一般的在-L的后面可以一次用-l指定多个库文件。
－I
表示：编译程序按照-I指定的路进去搜索头文件。
```

在使用-l参数编译时，查询的是库名，如liblua.so是库文件，库名为lua， 通常gcc/g++会到默认的g++安装的相关路径去搜索库，第三方库需要添加指定路径才能被搜索到，需要做如下设置：
```
1. 指定库文件搜索地址：export LD_LIBRARY_PATH=/xxxx/xxxx/lua/lib 或者 export LIBRARY_PATH=/xxxx/xxxx/lua/lib
2. 指定头文件搜索地址：export CPLUS_INCLUDE_PATH=/xxx/xxx/include 或者 export C_INCLUDE_PATH=/xxx/xxx/include
```
然后再进行编译： g++ xxx.cpp -o xxx -llua


