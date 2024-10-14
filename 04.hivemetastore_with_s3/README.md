<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/hive.png></a></p>

Following Trino we define a maria database container. This is used as the storage layer by the Hive Metastore. The Hive connector enables us to query data stored in S3 storage. In order for Hive to process these files, it must have a mapping for SQL tables to the files and directories in the S3 storage. To accomplish this, Hive uses the Hive Metastore Service ( HMS), often referred to as the Metastore. Metastore manages the metadata about the files such as columns, file locations, file formats, etc. This is how the data files are mapped to schemas and tables. This metadata is stored in the MariaDB, and is accessed via the Hive Metastore service.

</br>

**1. Deploy metastore database**:
</br>

```bash
kubectl apply -f ./metadb.yaml
```

**2. Deploy hive metastore**:
</br>

```bash
kubectl apply -f ./hivemetastore.yaml
```

- Pod:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/hive_pod.png></a></p>

- Service:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/hive_svc.png></a></p>