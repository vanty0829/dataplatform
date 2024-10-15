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

# -P save to specific dir
RUN    wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.4/jets3t-0.9.4.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-client/3.3.4/hadoop-client-3.3.4.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.3.4/hadoop-common-3.3.4.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar \
    && wget -P /opt/spark/jars/ https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.0/postgresql-42.7.0.jar

    # kafka-clients-2.5.0.jar
    # spark-sql-kafka-0-10_2.12-3.2.1.jar
    # spark-streaming-kafka-0-10-assembly_2.12-3.2.1.jar
    # spark-token-provider-kafka-0-10_2.12-3.1.2.jar

# COPY ./jars/* /opt/spark/jars/

USER spark