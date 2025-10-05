FROM uylulu/biomni_env

WORKDIR /app

COPY requirements.txt .

RUN conda install --yes --file requirements.txt

COPY . .

RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
