

```mongo
docker run --name mymongo -v /opt/mymongo/data:/data/db -d mongo
docker run --link mymongo:mongo -p 8081:8081 mongo-express

docker exec -it mymongo mongo # 连接到上面运行的mongo
```