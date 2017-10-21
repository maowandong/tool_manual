#安装
paddlepaddle官方建议的安装方式是用docker，所以需要确保运行环境提前安装好docder。
- 安装docker环境
- 拉取docker镜像文件

```
docker pull paddlepaddle/paddle:0.10.0
```

- 以交互方式启动paddle

```
docker run -it --rm paddlepaddle/paddle:0.10.0 /bin/bash

```
