#!/usr/bin/python3
import os
import subprocess
import time
import docker

# Configuration
DISK_NAME = "/dev/sda1"
DOCKER_COMPOSE_PATH = "/opt/sanchain/readonly"
DOCKER_COMPOSE_FILE = "docker-compose-clean-geth.yml"
CONTAINER_NAME = "sanchain_dev-geth_prune-1"
MAX_DISK_USAGE_PERCENT = 90
WAIT_INTERVAL = 30  # 30 seconds
SLEEP_INTERVAL = 300  # 5 minutes
MAX_WAIT_TIME = 2 * 60 * 60  # 2 hours

client = docker.from_env()

def check_disk_usage():
    try:
        df_output = subprocess.check_output(f"df -h | grep '{DISK_NAME}'", shell=True).decode()
        used_percent = int(df_output.split()[4].replace('%', ''))
        return used_percent
    except subprocess.CalledProcessError as e:
        print(f"Error checking disk usage: {e}")
        return None

def pull_clean_start():
    try:
        os.chdir(DOCKER_COMPOSE_PATH)
    except OSError as e:
        print(f"Error changing directory: {e}")
        return

    try:
        subprocess.check_call(f"docker compose stop", shell=True)
        time.sleep(WAIT_INTERVAL)
        subprocess.check_call(f"docker compose -f {DOCKER_COMPOSE_FILE} up -d", shell=True)
        time.sleep(WAIT_INTERVAL)

        container = client.containers.get(CONTAINER_NAME)
        start_time = time.time()

        while True:
            logs = container.logs().decode('utf-8')
            last_five_lines = logs.splitlines()[-5:]
            if any("State pruning successful" in line for line in last_five_lines):
                print("State pruning successful.")
                break
            elif time.time() - start_time > MAX_WAIT_TIME:
                print("Maximum wait time exceeded. State pruning failed or not found in logs.")
                break
            else:
                print("State pruning not yet visible in the logs.")
            time.sleep(SLEEP_INTERVAL)

        subprocess.check_call("docker compose start", shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing docker commands: {e}")
    except docker.errors.NotFound as e:
        print(f"Container not found: {e}")

if __name__ == "__main__":
    disk_usage = check_disk_usage()
    if disk_usage is None:
        print("Unable to determine disk usage. Exiting...")
    elif disk_usage > MAX_DISK_USAGE_PERCENT:
        print(f"Disk usage is above {MAX_DISK_USAGE_PERCENT}%, starting cleanup operations...")
        pull_clean_start()
    else:
        print(f"Disk usage is below {MAX_DISK_USAGE_PERCENT}%, no action required.")
