<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/star.png></a></p>

<p align="center">
    <b>Trino is a fast distributed SQL query engine for big data analytics.</b>
</p>


**1. Add trino reop**:
</br>

```bash
helm repo add trino https://trinodb.github.io/charts
```

**2. Pull template and values**:
</br>

```bash
helm pull trino/trino --untar
```

**3.1 Config heml chart for trino not use ranger**:

- Config trino version use 455 in values.yaml to use s3 file system

```bash
#values.yaml

image:
  #--- 
  tag: "455"
  #--- 
```


- Config trino authen with PASSWORD

```bash
#values.yaml

server:
  #--- 
  config:
    #---
    authenticationType: "PASSWORD"
    #---
  #--- 
```

- Additional config values.yaml

```bash
#values.yaml

additionalConfigProperties:
  - internal-communication.shared-secret=super-secret-communication-shared-secret # Shared secret to authenticate all communication between nodes of the cluster
  - http-server.process-forwarded=true # Needed when Trino cluster is behind a load balancer or proxy server
  - hide-inaccessible-columns=true
```

- Additional config catalog delta with hive-metastore values.yaml


```bash
#values.yaml
additionalCatalogs:
  delta: |-
    connector.name=delta_lake
    hive.metastore.uri=thrift://hive-metastore:9083
    delta.register-table-procedure.enabled=true
    hive.s3.endpoint=https://aaaaa.r2.cloudflarestorage.com
    hive.s3.aws-access-key=aaaaaaaaa
    hive.s3.aws-secret-key=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    hive.s3.path-style-access=true
    hive.s3.ssl.enabled=true
    delta.enable-non-concurrent-writes=true
```

- Config LDAP server for PASSWORD authen:

```bash
./templates/configmap-coordinator.yaml

password-authenticator.properties: |
    # password-authenticator.name=file
    # file.password-file={{ .Values.server.config.path }}/auth/password.db
    password-authenticator.name=ldap
    ldap.url=ldap://openldap:389
    ldap.allow-insecure=true
    ldap.bind-dn=cn=admin,dc=ranger,dc=local
    ldap.user-base-dn=dc=ranger,dc=local
    ldap.bind-password=admin
    # ldap.group-auth-pattern=(&(objectClass=inetOrgPerson)(uid=${USER})(memberof=CN=AuthorizedGroup,OU=Asia,DC=corp,DC=example,DC=com))
    ldap.group-auth-pattern=(&(objectClass=inetOrgPerson)(uid=${USER}))
```

- Deploy trino:

```bash
helm upgrade --install trino ./trino -f ./trino/values.yaml
```
#### Pod
    
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_pod.png></a></p>

#### Service
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_svc.png></a></p>



- Deploy ingress for trino to have tls to auth with password:

```bash
kubectl apply -f ./trino-ingress.yaml
```
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_ingress.png></a></p>

- Trino Cluster Overview:

#### Login

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_ui.png></a></p>

#### Cluster Overview

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_cluster.png></a></p>


- Query data on Trino:

#### Choose Trino connection in DBeaver tool:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_dbeaver_login.png></a></p>

#### Input connection info:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_dbeaver_login2.png></a></p>

#### Query data on delta table:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/trino_query_delta_table.png></a></p>