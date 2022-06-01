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