<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ranger.webp></a></p>

<p align="center">
    <b>Apache Ranger: An open-source framework for centralized policy management that we will use for Trino access control</b>
</p>


**1. Build Solr image and deploy**:
</br>

- Build Solr image:

```bash
#cd ./images/solr

docker buildx build -t bill/ranger-solr:0.0.1 -f Dockerfile.solr .
docker push bill/ranger-solr:0.0.1
```

- Deploy Solr:

```bash
kubectl apply -f ranger-solr.yaml
```

#### Solr UI
    
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/solr_ui.png></a></p>


**2. Deploy Ranger DB**:
</br>


```bash
kubectl apply -f ranger-db.yaml
```


**3. Build Ranger Admin image and deploy**:
</br>

- Build Ranger Admin image:

```bash
#cd ./images/ranger-admin

docker buildx build -t bill/ranger-admin:0.0.1 -f Dockerfile .
docker push bill/ranger-admin:0.0.1
```

- Deploy Ranger Admin:

```bash
kubectl apply -f ranger-admin.yaml
```

#### Ranger Admin UI
    
<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ranger_login.png></a></p>

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ranger_ui.png></a></p>

**4. Build Ranger UserSync image and deploy**:
</br>

- Build Ranger UserSync image:

```bash
#cd ./images/ranger-usersync

docker buildx build -t bill/ranger-usersync:0.0.1 -f Dockerfile.usersync .
docker push bill/ranger-usersync:0.0.1
```

- Deploy Ranger - Build Ranger UserSync image:
:

```bash
kubectl apply -f ranger-usersync.yaml
```


**5. Config access control for Trino-user on  Ranger**:
</br>

- Allow info-schema and jdbc:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ranger_allow_schema.png></a></p>

- Grant permssion for user:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ranger_grant_permistion.png></a></p>