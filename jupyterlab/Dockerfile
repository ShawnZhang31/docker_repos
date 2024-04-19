# 基础镜像
FROM jupyter/scipy-notebook

# 作为 root 用户执行以下命令
USER root

# 安装一些常用的工具
RUN apt-get update && \
    apt-get -y install curl telnet net-tools iputils-ping bash-completion && \
    rm -rf /var/lib/apt/lists/*  # 删除 apt 缓存文件夹中的所有文件

# 设置时区为上海
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# # 将默认的 Notebook 启动端口改为 8888
EXPOSE 8888

# 给予SUDO权限
ENV GRANT_SUDO=yes
# 设置环境变量，启用jupyterlab
ENV JUPYTER_ENABLE_LAB=yes
# ENV NOTEBOOK_ARGS="--NotebookApp.token='' --NotebookApp.password=''"

USER jovyan

# 启动 JupyterLab，禁用 token
# CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
# ENTRYPOINT ["jupyter",  "server", "--ServerApp.token=''", "--ServerApp.password=''", "--ServerApp.pylab='enable'"]
# 启动命令可参考 https://jupyter-server.readthedocs.io/en/latest/other/full-config.html
ENTRYPOINT ["jupyter",  "server", "--IdentityProvider.token=''", "--ServerApp.default_url='/lab'"]