import requests
import sys
import time
import os
from prometheus_client import start_http_server, Gauge

METRICS_PORT = os.environ.get('METRICS_PORT', 16784)
AWX_URL = os.environ.get('AWX_URL')
AWX_TOKEN = os.environ.get('AWX_TOKEN')
FAILED_STATUSES = {"failed", "error", "canceled"}
CHECKS_DELAY = os.environ.get('CHECKS_DELAY', 10)
# todo: replace by environment variable
PROJECTS_ID_TO_CHECK = []  # awx projects ID


def get_project_info(project_id, session):
    project_info = session.get(f"{AWX_URL}/api/v2/projects/{project_id}",
                               headers={'Authorization': f'Bearer {AWX_TOKEN}'})
    if project_info.status_code < 400:
        return project_info.json()
    else:
        print(f"AWX connection error http_status={project_info.status_code}")
        sys.exit(1)


def main():
    start_http_server(METRICS_PORT)

    # add metrics
    projects_status = Gauge('awx_project_up', 'Status of AWX project synchronisation', ['project_id', 'project_name'])

    # check endpoints every 'CHECKS_DELAY'
    while True:
        with requests.Session() as s:
            for project in PROJECTS_ID_TO_CHECK:
                project_info = get_project_info(project, s)
                projects_status.labels(project_id=project).set(
                    1 if project_info['status'] not in FAILED_STATUSES else 0)
        time.sleep(CHECKS_DELAY)


if __name__ == '__main__':
    main()
