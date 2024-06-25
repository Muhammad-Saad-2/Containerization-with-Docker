# Here we have covered 3 major topics till yet
* Docker Build    
    * how to write a dockerfile
    * base on what components we write a dockerfile
    * container troubleshooting 
    * handling the errors inside the container 
    * interacting with the containers
    * inspecting the containers

* Dev containers 
    * create a container through dev images
    * dev conatainer trouble shooting 

* Docker compose 
    * understanding the concept of Yaml file, what is compose yaml file
    * writing a compose yaml file 
    * how it plays the most important part in your container 
    * based on what compoenets we write a compose.yaml file 

* Compose DB
    

## Commands

* To Build the iamge you will use this command 

```
docker build -t testingimage:1.0.0 .
```
* To see the logs inside the container 


```
ls
```

*  To  create a container in a detach mode 

```
docker run -d -p 8000:8000 testingimage:1.0.0
```

## To create a container in an interactve mode

```
docker run -it -p 8000:8000 testimage:1.0.0 /bin/bash
```

* To step out of the container 
```
exit
```

* To step out of the container without interrupting the container
Pressing Ctrl + P followed by Ctrl + Q in sequence will detach your terminal from the container and return you to your host machine's terminal without stopping the container. This effectively allows you to "step out" of the container without interrupting its execution.
 


## To see the details of the container in case of any error 

```
docker logs <container name > or <container id>

```
## To see the runnig container 

```
docker ps

```
## To see the list of all containers 

```

docker ps -a

```
## To enter in an existing container

* with container name 
```
docker exec -it <container_name or id > /bin/bash
```

* with container id 
```
docker exec -it <container_name or id > /bin/bash
```
writing the starting 4 digits of the id could be enough 

* To inspect the contaienr 
```
docker inspect <container id or name>
```

* To create an image from a container 

```
docker commit<container_name or id >
``` 



## Docker compose 

* To run the compose file in a detach nmode 
```
docker compose up -d"
```

* To stop the ocntainer through docker compose 
```
docker compose down
```

* To forcefully build the container in case of any changes in code 
```
docker compose -up -d --buils
```

* To read the compose.yaml file in the terminal  
```
docker compose config
```


