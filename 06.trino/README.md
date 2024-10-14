<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/start.png></a></p>

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

- Pod:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap_pod.png></a></p>

- Service:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap_svc.png></a></p>


- LDAP management UI:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap_ui.png></a></p>