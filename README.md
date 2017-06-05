# Docker-Tools
This repository contains some python scripts to automate workflow for docker cleanup

## Docker cleanup
At times the running docker containers could cause problems on a virtual machine in terms of the
availability of resources on the virtual machine. If there are running docker cntainers on the
virtual machine, the virtutal machine could starve of available memory or become slower than
usual. The python script "docker_cleanup_script.py" helps in removing the docker containers and
their images using a command line. This script is better than executing linux docker commands like
"docker stop <container-id>", "docker rm <container-id>" and "docker rmi <image-name>", as this
script does everything on its won, without the user waiting to execute these commands on after
another.

1. Executing python script as "python docker_cleanup_script.py" displays the usage of this tool
$ python /users/ggaurav/TOOLS/docker_cleanup.py
Usage:  python docker_cleanup_script.py <option:all|images|processes>

2. Executing python script as "python docker_cleanup_script.py all" will cleanup all docker
containers and their images from the virtual machine.

$ docker ps -a
CONTAINER ID        IMAGE                 COMMAND             CREATED             STATUS                        PORTS               NAMES
8d233d20ce29        openswitch_image      "/sbin/init"        28 minutes ago      Exited (129) 28 minutes ago                       ops1
ab773f1ecd04        openswitch_image      "/sbin/init"        36 minutes ago      Up 36 minutes                                     ops
a1f164642ca3        topology/ops:latest   "/sbin/init"        8 days ago          Exited (137) 8 days ago                           sw2_140026880167720

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
openswitch_image    latest              b8802c6563a2        37 minutes ago      661.4 MB
topology/ops        latest              6fe2d4f5fca9        9 days ago          660.9 MB

$ python docker_cleanup_script.py all
Executing the docker cleanup script at 2017-06-04 16:53:37.353123

Cleaning up all docker containers
    Stopping all docker containers on the machine
        Successfully stopped docker instance ab773f1ecd04
    Number of containers successfully stopped: 1
    List of containers successfully stopped: ['ab773f1ecd04']
    Number of containers failed to stop: 0
    List of containers failed to stop: []

    Removing all docker containers on the machine
        Successfully removed docker instance 8d233d20ce29
        Successfully removed docker instance ab773f1ecd04
        Successfully removed docker instance a1f164642ca3
    Number of containers successfully removed: 3
    List of containers successfully removed: ['8d233d20ce29', 'ab773f1ecd04', 'a1f164642ca3']
    Number of containers failed to remove: 0
    List of containers failed to remove: []

Cleaning up all docker images
    Successfully removed docker image b8802c6563a2
    Successfully removed docker image 6fe2d4f5fca9
Number of images successfully removed: 2
List of images successfully removed: ['b8802c6563a2', '6fe2d4f5fca9']
Number of images failed to remove: 0
List of images failed to remove: []

$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE

3 Executing python script as "python docker_cleanup_script.py processes" will cleanup all docker processes
from the virtual machine. None of the docker images will be cleaned-up.

$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
1fc503e57ce1        openswitch_image    "/sbin/init"        2 minutes ago       Up 2 minutes                            ops1

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
openswitch_image    latest              dcec9f48f230        2 minutes ago       661.4 MB

$ python docker_cleanup_script.py processes
Executing the docker cleanup script at 2017-06-04 16:59:39.516627

Cleaning up all docker containers
    Stopping all docker containers on the machine
        Successfully stopped docker instance 1fc503e57ce1
    Number of containers successfully stopped: 1
    List of containers successfully stopped: ['1fc503e57ce1']
    Number of containers failed to stop: 0
    List of containers failed to stop: []

    Removing all docker containers on the machine
        Successfully removed docker instance 1fc503e57ce1
    Number of containers successfully removed: 1
    List of containers successfully removed: ['1fc503e57ce1']
    Number of containers failed to remove: 0
    List of containers failed to remove: []

$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
openswitch_image    latest              dcec9f48f230        3 minutes ago       661.4 MB

4 Executing python script as "python docker_cleanup_script.py images" will cleanup all docker images
from the virtual machine.

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
openswitch_image    latest              dcec9f48f230        3 minutes ago       661.4 MB

$ python docker_cleanup_script.py images
Executing the docker cleanup script at 2017-06-04 17:03:59.664665

Cleaning up all docker images
    Successfully removed docker image dcec9f48f230
Number of images successfully removed: 1
List of images successfully removed: ['dcec9f48f230']
Number of images failed to remove: 0
List of images failed to remove: []

$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
