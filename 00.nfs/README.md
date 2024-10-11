<p align="center"><img alt="Nginx" src=https://github.com/vanty0829/dataplatform/blob/master/99.images/00nfs.png></a></p>

NFS (Network File System) is a popular storage solution in Kubernetes that allows multiple pods to mount the same storage volume with ReadWriteMany (RWX) access mode. Here are some key points about NFS in Kubernetes.

**1. Pull helm nfs**:
</br>
```bash
helm repo add stable https://charts.helm.sh/stable
helm repo update
```

**2. Install nfs**:
</br>
```bash
helm install nfs stable/nfs-server-provisioner
```

<p align="center"><img alt="nginx_pod" src=https://github.com/vanty0829/dataplatform/blob/master/99.images/nfs_storage_class.png></a></p>

**3. Deploy PVC (Persistent Volume Claim) with nfs class**:
</br>
nfspvc.yaml
```bash
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-pvc
  labels: {}
  annotations: {}
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 2Gi
  storageClassName: nfs
```

```bash
kubectl apply -f ./nfspvc.yaml
```

<p align="center"><img alt="nginx_pod" src=https://github.com/vanty0829/dataplatform/blob/master/99.images/nfs_pvc.png></a></p>
