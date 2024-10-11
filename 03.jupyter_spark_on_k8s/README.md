<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/jupyter.png></a></p>

**1. Pull helm airflow**:
</br>
```bash
helm repo add apache-airflow https://airflow.apache.org
helm repo update
```

**2. Get values file**:
</br>
```bash
helm show values apache-airflow/airflow > ./values.yaml
```

**3. Adjust values.yaml to mount dags folder**:
</br>
```bash
dags:
  # Where dags volume will be mounted. Works for both persistence and gitSync.
  # If not specified, dags mount path will be set to $AIRFLOW_HOME/dags
  mountPath: ~
  persistence:
    # Annotations for dags PVC
    annotations: {}
    # Enable persistent volume for storing dags
    enabled: true
    # Volume size for dags
    size: 1Gi
    # If using a custom storageClass, pass name here
    storageClassName: nfs
    # access mode of the persistent volume
    accessMode: ReadWriteMany
    ## the name of an existing PVC to use
    existingClaim:
    ## optional subpath for dag volume mount
    subPath: ~
```


**4. Deploy airflow**:
</br>
```bash
helm upgrade --install airflow apache-airflow/airflow -f ./values.yaml
```
<p>Pod</p>
<p align="center"><img alt="airflow_pod" src=https://github.com/vanty0829/dataplatform/blob/master/99.images/airflow_pod.png></a></p>

<p>Service</p>
<p align="center"><img alt="airflow_svc" src=https://github.com/vanty0829/dataplatform/blob/master/99.images/airflow_svc.png></a></p>

**5. Check UI**:
- Forward Port of airflow-webserver to testing ui
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/airflow_fw.png></a></p>

- Login with username: admin, password: admin
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/airflow_login.png></a></p>

- Check the result
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/airflow_ui.png></a></p>

**Ref**:
- https://github.com/apache/airflow
