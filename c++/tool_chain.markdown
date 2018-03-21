
# 编译执行
  c++代码使用g++进行编译， g++ main.cpp -o main, 生成可执行文件main.
  如果住文件main.cpp里面依赖了一些头文件，如下：
  
  main.cpp
  ```javascript {.theme-peacock}
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


