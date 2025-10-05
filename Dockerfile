FROM uylulu/biomni_env

WORKDIR /app

COPY /app/requirements.txt .

RUN conda install --yes --file requirements.txt

COPY /app .
COPY /biomni /biomni

RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
