FROM ubuntu:22.04


# 修改时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

# 安装常用的的网络测试工具
RUN apt-get update && \
    apt-get install -y telnet vim wget curl

# 创建工作目录
WORKDIR /code

# 安装Python
COPY Miniconda3-py310_23.10.0-1-Linux-x86_64.sh ./Miniconda3-py310_23.10.0-1-Linux-x86_64.sh


CMD ["/bin/bash"]