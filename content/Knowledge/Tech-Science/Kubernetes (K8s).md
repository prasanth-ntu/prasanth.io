---
tags:
  - Programming
  - softwareengineering
  - DevOps
  - machinelearning
  - OpenSource
---
> [!TIP] [Kubernetes](https://kubernetes.io/docs/concepts/overview/), also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications.

> [!EXAMPLE] Resources
> - Prerequisite: 
> 	- [[Docker]] | [[Docker Compose]]
> - My Demo/Tutorial in Github Repo
> 	- [`prasanth-ntu/k8s-crash-course`](https://github.com/prasanth-ntu/k8s-crash-course)
> - Additional Resources
> 	- [Cheat Sheet - Coursera](https://www.coursera.org/collections/kubernetes-cheat-sheet)
> 	- [Official Documentation](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create)

# Kubernetes Architecture: End-to-End
<iframe src="/static/pages/Kubernetes%20Architecture.html" width="100%" height="750" frameborder="0" allowfullscreen></iframe>
<a href="/static/pages/Kubernetes%20Architecture.html" target="_blank" rel="noopener noreferrer"><b>Open in new tab</b></a> (<i>Note: Best viewed in desktop or landscape view</i>)


# Part 1: Introduction to Kubernetes
## What is Kubernetes?
- Open source (docker) container **orchestration tool**
- Developed by Google
- Helps manage (1000s of) containarized applications in **different deployment environments**

**What *problems* does K8s solve?**
- Increasing trend from **Monolithic** to **Microservices** 
- Increased use of container technology 
	- As containers offer perfect host for small independent applications like microservices
- Demand for proper way of managing those 100s of containers

**What are the *tasks/features* of an orchestration tool**
- High **Availability** or no downtime
- **Scalability** or high performance
- **Disaster recovery** (Self Healing) - backup and restore
## Kubernetes Architecture

![[k8s architecture.png]]

> [!TIP] **Node** = Virtual or Physical Machine

> [!TIP] Worker Nodes = Often referred to as "Nodes"

> [!TIP] kubelet = primary "node agent"
> A k8s process that makes it possible for cluster to talk to each other, and execute some tasks on the nodes (e.g., run application process)

K8s architecture is made up of 
- At least **==1 Master Node==**
	- Master node runs several k8s processes necessary to run and manage cluster properly.
	- Much **more important** than individual worker nodes.
	- Since we need to have backup of master at any given time, especially in prd environment, we will at least have 2 Master Nodes.
	- Processes running in master include
		- **==API Server==** = Entry point to K8s cluster
			- Also a container
			- This is the process different K8s clients (like UI, API, CLI) will talk to
		- **==Controller Manager==** = Keeps track of what's happening in the cluster
		- ==**Scheduler**== = Ensures Pods placement
			- Intelligent process that decides on which Worker Node new Pod should be placed/scheduled based on available resources on the worker node, and the load that container needs.
		- **==**etcd== = K8s backing store
			- At any time, stores the current state of any K8s components in the cluster (i.e., etcd snapshots)
- **==Worker Nodes==** connected to it
	- Each node has a ==kubelet== process running 
	- Each worker node has containers of different applications deployed on it 
		- A single node can run multiple containers. This is because a node can run multiple **Pods**, and each Pod can contain one or more containers. The scheduler decides how many pods get placed on a given node based on available resources (CPU, memory) and pod scheduling rules (like affinity/anti-affinity).
		- Best practice is to run **one application container per Pod**. However, a Pod *can* have multiple containers when they are tightly coupled — these are called **sidecar containers** (e.g., logging agents, proxy containers like Envoy/Istio, init containers for config setup). Containers in the same Pod share the same network namespace (localhost) and storage volumes, so they should only be grouped if they truly need that tight coupling.
	- Worker node is where our applications are running (i.e., actual work is happening) and has the most load. So, they are much bigger and has more resources.
- **==Virtual Network==** = Creates one unified machine

# Part 2: Main Kubernetes Components

![[k8s main components.png]]
## Node

> [!TIP] **Node** = Virtual or Physical Machine

## Pod 
- **Smallest** unit unit in K8s
- **Abstraction** over Docker Container 	
	- So, we only interact with K8s layer
- Usually **1 Application per Pod**
	- e.g., 1 server Node with 2 containers running 		
		- Our custom JS app running in 1 Pod
		- MongoDB Pod running in 1 Pod
- Each Pod (not the container) gets its **own IP address**
	- Using this internal IP address, they can communicate with each other
- **New IP address** on recreation
	 - ⚠️ Pod is Ephemeral

In other words, Pod is like a layer over the Docker Container, so that we don't have to work directly with Docker technology. 
## Service
- **Permanent IP address**
	- Attached to each Pod
- Lifecycle of Pod and Service are **not connected**
	- IP address will stay even if Pod dies
- We specify the **type of Service** on creation
	-  Internal Service is the default type
- The Service is also a **load balancer**
## Ingress
- The (external) request goes to Ingress (e.g., https://my-app.com from user browser), which then forwards the request to the Service
## ConfigMap
- **External** Configuration of our application
- Contains configuration data like
	- URLs of database (e.g., `DB_URL = mongo-db`)
	- Other services
- ⚠️ ConfigMap is for non-confidential data only
- Reference ConfigMap in Deployment/Pod
- Use it as environment variables or as a properties file
## Secret
- Just like ConfigMap, but used store **secret data** (such as credentials) 
- Data is not stored as plain text, but as base64 encoded format
- Reference Secret in Deployment/Pod
- Use it as environment variables or as a properties file
## Volume

> [!WARNING] K8s does not manage data persistence!

> [!TIP] Think of Storage as external HD plugged into the K8s cluster.

- Data Storage (DB): If we have only 1 DB container or pod and if it gets restarted, the data would be gone, which is problematic as DB data should be persisted long term
- To address this issue, we can use the Volumes
	- It attaches physical storage on a hard drive to our pod
	- The storage could be 
		- Local machine or
		- Remote/Cloud storage, outside of K8s cluster (with external reference)
## Deployment
- *Distributed System*: **Replicate everything** on multiple servers
	- Instead of relying on 1 application pod and 1 DB pod
	- The replica is connected to the same Service (Yay!)
		- So, if one application Pod dies, the Service will redirect the request to another application Pod
-  **Blueprint**/Template for creating Pods (e.g., for `my-app`)
	- Specify how many replicas we want
- In practice, we create **Deployments** (not Pods)
- **Abstraction** of Pods
- For StateLESS Apps
	- ❌ DB cannot be replicated via Deployment as DBs have state
## StatefulSet
- For STATEFUL apps or DBs
	- e.g., MySQL, MongoDB, Elastic
- Deploying StatefulSet is not easy
- DBs are often hosted outside K8s cluster.
## DeamonSet
...
## Summary of K8s Components
- Pod: Abstraction of containers
- Service: Communication between Pods
- Ingress: Router traffic into cluster
- ConfigMap: External configuration
- Secrets: External configuration
- Volume: Data Persistence
- Deployment: Replication for StateLESS apps
- StatefulSet: Replication for StateFul apps or DBs
## How to create the resources & configure the K8s cluster?
- All configs goes through Master Node through process called ==API Server==, which is the main and only entry point to the cluster
- The request has to be in YAML/JSON format
- K8s client could be
	- UI
	- API
	- Script
	- Curl command
	- kubectl - K8s CLI

### K8s Configuration
- **Declarative**
- Is == Should
	- Controller Manager checks:  `desired state == actual state ?`

### 3 Parts of K8s Configuration File
1. **Metadata** (`metadata`)
2.  **Specification** (`spec`)
	- Attributes will be specific to the `kind`
3. **Status** (`status`)
	- Automatically generated, added and updated continuously by K8s.
	- Where does K8s gets the status data?
		- From `etcd`
Besides that, we also have API version and service kind.

![[k8s master processes.png]]

# Part 3:  Local Setup: Minikube and kubectl

## What is minikube?
**Production Cluster Setup**
- Multiple Master Nodes and Worker Nodes
- Separate virtual or physical machines each representing a Node
![[k8s production cluster setup.png]]

🤔 **Test on Local Machine?**
- We may not have enough resources locally to test this entire cluster

**Minikube**
- Both Master Nodes and Worker Nodes processes run on **ONE machine**
- Comes Docker Container runtime pre-installed, where we can run the pods with containers in the (virtual) Node.
- Minikube has kubectl as dependency

![[k8s Local cluster setup.png]]
## What is kubectl?
- CLI for K8s cluster
	- Helps to interact with various K8s clusters (like Minikube cluster, Cloud cluster, etc.)
- As we know, the API server in Master Processes is the main entry point into the K8s cluster
	- We can talk to the API server via 3 different clients (CLI, UI, API) where
		- 💪 `kubectl` is the most powerful of 3 clients
	
![[what is kubectl.png]]

## Set-up Minikube cluster

**Installation**
- For installation details, refer [Official Doc](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fhomebrew).

**Start our Minikube cluster**
- We need either a **container runtime** or **VM manager** on our laptop to run minikube
	- This will be the driver for our minikube
	- Refer [Official Doc](https://minikube.sigs.k8s.io/docs/drivers/) for Drivers supported.

> [!TIP] Docker is one of the preferred driver for running minikube on all OS

> [!TIP] 2 Layers of Docker
> 1. Minikube running as Docker container
> 2. Docker inside Minikube to run our application container

```bash
$ minikube start --driver docker
```

```bash
$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

```bash
# Display all the nodes in the Cluster
kubectl get node
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   73m   v1.34.0
```

Now, we have actual K8s cluster running locally in our machine. We can start deploying applications in it.
# Part 4: Complete Demo Project

## Demo Project Overview

![[k8s demo project overview.png]]

We will deploy a mongoDB and web application. The web application will connect to mongoDB via external configuration data (ConfigMap and Secret). Finally, we will make web application accessible externally from browser.

Key resources
- [K8s documentation](https://kubernetes.io/docs/home/)
- [nanajanashia/k8s-demo-app](https://hub.docker.com/r/nanajanashia/k8s-demo-app/tags) image from DockerHub

## K8s Components Overview

Let's create all 4 K8s configuration files needed for deploying our application setup.
![[k8s components overview.png]]

### 1. `mongo-config.yaml`
Copy the template from official doc > [configmap](https://kubernetes.io/docs/concepts/configuration/configmap/#configmaps-and-pods), and update it.
### 2. `mongo-secret.yaml`
Copy the template from official doc > [secret](https://kubernetes.io/docs/concepts/configuration/secret/#use-case-dotfiles-in-a-secret-volume), and update it.

```bash
# Values in secrets are Base64 encoded. So, we cannot store them in plain text. So, we need to use Base64 form.
$ echo -n mongouser | base64
 bW9uZ291c2Vy

$ echo -n mongopassword | base64
bW9uZ29wYXNzd29yZA==
```

> [!DANGER] `Secret` file should not be synced in Git repo.

> [!NOTE] These external configurations (ConfigMap and Secret) can now be references by different **Deployments**.
### 3. `mongo.yaml`
1 unified file Config file for deployment and service for MongoDB.
#### Deployments
Copy the template from official doc > [deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment), and update it.
##### Label
- We can give any K8s component a **label**
- Labels are **key/value** pairs that are attached to k8s resources
- Additional **Identifiers** of the components in addition to the name
- Examples
	- `"release": "stable"` vs. `"release": "canary"` 
	- `"env": "dev"` vs. `"env": "prd"` 
	- `"tier": "frontend"` vs. `"tier": "backend"` 
- Why do we need them?
	- Unlike names, Labels do not provide uniqueness.
		- e.g., All Pod replicas will have the same label

| Unique name      | `mongo-101` | `mongo-111` | `mongo-210` |
| ---------------- | ----------- | ----------- | ----------- |
| **Common Label** | `app:nginx` | `app:nginx` | `app:nginx` |
##### **Label Selectors**
- How does K8s know which Pods belong to Deployments?
	- Identify a set of resources
	- e.g., Match all Pods with label "app:nginx"
#### Service
Copy the template from official doc > [service](https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service), and update it.
### 4. `webapp.yaml` - WebApp Deployment & Service
Copy the contents of `mongo.yaml` and update as per needed, especially the `name`, `image`, `labels`, `port`, etc.

### 5. Pass ConfigMap & Secret Data to Mongo & WebApp Pods Deployment
#### `mongo.yaml`
We need to set: Username and Password when the DB starts
- [Environment variables](https://hub.docker.com/_/mongo#environment-variables): 
		- `MONGO_INITDB_ROOT_USERNAME`
		- `MONGO_INITDB_ROOT_PASSWORD 

> [!QUESTION] How do we pass these environment variables to mongo application running inside the container?
> - We can use `env` with `name` and `value` in the `.yaml` file.
> - [!WARNING] However, we should Reference `Secret` data here instead of hardcode sensitive data.
- Example:
```yaml
        env:
          - name: MONGO_INITDB_ROOT_USERNAME
            # value: secretValue # Reference Secret data here instead of hardcode sensitive data.
            valueFrom:
              secretKeyRef:
                name: mongo-secret # Name of the Secret resource that holds the username.
                key: mongo-user
```

#### `webapp.yaml`
When our webapp starts, it will need to connect to MongoDB. So, we need to give info about DB Endpoint and other details.

> [!QUESTION] How do we pass the DB endpoint, username, and password to webapp?
> - DB **Endpoint** (`DB_URL`) - Ref from `ConfigMap`
> - DB **Username** (`USER_NAME`) - Ref from `Secret`
> - DB **Password** (`USER_PWD`) - Ref from `Secret`

> [!NOTE] FYI, the webapp is already configued to take in the above values as **environment variables**

### 6. Configure External Service
### `webapp.yaml`
To make the webapp accessible from outside (e.g., browser), we need to make it as an External Service by setting `Service` 
- `type`: Service type
	- Options: `ClusterIP` (Default, an Internal Service) or `NodePort` (External Service)
- `NodePort`: exposes the Service on each Node's IP at a static port
	- Must be between 30000 - 32767

### 7. Final Step
We will create the above Services/Pods one by one in K8s.

Minikube is running, but no components deployed yet.
```bash
$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

$ kubectel get pods
No resources found in default namespace.
```

> [!IMPORTANT] `ConfigMap`and `Secret` must exist before Deployments.

#### Start the (Pod) services
```bash
$ kubectl get pods
No resources found in default namespace.

$ kubectl apply -f mongo-config.yaml 
configmap/mongo-config created

$ kubectl apply -f mongo-secret.yaml 
secret/mongo-secret created

$ kubectl apply -f mongo.yaml       
deployment.apps/mongo-deployment created
service/mongo-service created

$ k8s-demo kubectl apply -f webapp.yml 
deployment.apps/webapp-deployment created
service/webapp-service created 

$ kubectl get pods
NAME                                 READY   STATUS              RESTARTS   AGE
mongo-deployment-5585b4c49c-fzxzz    0/1     ContainerCreating   0          8s
webapp-deployment-67c784bbc6-t955s   0/1     ContainerCreating   0          1s
```

#### **Interacting with K8s cluster**
```bash
# Gives all the components created in the K8s cluter, including
# Pods
# Services
# Deployment

$ kubectl get all 
NAME                                     READY   STATUS    RESTARTS   AGE
pod/mongo-deployment-5585b4c49c-fzxzz    1/1     Running   0          2m18s
pod/webapp-deployment-67c784bbc6-t955s   1/1     Running   0          2m11s

NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP          7h22m
service/mongo-service    ClusterIP   10.111.229.76    <none>        27017/TCP        2m18s
service/webapp-service   NodePort    10.107.206.166   <none>        3000:30100/TCP   2m11s

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mongo-deployment    1/1     1            1           2m18s
deployment.apps/webapp-deployment   1/1     1            1           2m11s

NAME                                           DESIRED   CURRENT   READY   AGE
replicaset.apps/mongo-deployment-5585b4c49c    1         1         1       2m18s
replicaset.apps/webapp-deployment-67c784bbc6   1         1         1       2m11s
```

```bash
$ kubectl get configmaps 
NAME               DATA   AGE
kube-root-ca.crt   1      7h24m
mongo-config       1      4m49s

$ kubectl get secrets 
NAME           TYPE     DATA   AGE
mongo-secret   Opaque   2      4m41s
```


```bash
# Get more detailed output about specific component like Pod or Service
$ kubectl describe service webapp-service
Name:                     webapp-service
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=webapp
Type:                     NodePort
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.107.206.166
IPs:                      10.107.206.166
Port:                     <unset>  3000/TCP
TargetPort:               3000/TCP
NodePort:                 <unset>  30100/TCP
Endpoints:                10.244.0.4:3000
Session Affinity:         None
External Traffic Policy:  Cluster
Internal Traffic Policy:  Cluste

# Gets details of the pod including status, config, etc.
$ kubectl describe pod webapp-deployment
Name:             webapp-deployment-67c784bbc6-t955s
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
... 
```

```bash
# Get logs
$ kubectl logs webapp-deployment-67c784bbc6-t955s
app listening on port 3000!

# Stream the logs
$ kubectl logs webapp-deployment-67c784bbc6-t955s -f
app listening on port 3000!
```
#### Validate that app is accessible from Browser
```bash
$ kubectl get service
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP          7h32m
mongo-service    ClusterIP   10.111.229.76    <none>        27017/TCP        12m
webapp-service   NodePort    10.107.206.166   <none>        3000:30100/TCP   11m
```

> [!Question] Which IP address should we access?
> NodePort Service is accessible **on IP address of Cluster Nodes (all the Worker Node's the Cluster has)**.

Since we only have 1 which is the minikube, let's get that
```bash
$ minikube ip        
192.168.49.2

$ kubectl get node    
NAME       STATUS   ROLES           AGE     VERSION
minikube   Ready    control-plane   7h34m   v1.34.0

$ kubectl get node -o wide
NAME       STATUS   ROLES           AGE     VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
minikube   Ready    control-plane   7h34m   v1.34.0   192.168.49.2   <none>        Ubuntu 22.04.5 LTS   6.12.54-linuxkit   docker://28.4.0
```

As mentioned in the Youtube guide, the http://192.168.49.2 did not work.
Instead, these two alternative options worked.
```bash
# Option 1a:
$ minikube service webapp-service
┌───────────┬────────────────┬─────────────┬───────────────────────────┐
│ NAMESPACE │      NAME      │ TARGET PORT │            URL            │
├───────────┼────────────────┼─────────────┼───────────────────────────┤
│ default   │ webapp-service │ 3000        │ http://192.168.49.2:30100 │
└───────────┴────────────────┴─────────────┴───────────────────────────┘
🏃  Starting tunnel for service webapp-service./┌───────────┬────────────────┬─────────────┬────────────────────────┐
│ NAMESPACE │      NAME      │ TARGET PORT │          URL           │
├───────────┼────────────────┼─────────────┼────────────────────────┤
│ default   │ webapp-service │             │ http://127.0.0.1:57630 │
└───────────┴────────────────┴─────────────┴────────────────────────┘
🏃  Starting tunnel for service webapp-service.
🎉  Opening service default/webapp-service in default browser...
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.

# Option 1b: 
$ minikube service webapp-service --url
http://127.0.0.1:53087
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it

# Option 2:                                                                   
$ kubectl port-forward svc/webapp-service 3000:3000
Forwarding from 127.0.0.1:3000 -> 3000
Forwarding from [::1]:3000 -> 3000
Handling connection for 3000
Handling connection for 3000
Handling connection for 3000
Handling connection for 3000
Handling connection for 3000
Handling connection for 300
```

**Why `minikube ip:30100` failed earlier?**
- With Minikube **docker driver on macOS**, the “node IP” (`minikube ip`, e.g. `192.168.x.x`) is often on an internal network your host can’t route to directly, so `NodePort` on that IP can time out even though the Service and Pods are healthy.

**Option 1: `minikube service webapp-service --url`**
- **What it does**: Asks Minikube to expose the Kubernetes **Service** to your host and prints a **reachable URL** (often `http://127.0.0.1:<random-port>` on macOS with the `docker` driver).
- **Why it worked**: Your host can always reach `127.0.0.1`, and Minikube sets up the needed forwarding/tunnel so traffic reaches `webapp-service` inside the cluster.
- **When to use**: Quick “give me a URL I can open in the browser” for a Service.
 
 **Option 2: `kubectl port-forward svc/webapp-service 3000:3000`**
- **What it does**: Creates a local tunnel from **your machine** `localhost:3000` → **the Service** `webapp-service:3000` inside the cluster (through the Kubernetes API connection).
- **Key detail**: This does **not** require `NodePort` or `minikube ip` to be reachable; it works as long as `kubectl` can talk to the cluster.
- **When to use**: Reliable debugging, a stable local port, or when NodePort/VM IP routing isn’t reachable from your host.

