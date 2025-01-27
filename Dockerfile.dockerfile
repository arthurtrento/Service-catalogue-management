##############BUILDER stage
FROM python:3-slim as builder

RUN apt-get -y update && apt-get -y install python3-dev default-libmysqlclient-dev build-essential && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

RUN addgroup --gid 1000 catalogo-glpi && adduser --gid 1000 --uid 1000 --home /opt/catalogo-glpi --no-create-home catalogo-glpi && mkdir -p /opt/catalogo-glpi && chown -R catalogo-glpi:catalogo-glpi /opt/catalogo-glpi

USER catalogo-glpi

WORKDIR /opt/catalogo-glpi

COPY requirements.txt requirements.txt
RUN python3 -m pip install --user --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .


############FINAL STAGE
FROM python:3-slim

RUN addgroup --gid 1000 catalogo-glpi && adduser --gid 1000 --uid 1000 --home /opt/catalogo-glpi --no-create-home catalogo-glpi && mkdir -p /opt/catalogo-glpi && chown -R catalogo-glpi:catalogo-glpi /opt/catalogo-glpi

USER catalogo-glpi

WORKDIR /opt/catalogo-glpi

COPY --from=builder /opt/catalogo-glpi .

USER root

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install default-libmysqlclient-dev && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

USER catalogo-glpi

EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]