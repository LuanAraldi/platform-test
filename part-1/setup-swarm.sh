docker swarm init --advertise-addr 192.168.150.236
docker service create --name registry --publish published=5000,target=5000 registry:2
docker network create -d overlay --subnet 192.168.0.0/24 --gateway 192.168.0.1 --attachable dockernet
docker-compose build
docker-compose push