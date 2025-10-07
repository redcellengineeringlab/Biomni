FROM uylulu/biomni_env:latest

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .
ENV PYTHONUNBUFFERED=1

RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
