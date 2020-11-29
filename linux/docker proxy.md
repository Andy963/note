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
```

### nginx
```nginx
server {
    listen 443 ssl http2;
    ssl_certificate       /opt/cert/certificate.crt;
    ssl_certificate_key   /opt/cert/private.key;
    ssl_protocols         TLSv1.3;
    ssl_ciphers           TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-128-CCM-8-SHA256:TLS13-AES-128-CCM-SHA256:EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+ECDSA+AES128:EECDH+aRSA+AES128:RSA+AES128:EECDH+ECDSA+AES256:EECDH+aRSA+AES256:RSA+AES256:EECDH+ECDSA+3DES:EECDH+aRSA+3DES:RSA+3DES:!MD5;

    server_name www.domain.com;
    index index.html index.htm;
    root  /opt/site;
    error_page 400 = /400.html;

    location /xxx/
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
}
server {
    listen 80;
    server_name www.domain.com;
    return 301 https://www.domain.com$request_uri;
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
      "streamSettings": {
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

docker run -d --name wt --restart unless-stopped -v /var/run/docker.sock:/var/run/docker.sock   containrrr/watchtower -c $(cat opt/wt/watchtower.list) --schedule "0 0 3 * * *"
```



### config
```trojan
{
    "run_type": "server",
    "local_addr": "0.0.0.0",
    "local_port": 443,
    "remote_addr": "127.0.0.1",
    "remote_port": 80,
    "password": [
        "nopassword1"
    ],
    "log_level": 1,
    "ssl": {
        "cert":"/opt/cert/certifacate.crt",
        "key":"/opt/cert/private.key",
        "key_password": "",
        "cipher": "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384",
        "cipher_tls13": "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384",
        "prefer_server_cipher": true,
        "alpn": [
            "http/1.1"
        ],
        "reuse_session": true,
        "session_ticket": false,
        "session_timeout": 600,
        "plain_http_response": "",
        "curves": "",
        "dhparam": ""
    },
    "tcp": {
        "prefer_ipv4": false,
        "no_delay": true,
        "keep_alive": true,
        "reuse_port": false,
        "fast_open": false,
        "fast_open_qlen": 20
    },
    "mysql": {
        "enabled": false,
        "server_addr": "127.0.0.1",
        "server_port": 3306,
        "database": "trojan",
        "username": "trojan",
        "password": ""
    }
}
```

```shell
mkdir -p /etc/trojan-go
```
### server
```json
cat > /etc/trojan-go/config.json <<EOF
{
    "run_type": "server",
    "local_addr": "0.0.0.0",
    "local_port": 443,
    "remote_addr": "127.0.0.1",
    "remote_port": 80,
    "password": [
        "1stepkill1p"
    ],
    "ssl": {
        "cert": "full_chain.pem",
        "key": "private.key",
        "sni": "domain.com",
        "fallback_port": 1234
    }
}
EOF
```

### client 
```json
{
    "run_type": "client",
    "local_addr": "127.0.0.1",
    "local_port": 51837,
    "remote_addr": "www.domain.com",
    "remote_port": 443,
    "password": [
        "1stepkill1p"
    ],
    "ssl": {
        "sni": "www.domain.com"
    },
    "mux" :{
        "enabled": true,
    },
    "router":{
        "enabled": true,
        "bypass": [
            "geoip:cn",
            "geoip:private",
            "geosite:cn",
            "geosite:geolocation-cn"
        ],
        "block": [
            "geosite:category-ads"
        ],
        "proxy": [
            "geosite:geolocation-!cn"
        ]
    }
}
```

```shell
docker run -d --network host --name tg --restart=always -v /etc/trojan-go:/etc/trojan-go teddysun/trojan-go
```

return 301 https://www.domain.com$request_uri;