**1. Pull helm nginx**:
</br>
```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

**2. Install nginx**:
</br>
  helm install nginx-ingress ingress-nginx/ingress-nginx

3. pull helm cert-manager
helm repo add jetstack https://charts.jetstack.io

4. install cert-manger
helm upgrade --install cert-manager jetstack/cert-manager --version v1.10.1 --set installCRDs=true

5. issue cert for tls
kubectl apply -f ./cert-manager/production_issuer.yaml

6. create secret tls
kubectl create secret tls tls --cert=cf.crt --key=cf.key #you need to create cf.crt and cf.key first

9. orthers:

-----------tls key-------------------------------------------------------
openssl genpkey -algorithm RSA -out tls.key -pkeyopt rsa_keygen_bits:2048
openssl req -new -x509 -key tls.key -out tls.crt -days 365

ref:
https://github.com/kubernetes/ingress-nginx