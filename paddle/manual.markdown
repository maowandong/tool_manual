#安装与使用

paddlepaddle官方建议的安装方式是用[docker安装](http://doc.paddlepaddle.org/doc_cn/getstarted/build_and_install/docker_install_cn.html)，所以需要确保运行环境提前安装好docder。
- 安装docker环境
- 拉取docker镜像文件

```
docker pull paddlepaddle/paddle:0.10.0
```

- 启动paddle

**A.交互方式：**

```
docker run -it --rm paddlepaddle/paddle:0.10.0 /bin/bash

```

**B. 挂载宿主磁盘文件到容器中:**
```
docker run -it -v $PWD:/home/work/paddle paddlepaddle/paddle:0.10.0 /bin/bash

```

$PWD: 宿主文件路径; /home/work/paddle为容器的挂载路径