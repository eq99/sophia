FROM python:3.8

WORKDIR /sophia/api/

COPY requirements.txt .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]
