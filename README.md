**create service account**:
</br>

```bash
kubectl create serviceaccount spark-driver
kubectl create rolebinding spark-driver-rb --clusterrole=kubectl describe clusterrole cluster-admin --serviceaccount=spark-operator:spark-driver
```
