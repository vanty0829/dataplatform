<p align="center"><img src=https://github.com/vanty0829/dataplatform/blob/master/99.images/jupyter.png></a></p>

**1. Deploy jupyter.yaml to k8s**:
</br>

```bash
kubectl apply -f ./jupyter.yaml
```

**4. Start SparkSession on k8s**:
</br>

```bash
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("spark-app")
    .master("k8s://https://kubernetes.default.svc.cluster.local:443")
    .config("spark.submit.deployMode", "client")
    .config("spark.executor.instances", "2")
    .config("spark.executor.memory", "2G")
    .config("spark.driver.memory", "2G")
    .config("spark.executor.cores", "1")
    .config("spark.kubernetes.namespace", "spark-operator")
    .config("spark.kubernetes.container.image", "bill/spark:0.0.1") #change with your spark image
    .config("spark.kubernetes.driver.pod.name",os.environ["HOSTNAME"])
    .config("spark.driver.bindAddress", "0.0.0.0")
    .config("spark.driver.host", "jupiter-spark-driver-headless")
    .enableHiveSupport()
    .getOrCreate()
)
```
