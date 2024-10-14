FROM trinodb/trino:436
USER root

COPY install.properties /root/
RUN chmod +x /root/install.properties

COPY ./docker-entrypoint.sh /root/
RUN chmod +x /root/docker-entrypoint.sh

RUN chmod 777 -R /etc/trino/
RUN chmod 777 -R /data/trino/

ENTRYPOINT ["/root/docker-entrypoint.sh"]
