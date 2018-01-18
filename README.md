# Room service (python flask application) - Eduardo Barbosa da Costa

***Setup***
* docker, kubernetes;

***Run***
##### On the command line on the project root:

1. *docker build . -t eduardobarbosa/room-service:1.0*
2. *docker-compose up -d*
The endpoints will be available in: http://&lt;docker host&gt;:9090

##### On kubernetes
2. *kubectl create -f .*
The endpoints will be available in: http://&lt;cluster IP&gt;:9090

