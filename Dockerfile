FROM python:3.10-slim

WORKDIR /code
COPY requrements.txt .
RUN pip install -r requrements.txt
COPY app.py .
COPY data data
COPY constants.py .
COPY utils.py .
COPY models.py .

CMD python -m gunicorn app:app -b 0.0.0.0:8080 -w 4
