FROM spark:3.5.0

USER root

RUN apt -y update \
&& apt -y install postgresql postgresql-contrib \
&& apt-get install -y libpq-dev

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean && rm requirements.txt

ENV SPARK_HOME="/opt/spark"



WORKDIR /
COPY ./spark-apps /opt/spark-apps
COPY ./spark-config/spark-defaults.conf /opt/spark/conf/
COPY ./spark-config/hive-site.xml /opt/spark/conf/

# RUN wget ./jars/ https://repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.9.3/antlr4-runtime-4.9.3.jar
# COPY ./jars/* /opt/spark/jars/



USER spark