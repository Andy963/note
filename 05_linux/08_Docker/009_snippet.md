### dockerhub

本地构建docker镜像并推送到dockerhub

```shell

docker build . -t telegram_chatgpt_bot:1.05

docker tag chatgpt:1.0.5 andy963/telegram_chatgpt_bot:1.0.5

docker push andy963/telegram_chatgpt_bot:1.0.5

docker run -d  --name chatgpt -v /etc/gpt:/etc/gpt andy963/telegram_chatgpt_bot:latest
```


### watchtower
用来更新docker镜像
```sh
# 将需要监测的docker 实例写到watchtoer.list中，
# 后面的schedule 则是周期，是6位crontab格式
docker run -d \
    --name wt \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    $(cat /opt/containerd/watchtower.list) \
    --schedule "0 0 2 */7 * *"

# 只运行一次更新，更新完删除watchtower镜像
docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --run-once \
    ct
```


#### ct

shell 命令

```sh
docker run -d -p 127.0.0.1:3000:3000 --name ct --restart=always -e AUTH="andy963:pwd" -e TITLE="Hello download" -v /opt/downloads:/downloads boypt/cloud-torrent

```

nginx 配置

```nginx
#ctorrent
 location /ctorrent/ {
    proxy_pass http://127.0.0.1:3000/; # note the trailing slash here, it matters!
}

location /ctorrent/sync {
   proxy_pass http://127.0.0.1:3000/sync;
   proxy_set_header Connection '';
   proxy_http_version 1.1;
   chunked_transfer_encoding off;
   proxy_buffering off;
   proxy_cache off;
}
```