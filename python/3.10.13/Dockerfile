FROM python:3.10.13


# 修改时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

# 安装常用的的网络测试工具
RUN apt-get update && \
    apt-get install -y telnet vim wget curl


# 创建工作目录
WORKDIR /code


CMD ["/bin/bash"]




