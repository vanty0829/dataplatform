**Create namespace**:
</br>

```bash
kubectl create namespace spark-operator
```
**Jump in specific namespace**:
</br>

```bash
kubectl config set-context --current --namespace=spark-operator
```

**Create service account**:
</br>

```bash
kubectl create serviceaccount spark-driver
kubectl create rolebinding spark-driver-rb --clusterrole=cluster-admin --serviceaccount=spark-operator:spark-driver
```

**Build & push image**:
</br>

```bash
docker buildx build -t bill/k8s:0.0.7 -f Dockerfile .
docker push bill/k8s:0.0.7
```


**Interact with pod**:
</br>

```bash
$podName = $(kubectl get pods -l "app=workers" -o name) -split '/' | Select-Object -Last 1
kubectl cp ./test.py ${podName}:/opt/airflow/dags/test.py
kubectl cp ./config ${podName}:/opt/airflow/dags/config


$pods = kubectl get pods -l "app=workers" -o name
foreach ($pod in $pods) {
    $podName = $pod -replace 'pod/', ''
    kubectl cp ./airflow/dags ${podName}:/opt/airflow
    kubectl cp ./config ${podName}:/opt/airflow/dags/config
    kubectl exec ${podName} -- pip install spark-on-k8s
}

$pods = kubectl get pods -l "dag=mount" -o name
foreach ($pod in $pods) {
    $podName = $pod -replace 'pod/', ''
    
    kubectl cp ./airflow/dags ${podName}:/opt/airflow
}

$podName = $(kubectl get pods -l "app=spark" -o name) -split '/' | Select-Object -Last 1
kubectl cp ./bill/ ${podName}:/home/


kubectl exec -it ${podName} -- chmod 777 /home/bill/


$podName = $(kubectl get pods -l "app=spark" -o name) -split '/' | Select-Object -Last 1
kubectl cp ${podName}:/home/bill/ ./bill/
```