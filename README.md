scraping sports betting b/c why not. Now dockerized.

### Commands:


* Build it
```
docker-compose build
```

* Run it (detached)
```
docker-compose up -d
```

* Connect to container running python for current dev set-up (I subsequently run ipython in the container)
```
# we know container is named "pystuff" due to docker-compose.yml param
docker exec -it pystuff /bin/bash
```
