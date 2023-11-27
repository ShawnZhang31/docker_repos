FROM centos:latest

#RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /code

RUN rm -rf /etc/yum.repos.d/*

COPY ./Centos-8.repo /etc/yum/repos.d/

RUN dnf clean all && dnf makecache && \
    dnf install -y vim net-tools telnet sqlite gcc clang git tmux curl &&\
    dnf clean all

EXPOSE 8000

# 设置启动命令为一个空数组，稍后会通过 ENTRYPOINT 指定
CMD []

ENTRYPOINT ["sh", "-c", "vim", "test.py"]
