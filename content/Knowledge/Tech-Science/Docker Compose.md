---
tags:
  - Programming
  - softwareengineering
  - DevOps
  - machinelearning
---
> [!TIP] Docker compose is a (centralised) tool to manage (define and run) multi-containers Docker applications in 1 isolated environment.
> - To define and manage services
> - So they run together in isolated environment
> - Easy to run and clean up our entire app

Prerequisite: [[Docker]]
Postrequisite: [[Kubernetes (K8s)]]

This note is a cohesive walkthrough based on the crash course I watched ([YouTube video](https://www.youtube.com/watch?v=SXwC9fSwct8)),  the hands-on custom docker compose project ([`prasanth-ntu/docker-compose-crash-course/`](https://github.com/prasanth-ntu/docker-compose-crash-course/tree/main)), and the corresponding custom image for JS application pushed to the Docker Hub ([`## prasanthntu/my-app`](https://hub.docker.com/r/prasanthntu/my-app)).

# Docker Compose Architecture: End-to-End
<iframe src="https://prasanth.io/static/pages/Docker%20Compose%20Architecture.html" width="100%" height="650" frameborder="0" allowfullscreen></iframe>
<a href="https://prasanth.io/static/pages/Docker%20Compose%20Architecture.html" target="_blank" rel="noopener noreferrer"><b>Open in new tab</b></a> (*Note: Best viewed in desktop or landscape view*)

# `docker compose.yaml` configuration

> [!TIP] **Simplifies** container management

- ✅ Helps to structure our commands.
	- With a **single** command, we create and start all the services from our configurations.
- ✅ Easier to make changes, and see current configuration.
	- We use a **single YAML file** to configure and maintain our application's services.
- **✅ Declarative** definition approach.
	- Defining the current state.

## Network configuration
- ✅ By default, **Compose sets up a single network** for our app.
- ✅ Communication via container name.
- ✅ We have option to specify our own networks with top-level "**network**" keys.

## Control Startup Order
- Some services depend on other services (e.g., mongo-express depending on mongo-db, webapp that needs to connect to db).
- `depends_on` attribute controls the order of service startup and shutdown.

# Demo 
## Demo Without Compose

> [!warning] We achieve everything with plain docker commands.
### Step 1 - Create the Docker Network

> [!TIP] Docker network = Allows containers to communicate with each other and with the external world

```bash
$ docker network ls 

NETWORK ID     NAME      DRIVER    SCOPE
76e60ffb24f0   bridge    bridge    local
e5fe30e3c7da   host      host      local
412bd0cd1370   none      null      local
```

Create a user-defined network using `docker network create [OPTIONS] NETWORK_NAME`.
```bash
$ misc docker network create mongo-network   
fec1b2d064db058e2087e243eb85b90b9a16630bc7b27c0bab09c1a245b5361f

$ docker network ls 

NETWORK ID     NAME            DRIVER    SCOPE
76e60ffb24f0   bridge          bridge    local
e5fe30e3c7da   host            host      local
fec1b2d064db   mongo-network   bridge    local
412bd0cd1370   none            null      local
```

Containers connected to `mongo-network` can resolve each other by name.

### Step 2 - Start MongoDB Container
- Docker Hub > Official Images > [`mongo`](https://hub.docker.com/_/mongo)
	- [Default MongoDB port](https://hub.docker.com/_/mongo#connect-to-mongodb-from-another-docker-container): `27017`
	- [Environment variables](https://hub.docker.com/_/mongo#environment-variables): 
		- `MONGO_INITDB_ROOT_USERNAME` - 
		- `MONGO_INITDB_ROOT_PASSWORD` - 

Fetch/pull the mongoDB docker image and run it in detached mode.
```bash 
# start mongodb
$ docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=supersecret \
--network mongo-network \
--name mongodb \
mongo

Unable to find image 'mongo:latest' locally
latest: Pulling from library/mongo
e4ff4183d396: Pull complete 
97dd3f0ce510: Pull complete 
be6c93d4528b: Pull complete 
3ab158345587: Pull complete 
fe1d960a6567: Pull complete 
cec3fd50f49f: Pull complete 
90aac4a84565: Pull complete 
bdb9ad4997b8: Pull complete 
fce2d6033e18: Download complete 
2ce8f7b034ed: Download complete 
Digest: sha256:7f5bbdafebde7c42e42e33396d01c0eda3eb753da8dae99071a30e350568a0a4
Status: Downloaded newer image for mongo:latest
045ac74aff2b4407cd9579768c10c105043fe19ebac6024ef52f7af1b828a6ad
```

```bash
$ docker ps      
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                             NAMES
045ac74aff2b   mongo     "docker-entrypoint.s…"   19 seconds ago   Up 18 seconds   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   mongodb
```

### Step 3 - Start Mongo Express Container
- Docker >Hub  Official Images > [`mongo-express`](https://hub.docker.com/_/mongo-express)
	- [Default Express port](https://hub.docker.com/_/mongo-express#how-to-use-this-image): `8081`
	- [Environment variables](https://hub.docker.com/_/mongo-express#configuration): 
		- `ME_CONFIG_MONGODB_ADMINUSERNAME` - MongoDB admin username
		- `ME_CONFIG_MONGODB_ADMINPASSWORD` - MongoDB admin password
		- `ME_CONFIG_MONGODB_SERVER` - MongoDB container name. Use comma delimited list of host names for replica sets.

Fetch/pull the mongo-express docker image and run it.
```bash
# start mongo-express
$ docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=supersecret \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--network mongo-network \
--name mongo-express \
mongo-express
```

```bash
$ docker ps      

  CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                             NAMES
ade494422af5   mongo-express   "/sbin/tini -- /dock…"   13 seconds ago   Up 13 seconds   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp       mongo-express
d5a8c56f2dd7   mongo           "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   mongodb
```

Retrieve the mongo-express web login creds 
```bash
$ docker logs -f mongo-express 

Waiting for mongo:27017...
/docker-entrypoint.sh: line 15: mongo: Name does not resolve
/docker-entrypoint.sh: line 15: /dev/tcp/mongo/27017: Invalid argument
...
Welcome to mongo-express 1.0.2
------------------------


Mongo Express server listening at http://0.0.0.0:8081
Server is open to allow connections from anyone (0.0.0.0)
basicAuth credentials are "admin:pass", it is recommended you change this in your config.js
```

Visit http://localhost:8081/ and enter the login creds retrieved from the logs
- username: `admin`
- password: `pass`

![[mongo-express-localhost.png]]

> [!SUCCESS] 🥳 We are able to connect to the MongoDB using Mongo Express

## Demo With Compose
### Step 1 - Map docker commands to compose definition
`docker-compose.yaml`
```YAML
services: # List all our services we want to run

  mongodb: # First service (container name of the service)
  # configs for the service
    image: mongo # Image to use for the service
    ports: # List of ports to expose
      - 27017:27017 # Map the port 27017 on the host to the port 27017 on the container
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=supersecret
  
  mongo-express:
    image: mongo-express
    ports:
      - 8081:8081
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - ME_CONFIG_MONGODB_ADMINPASSWORD=supersecret
      - ME_CONFIG_MONGODB_SERVER=mongodb
    depends_on:
      - mongodb
```

### Step 2 - Create and start containers
[Official documentation](https://docs.docker.com/reference/cli/docker/compose/up/)

Go through `docker-compose.yaml` and start all the docker container services configured in it.
```bash
# Builds, (re)creates, starts, and attaches to containers for a service.
$ docker compose -f docker-compose.yaml up

...
[+] Running 3/3
 ✔ Network docker-compose-demo_default            Created                                                                                                                                                    0.0s 
 ✔ Container docker-compose-demo-mongo-express-1  Created                                                                                                                                                    0.0s 
 ✔ Container docker-compose-demo-mongodb-1        Created                                                                                                                                                    0.0s 
Attaching to mongo-express-1, mongodb-1
...
mongo-express-1  | Mongo Express server listening at http://0.0.0.0:8081
mongo-express-1  | Server is open to allow connections from anyone (0.0.0.0)
mongo-express-1  | basicAuth credentials are "admin:pass", it is recommended you change this in your config.js!
mongodb-1        | {"t":{"$date":"2025-12-25T11:06:57.313+00:00"},"s":"I",  "c":"NETWORK",  "id":22943,   "ctx":"listener","msg":"Connection accepted","attr":{"remote":"172.18.0.3:52368","isLoadBalanced":false,"uuid":{"uuid":{"$uuid":"7c957071-43ce-479d-88c0-7adf35250adc"}},"connectionId":3,"connectionCount":3}}
mongodb-1        | {"t":{"$date":"2025-12-25T11:06:57.314+00:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"172.18.0.3:52368","client":"conn3","negotiatedCompressors":[],"doc":{"driver":{"name":"nodejs","version":"4.13.0"},"os":{"type":"Linux","name":"linux","architecture":"arm64","version":"6.12.54-linuxkit"},"platform":"Node.js v18.20.3, LE (unified)|Node.js v18.20.3, LE (unified)"}}}
...
```

> [!NOTE] `compose up` **aggregates the output** of each container.
> So, the logs of the two containers `mongodb-1` and `mongo-express-1` are mixed.
  
Docker container names follow `<folder_name>-<service-name>-<id>`.
```bash
$ docker ps      
  
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                             NAMES
c783f9de70f9   mongo           "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   docker-compose-demo-mongodb-1
ca8f40bbda1a   mongo-express   "/sbin/tini -- /dock…"   2 minutes ago   Up 2 minutes   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp       docker-compose-demo-mongo-express-1
```

Docker compose takes care of creating dedicated network for all the containers (refer `docker-compose-demo_default` network).
```bash
$ docker network ls

NETWORK ID     NAME                          DRIVER    SCOPE
44928d6c7344   bridge                        bridge    local
8681bc4c5af8   docker-compose-demo_default   bridge    local
e5fe30e3c7da   host                          host      local
412bd0cd1370   none                          null      local
```

Visit http://localhost:8081/ and enter the login creds retrieved from the logs
- username: `admin`
- password: `pass`

![[mongo-express-localhost.png]]

Create a new db and table
- Create `my-db` DB
- Inside the `my-db`, create `my-collection` collection

Run docker compose in the background
```bash
$ docker compose -f docker-compose.yaml up -d
[+] Running 2/2
 ✔ Container docker-compose-demo-mongodb-1        Started                                                                                                                                                    0.1s 
 ✔ Container docker-compose-demo-mongo-express-1  Started       
```

Easy way to **stop** (and **completely remove**) all the containers, networks, volumes and images created by "up" ⟹ All the changes made to the db will be gone as **containers are ephemeral**.
```bash
$ docker compose -f docker-compose.yaml down 
[+] Running 3/3
 ✔ Container docker-compose-demo-mongo-express-1  Removed                                                                                                                                                    0.2s 
 ✔ Container docker-compose-demo-mongodb-1        Removed                                                                                                                                                    0.3s 
 ✔ Network docker-compose-demo_default            Removed       
```

To stop and re-start the containers only (without completely removing them) ⟹ Will keep the data 
```bash
$docker compose -f docker-compose.yaml stop 
[+] Stopping 2/2
 ✔ Container docker-compose-demo-mongo-express-1  Stopped                                                                                                                                                    0.2s 
 ✔ Container docker-compose-demo-mongodb-1        Stopped   

$ docker compose -f docker-compose.yaml start
[+] Running 2/2
 ✔ Container docker-compose-demo-mongodb-1        Started                                                                                                                                                    0.1s 
 ✔ Container docker-compose-demo-mongo-express-1  Started   

```

### Step 3 - Add own custom web application
Git repo: https://gitlab.com/twn-youtube/docker-compose-crash-course

![[3-services-in-docker-compose.png]]

Add "New Document" in the `my-collection` with below details:
```json
{
        "_id": ObjectId(),
    	"myid": 1,
    	"data": "some dynamic data loaded from mongodb"
}
```
After adding, it would look something like this
![[mongo-express-my-collection-new-doc.png]]

#### **What we will do now**

![[docker-compose-what-we-will-do.png]]

1. Let's create a custom JS application that
	- Connects to the mongo db
	- Displays the retrieved data
2. Containerize the JS application with `Dockerfile`
3. Run it as part of the `docker compose` services using `docker-compose.yaml`

Clone the repo
```bash
$ git clone https://gitlab.com/twn-youtube/docker-compose-crash-course                                               
Cloning into 'docker-compose-crash-course'...
warning: redirecting to https://gitlab.com/twn-youtube/docker-compose-crash-course.git/
remote: Enumerating objects: 12, done.
remote: Total 12 (delta 0), reused 0 (delta 0), pack-reused 12 (from 1)
Receiving objects: 100% (12/12), 19.01 KiB | 19.01 MiB/s, done.
```

Project Tree
```
|- app
	|- server.js # Connects to the DB logic
	|- index.html # Shows 2 lines of data (1. static hardcoded, 2. dynamic from MongoDB)
	|- package.json
|- Dockerfile
|- docker-compose-v1.yaml
```

> [!NOTE] We don't have to worry about understanding the actual code as our focus is on the configuration and dockerization.

Update the yaml file.

Run docker compose to start all our services.
```bash
$ docker compose -f docker-compose-v1.yaml up -d                               
[+] Building 14.4s (13/13) FINISHED                                                                                                                                                                               
 => [internal] load local bake definitions                                                                                                                                                                   0.0s
 => => reading from stdin 599B                                                                                                                                                                               0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                         0.0s
 => => transferring dockerfile: 551B                                                                                                                                                                         0.0s
 => [internal] load metadata for docker.io/library/node:20-alpine                                                                                                                                            4.2s
 => [auth] library/node:pull token for registry-1.docker.io                                                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                                                              0.0s
 => [1/5] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448                                                                                      5.4s
 => => resolve docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448                                                                                      0.0s
 => => sha256:bb9f6f8b202047f37f5d51a1f2e731b60925a601fe4c9c1495e6c000ddd25944 1.26MB / 1.26MB                                                                                                               1.0s
 => => sha256:70268380327fbc2d9c066979d554cdff4c22f752e9be70bde123ec5ccb64c292 443B / 443B                                                                                                                   0.6s
 => => sha256:eb9824d7990580162dd96cf3c8e08c9e966ed8d819adbb6e065c3c5ab73d74b4 43.12MB / 43.12MB                                                                                                             4.8s
 => => extracting sha256:eb9824d7990580162dd96cf3c8e08c9e966ed8d819adbb6e065c3c5ab73d74b4                                                                                                                    0.6s
 => => extracting sha256:bb9f6f8b202047f37f5d51a1f2e731b60925a601fe4c9c1495e6c000ddd25944                                                                                                                    0.0s
 => => extracting sha256:70268380327fbc2d9c066979d554cdff4c22f752e9be70bde123ec5ccb64c292                                                                                                                    0.0s
 => [internal] load build context                                                                                                                                                                            0.0s
 => => transferring context: 79.97kB                                                                                                                                                                         0.0s
 => [2/5] RUN mkdir -p /home/app                                                                                                                                                                             0.3s
 => [3/5] COPY ./app /home/app                                                                                                                                                                               0.0s
 => [4/5] WORKDIR /home/app                                                                                                                                                                                  0.0s
 => [5/5] RUN npm install                                                                                                                                                                                    3.1s
 => exporting to image                                                                                                                                                                                       1.0s 
 => => exporting layers                                                                                                                                                                                      0.6s 
 => => exporting manifest sha256:8309693daec8852b51aab55da903df788f891c9815ca3b7da07bd12d32a53825                                                                                                            0.0s 
 => => exporting config sha256:9c1b48bebea1dd7c80915825f2bb9ca7efb4be17071c688b8a875c99c445b3d9                                                                                                              0.0s
 => => exporting attestation manifest sha256:7d3a9651efd8f15d76d9f8fe2c938a4ccdff1021efa86795055b9a5cc7326270                                                                                                0.0s
 => => exporting manifest list sha256:46ac1d0db873ba307f412e7ef79ad7f10156416c3971fd5b22aae8307aa03fd2                                                                                                       0.0s
 => => naming to docker.io/library/docker-compose-crash-course-my-app:latest                                                                                                                                 0.0s
 => => unpacking to docker.io/library/docker-compose-crash-course-my-app:latest                                                                                                                              0.3s
 => resolving provenance for metadata file                                                                                                                                                                   0.0s
[+] Running 5/5
 ✔ docker-compose-crash-course-my-app                     Built                                                                                                                                              0.0s 
 ✔ Network docker-compose-crash-course_default            Created                                                                                                                                            0.0s 
 ✔ Container docker-compose-crash-course-my-app-1         Started                                                                                                                                            0.4s 
 ✔ Container docker-compose-crash-course-mongodb-1        Started                                                                                                                                            0.4s 
 ✔ Container docker-compose-crash-course-mongo-express-1  Started 
```

Visit http://localhost:3000/ and we will observe this 
![[viewe-data-from-front-end-no-dynamic-data.png]]

```bash
$ docker ps                                     
CONTAINER ID   IMAGE                                COMMAND                  CREATED              STATUS              PORTS                                             NAMES
d938cb321665   mongo-express                        "/sbin/tini -- /dock…"   About a minute ago   Up About a minute   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp       docker-compose-crash-course-mongo-express-1
002bd3e0ba3a   mongo                                "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   docker-compose-crash-course-mongodb-1
789e177f4333   docker-compose-crash-course-my-app   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp       docker-compose-crash-course-my-app-1
```

```bash
$ docker ps -a
CONTAINER ID   IMAGE                                COMMAND                  CREATED              STATUS                       PORTS                                             NAMES
d938cb321665   mongo-express                        "/sbin/tini -- /dock…"   About a minute ago   Up About a minute            0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp       docker-compose-crash-course-mongo-express-1
002bd3e0ba3a   mongo                                "docker-entrypoint.s…"   About a minute ago   Up About a minute            0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   docker-compose-crash-course-mongodb-1
789e177f4333   docker-compose-crash-course-my-app   "docker-entrypoint.s…"   About a minute ago   Up About a minute            0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp       docker-compose-crash-course-my-app-1
979c5d68491d   mongo-express                        "/sbin/tini -- /dock…"   2 hours ago          Exited (143) 2 minutes ago                                                     docker-compose-demo-mongo-express-1
5929b55898a1   mongo                                "docker-entrypoint.s…"   2 hours ago          Exited (0) 2 minutes ago                                                       docker-compose-demo-mongodb-1
```
From the above results, we can see that the previous container services 
- `docker-compose-demo-mongodb-1` and 
- `docker-compose-demo-mongo-express-1`
are not running. 

Instead, new container services
- `docker-compose-crash-course-mongodb-1`, 
- `docker-compose-crash-course-mongo-express-1`, and 
- `docker-compose-crash-course-my-app-1`
are created from scratch.

Let's override the value that's used as a prefix (say, we want to reuse the containers but moved the `docker-compose.yaml` to a different project folder/location).

```bash
# Remove the newly created containers
$ docker compose -f docker-compose-v1.yaml down 
[+] Running 4/4
 ✔ Container docker-compose-crash-course-mongo-express-1  Removed                                                                                                                                            0.3s 
 ✔ Container docker-compose-crash-course-my-app-1         Removed                                                                                                                                            1.2s 
 ✔ Container docker-compose-crash-course-mongodb-1        Removed                                                                                                                                            0.3s 
 ✔ Network docker-compose-crash-course_default            Removed     
 
# 
$ docker compose --project-name docker-compose-demo -f docker-compose-v1.yaml up -d
...
[+] Running 4/4
 ✔ docker-compose-demo-my-app                     Built                                                                                                                                                      0.0s 
 ✔ Container docker-compose-demo-my-app-1         Started                                                                                                                                                    0.2s 
 ✔ Container docker-compose-demo-mongodb-1        Started                                                                                                                                                    0.2s 
 ✔ Container docker-compose-demo-mongo-express-1  Started     
```
From the above output, we can observe that old instances of `docker-compose-demo-mongodb-1` and `docker-compose-demo-mongo-express-1` are restarted instead of new ones being created.

So, if we refresh, we will still have `my-db` and `my-collection`, and the data inside in it.

Visit http://localhost:3000/ and we will observe this (both static and dynamic data)
![[view-data-from-front-end-with-dynamic-data.png]]

Here's the `Network` results, esp. the `fetch-data` results
![[network-results-for-fetch-data-dynamical-from-mongodb.png]]
```bash
$ curl -s http://localhost:3000/fetch-data 
{"_id":"694d85017720d490d5f09da1","myid":1,"data":"some dynamic data loaded from mongodb"}%
```

To stop (and remove) all the services,
```bash
$ docker compose --project-name docker-compose-demo -f docker-compose-v1.yaml down
[+] Running 4/4
 ✔ Container docker-compose-demo-my-app-1         Removed                                                                                                                                                    1.2s 
 ✔ Container docker-compose-demo-mongo-express-1  Removed                                                                                                                                                    0.2s 
 ✔ Container docker-compose-demo-mongodb-1        Removed                                                                                                                                                    0.2s 
 ✔ Network docker-compose-demo_default            Removed                                                                                                                                                    0.2s 

$ docker ps                                                                      
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
#### Variables in `docker-compose.yaml`

> [!DANGER] Do NOT hardcode any sensitive data, esp username, passwords, tokens, secret keys, etc.

Update the `docker-compose.yaml` file by replacing hardcoded ENV variables with placeholders.

Then, export these environment variables in the shell.
```bash
$ echo $MONGO_ADMIN_USER               


$ export MONGO_ADMIN_USER=admin

$ export MONGO_ADMIN_PASS=supersecret          

$ echo $MONGO_ADMIN_USER       
admin

$ echo $MONGO_ADMIN_PASS  
supersecret
```

```bash
# Run the docker compose to start the build and service
$ docker compose --project-name docker-compose-demo -f docker-compose-v2.yaml up 
[+] Running 4/4
 ✔ Network docker-compose-demo_default            Created                                                                                                                                                    0.0s 
 ✔ Container docker-compose-demo-my-app-1         Created                                                                                                                                                    0.0s 
 ✔ Container docker-compose-demo-mongodb-1        Created                                                                                                                                                    0.1s 
 ✔ Container docker-compose-demo-mongo-express-1  Created                                                                                                                                                    0.1s 
Attaching to mongo-express-1, mongodb-1, my-app-1
...
  
```

```bash
# Stop the container service (but do not remove it)
$ $ docker compose --project-name docker-compose-demo -f docker-compose-v2.yaml stop

# (Re-)Start the service
$ docker compose --project-name docker-compose-demo -f docker-compose-v2.yaml start
```

#### Use `secrets` in `docker-compose.yaml`
> [!DANGER] With environment variables, there is still a risk of **unintentional information exposure**.

- `secrets` is an even better way to use secrets without having to use environment variables.
	- 1) Define the secret using the ***top-level `secrets`*** element.
	- 2) In the service definition, **reference the secret** with the `secrets` attribute.
- This permits **granular access control** within a service container via standard filesystem permissions.

```yaml
# Secrets example
services:
	myapp:
		image: myapp:latest
		secrets: 
			- my_secret
			  
secrts:
	my_secret
		file: ./my_secret.txt
```

#### Push to repository & Pull from it (Public or Private)
Create a new repo in your docker account
- Namespace: `prasanthntu`
- Repository Name: `my-app`

Build our image using docker file
```bash
# Build our image using "docker build" command 
$ docker build -t prasanthntu/my-app:1.0 .
[+] Building 2.9s (11/11) FINISHED                                                                                                                                                           docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                         0.0s
 => => transferring dockerfile: 551B                                                                                                                                                                         0.0s
 => [internal] load metadata for docker.io/library/node:20-alpine                                                                                                                                            2.7s
 => [auth] library/node:pull token for registry-1.docker.io                                                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                                                            0.0s
 => => transferring context: 2B                                                                                                                                                                              0.0s
 => [1/5] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448                                                                                      0.0s
 => => resolve docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448                                                                                      0.0s
 => [internal] load build context                                                                                                                                                                            0.0s
 => => transferring context: 170B                                                                                                                                                                            0.0s
 => CACHED [2/5] RUN mkdir -p /home/app                                                                                                                                                                      0.0s
 => CACHED [3/5] COPY ./app /home/app                                                                                                                                                                        0.0s
 => CACHED [4/5] WORKDIR /home/app                                                                                                                                                                           0.0s
 => CACHED [5/5] RUN npm install                                                                                                                                                                             0.0s
 => exporting to image                                                                                                                                                                                       0.1s
 => => exporting layers                                                                                                                                                                                      0.0s
 => => exporting manifest sha256:cb7bf027253cf5e6590db1d1c4469f43bc177014ee9a6fd12294abef6aa03323                                                                                                            0.0s
 => => exporting config sha256:a7d8f4f3b0f1523de7d0cb41b83eb16a623e48322d19c5092d5fa461dc76363b                                                                                                              0.0s
 => => exporting attestation manifest sha256:147f5f94745c90d51456656000d3e761ab48b7a3a067cccf7029322f38bae292                                                                                                0.0s
 => => exporting manifest list sha256:7905293d827c3947ee40648377bdb62404bf5cb83c2afc6978210920c5f384d9                                                                                                       0.0s
 => => naming to docker.io/prasanthntu/my-app:1.0                                                                                                                                                            0.0s
 => => unpacking to docker.io/prasanthntu/my-app:1.0                                                                                                                                                         0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/mbpw4z5gartqe0ouw85kx5ox1
```

Login into the docker in shell
```bash
$ docker login                            
Authenticating with existing credentials... [Username: prasanthntu]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
```

Push the new tag to the repository
```bash
$ docker push prasanthntu/my-app:1.0    
The push refers to repository [docker.io/prasanthntu/my-app]
46544c70f387: Pushed 
bb9f6f8b2020: Pushed 
f6b4fb944634: Pushed 
5144ef3ea83f: Pushed 
70268380327f: Pushed 
eb9824d79905: Pushed 
2bbed94c184c: Pushed 
4f4fb700ef54: Mounted from opensearchproject/opensearch-dashboards 
ea93af6352ec: Pushed 
1.0: digest: sha256:589a4da7779488b24168c6469bd5b5be0da6016f4e022661f584cf6747a287e0 size: 856
```

 Update the `docker-compose.yaml` file by commenting out `build: .` and add `image: prasanthntu/my-app:1.0` to reference our custom image in our docker repo.

Pull the image from repository and run
```bash
$ docker compose --project-name docker-compose-demo -f docker-compose-v3.yaml up -d
[+] Running 6/6
 ✔ my-app Pulled                                                                                                                                                                                             8.2s 
   ✔ 5144ef3ea83f Pull complete                                                                                                                                                                              0.0s 
   ✔ 4f4fb700ef54 Pull complete                                                                                                                                                                              0.0s 
   ✔ 2bbed94c184c Pull complete                                                                                                                                                                              0.0s 
   ✔ 46544c70f387 Pull complete                                                                                                                                                                              0.4s 
   ✔ ea93af6352ec Download complete                                                                                                                                                                          0.0s 
[+] Running 3/3
 ✔ Container docker-compose-demo-my-app-1         Started                                                                                                                                                    0.3s 
 ✔ Container docker-compose-demo-mongodb-1        Started                                                                                                                                                    0.1s 
 ✔ Container docker-compose-demo-mongo-express-1  Started  
```

# Limitations of docker compose
> [!WARNING] A **lot of  operational effort** to run containers on a large scale.
- Only well-suited for local development and **small-scale deployments** (i.e., if we have smaller set of containers)
- Designed to run containers on a **single** host system
- Engineers still need to operate the containers **manually**

# Kubernetes to the Rescue
> [!TIP] With kubernetes, we can merge hundreds of servers into one huge server to deploy all the containers that belong to same app in the environment.
- Can manage **large-scale apps** and containers deployed across **multiple nodes**
- Auto-Scaling
- Self-Healing

> [!TIP] Docker & Kubernetes - Strengths and Use Cases
> - **Docker**: Simplifies local development, testing and for smaller deployments.
> - **Kubernetes**: **Advanced features** for scalability, high availability and production-grade deployments.
