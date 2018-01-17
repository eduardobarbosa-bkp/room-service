# Room service (python flask application) - Eduardo Barbosa da Costa

***Setup***
* docker, kubernetes;

***Run***
* On the command line on the project root:

1. *docker build . -t eduardobarbosa/room-service:1.0*
2. *docker-compose up -d*
The endpoints will be available in: http://<docker host>:9090

* On kubernetes
2. *kubectl create -f .*
The endpoints will be available in: http://<cluster IP>:9090

