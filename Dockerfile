# 基于python镜像 
FROM python

# 设置工作目录
WORKDIR /app

COPY test.py /app/

# 安裝依賴套件
RUN pip install bs4 && pip install requests && pip install lxml && pip install requests_html

# 暴露容器端口
EXPOSE 5000

# 运行app.py 
CMD ["python", "test.py"]