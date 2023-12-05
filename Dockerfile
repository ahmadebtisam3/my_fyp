FROM python:3.10
WORKDIR /usr/src/app
COPY BS0_market_place ./BS0_market_place
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "BS0_market_place/manage.py", "runserver", "0.0.0.0:8000"]

