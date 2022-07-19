## docker 安装
```
sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### 证书
```
curl https://get.acme.sh | sh
bash acme.sh --issue -d "www.domain.com" --standalone -k ec-256 --force --test
bash acme.sh --installcert -d "www.domain.com" --fullchainpath /data/v2ray.crt --keypath /data/v2ray.key --ecc --force          
# 签证书                   
acme.sh --issue -d www.yibu.ga  --standalone 
cp /root/.acme.sh/www.yibu.ga/www.yibu.ga.key /opt/cert/
cp /root/.acme.sh/www.yibu.ga/fullchain.cer /opt/cert
systemctl restart xray
# 0 0 * * 1 -u root /opt/scripts/cleanXrayLog.sh
sed -i d /var/log/xray/access.log
sed -i d /var/log/xray/error.log
```

### nginx
set $domain 在实际使用中不生效
```nginx
server {
    set $domain  'your_domain'
    listen 443 ssl http2;
    ssl_certificate       /etc/v2ray/$domain.crt;
    ssl_certificate_key   /etc/v2ray/$domain.key;
    ssl_protocols         TLSv1.2 TLSv1.3;
    ssl_ciphers           TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-128-CCM-8-SHA256:TLS13-AES-128-CCM-SHA256:EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+ECDSA+AES128:EECDH+aRSA+AES128:RSA+AES128:EECDH+ECDSA+AES256:EECDH+aRSA+AES256:RSA+AES256:EECDH+ECDSA+3DES:EECDH+aRSA+3DES:RSA+3DES:!MD5;

    access_log /var/log/nginx/access.log;
    error_log  /var/log/nginx/error.log;
    server_name www.$domain;
    index index.html index.htm;
    root  /var/www/html/hazze;
    error_page 400 = /400.html;

     location / {
                root  /var/www/html/hazze;
                index index.html index.htm;
                try_files $uri $uri $uri/ =404;
        }

    location /bing
    {
      proxy_redirect off;
      proxy_pass http://127.0.0.1:9000;
      proxy_http_version 1.1;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
      proxy_set_header Host $http_host;
    }
    
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
}
server {
    listen 80;
    server_name www.$domain;
    return 301 https://www.$domain$request_uri;
} 
```

### config.json
```json
{
  "log": {
        "access": "/var/log/v2ray/access.log",
        "error": "/var/log/v2ray/error.log",
        "loglevel": "warning"
    },
  "inbounds": [
    {
    "port":9000,
      "listen": "127.0.0.1", #docker中这里应该是0.0.0.0
      "tag": "vmess-in",
      "protocol": "vmess",
      "settings": {
        "clients": [
          {
          "id":"63a37715-84ee-414c-9371-4440c74555b5",
          "flow":"xtls-rprx-direct",
          "level":0
          }
        ]
      },
      "streamSettings": { # 当使用nginx 反代时，streamSettings时，不要使用tls相关设置，否则会导致400
        "network": "ws",
        "wsSettings": {
          "path":"/path/"
        }
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom",
      "settings": { },
      "tag": "direct"
    },
    {
      "protocol": "blackhole",
      "settings": { },
      "tag": "blocked"
    }
  ],
  "dns": {
    "servers": [
      "https+local://1.1.1.1/dns-query",
          "1.1.1.1",
          "1.0.0.1",
          "8.8.8.8",
          "8.8.4.4",
          "localhost"
    ]
  },
  "routing": {
    "domainStrategy": "AsIs",
    "rules": [
      {
        "type": "field",
        "domain": [
        "googleapis.cn"
        ],
        "inboundTag": [
          "vmess-in"
        ],
        "outboundTag": "direct"
      }
    ]
  }
}# 
手动下载v2ray 安装包：
```
wget https://github.com/v2ray/v2ray-core/releases/download/v4.23.2/v2ray-linux-64.zip
```

### ss
```shell
docker run -d -p 127.0.0.1:9000:9000 --name v2 --restart=always -v /opt/v2:/etc/v2ray teddysun/v2ray
docker run -d --restart always --name v2ray -v /etc/v2ray:/etc/v2ray -p 127.0.0.1:9000:9000 v2fly/v2fly-core 
docker run -d -p 127.0.0.1:9000:9000 --name xray --restart=always -v /etc/xray:/etc/xray teddysun/xray
docker run -d -p 127.0.0.1:3000:3000 --name ct --restart=always -e AUTH="name:password" -e TITLE="download" -v /opt/downloads:/downloads boypt/cloud-torrent
docker run -d --name wt --restart unless-stopped -v /var/run/docker.sock:/var/run/docker.sock   containrrr/watchtower -c $(cat opt/wt/watchtower.list) --schedule "0 0 3 * * *"
```

return 301 https://www.domain.com$request_uri;