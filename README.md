## Build docker image

``` 
docker build -t simple-flask-app -f Dockerfile
```

## run with memory constraint
``` 
docker run --name flask-app -p 5000 -m 200m simple-flask-app
```