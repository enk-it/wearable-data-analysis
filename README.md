# Installation

```shell

yay -S clickhouse clickhuse-client
yay -S grafana

sudo systemctl enable --now clickhouse-server

sudo systemctl enable --now grafana


```


# Grafana

Grafana default host is your machine hostname, and default port is 3000, so you can access it like this:

```
http://archpc:3000
```

default login/password is admin/admin

