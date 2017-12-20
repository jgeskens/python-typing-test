FROM python:3.6

RUN pip install flake8-mypy==17.8.0

COPY . /app

CMD bash -c 'cd /app && python main.py'
