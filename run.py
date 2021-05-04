import os
import socket

from configobj import ConfigObj

SERVICE_DIR = "services/"


def checkPort(host, port):
    # REF: https://docs.python.org/3/library/socket.html
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock.connect_ex((host, port))


def launchService(service, host, port):
    # Check if the service is running or not
    addr = f"localhost://{port}"
    print(f"Address is {addr}")
    resp = checkPort(host, int(port))
    if resp != 0:
        print(
            f"Service {service} not running, starting service at port {port} on host {host}"
        )
        os.system(f"python {SERVICE_DIR}{service}.py &")
    else:
        print(f"Service {service} running at port {port} on host {host}")


def walkThrough(section, obj):
    if "preload" in section:
        services = section["preload"].split(" ")
        for service in services:
            launchService(service, obj[service]["host"], obj[service]["port"])
    launchService(section.name, section["host"], section["port"])


def loadDependencies():
    # Read the dependencies.ini file
    config = ConfigObj("dependencies.ini")
    for section in config:
        walkThrough(config[section], config)


if __name__ == "__main__":
    loadDependencies()
