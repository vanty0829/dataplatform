<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap.png></a></p>

LDAP stands for Lightweight Directory Access Protocol. It is a protocol used to access and manage directory information over an Internet Protocol (IP) network. LDAP is commonly used for:

</br>

- Directory Services: Storing information about users, groups, devices, and other resources in a hierarchical manner.
- Authentication: Verifying user credentials for access control in various applications and services.
- Centralized Management: Providing a central repository for managing user and resource information, making it easier to administer and secure.

</br>

LDAP is often implemented in organizational settings for managing user directories and integrating with other systems.


**1. Buid and push docker image ldap**:
</br>

```bash
docker buildx build -t bill/ldap:0.0.1 -f Dockerfile .
docker push bill/ldap:0.0.1
```

**2. Deploy ldap service**:
</br>

```bash
#ldap server
kubectl apply -f ./ldap.yaml

#ldap management
kubectl apply -f ./lam.yaml
```

- Pod:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap_pod.png></a></p>

- Service:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap_svc.png></a></p>


- LDAP management UI:

<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/ldap_ui.png></a></p>