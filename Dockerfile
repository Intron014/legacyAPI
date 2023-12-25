FROM python:latest
LABEL authors="intron014"
LABEL version="1.0.0"
LABEL description="I014 API in a docker container, woah!"

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8004

CMD ["gunicorn", "--bind", "0.0.0.0:8004", "--log-level", "DEBUG", "-w", "4", "main:app"]