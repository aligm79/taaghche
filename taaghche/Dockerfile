FROM docker.arvancloud.ir/python:3.11.1

WORKDIR /taaghche
COPY requirements.txt requirements.txt
RUN pip install --trusted-host https://mirrors.aliyun.com -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
COPY . .


CMD bash -c "python manage.py runserver 0.0.0.0:8000 & celery -A taaghche worker --loglevel=info"