docker swarm init --advertise-addr 192.168.150.236
docker service create --name registry --publish published=5000,target=5000 registry:2
docker volume create --name=testvol -o size=10G