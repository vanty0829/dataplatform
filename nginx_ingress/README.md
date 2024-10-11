![Nginx](https://github.com/vanty0829/dataplatform/blob/master/images/1.nginx%2Bingress.drawio)

**1. Pull helm nginx**:
</br>
```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

**2. Install nginx**:
</br>
```bash
helm install nginx-ingress ingress-nginx/ingress-nginx
```
  
**3. Pull helm cert-manager**:
</br>
```bash
helm repo add jetstack https://charts.jetstack.io
```


**4. Install cert-manger**:
</br>
```bash
helm upgrade --install cert-manager jetstack/cert-manager --version v1.10.1 --set installCRDs=true
```

**5. Issue cert for tls**:
</br>
```bash
kubectl apply -f ./cert-manager/production_issuer.yaml
```

**6. Create secret tls**:
</br>
```bash
kubectl create secret tls tls --cert=cf.crt --key=cf.key #you need to create cf.crt and cf.key first
```


**9. Others**:
</br>
```bash
#create tls key 
openssl genpkey -algorithm RSA -out tls.key -pkeyopt rsa_keygen_bits:2048
openssl req -new -x509 -key tls.key -out tls.crt -days 365
```

**Ref**:
- https://github.com/kubernetes/ingress-nginx
