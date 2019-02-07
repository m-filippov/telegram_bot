import docker
client = docker.DockerClient(base_url='tcp://10.8.24.183:1234')
print client.containers.list()