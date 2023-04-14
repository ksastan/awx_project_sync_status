# awx_project_sync_status
Script checks AWX project synchronisation status and provide it as prometheus metric.
Metrics endpoint `/metrics`, e.g.:
```shell
htttp://<ip>:<METRICS_PORT>/metrics
```

# Prerequisites
Install python modules
```shell
pip install requirements.txt
```

# Environment variables
- METRICS_PORT - listening TCP port, e.g. 8000
- AWX_URL - AWX URL address, http://awx.server/
- AWX_TOKEN - token to access AWX
- CHECKS_DELAY - delay between projects checks

Variables can be exported in shell or in other ways, e.g. docker via docker/k8s envs:
```shell
export METRICS_PORT="8000"
export AWX_URL="https://my.awx/"
export AWX_TOKEN="my-secret-token"
```
