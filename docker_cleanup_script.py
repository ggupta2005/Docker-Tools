"""
This python script is useful to stop and remove docker containers or remove
the docker images
"""
import sys
import os
import subprocess
import datetime
from time import sleep


def docker_stop_docker_processes(docker_process_name):

    """
    This function stops the docker container named 'docker_process_name'
    if 'docker_process_name' is not None. Otherwise this function attempts
    to stop all running docker containers.
    """

    if docker_process_name is not None:
        cmd_string = 'docker stop %s > /dev/null' \
                     % (docker_process_name)

        val = os.system(cmd_string)

        if val is 0:
            print("Successfully stopped a docker instance %s" \
                  % docker_process_name)
        else:
            print("Couldn't stop docker instance %s" \
                  % docker_process_name)
        return

    print("\tStopping all docker containers on the machine")

    containers_stopped_successfully = []
    containers_stopped_failure = []

    output = subprocess.check_output('docker ps -q', shell=True)
    output_lines = output.split("\n")

    for line in output_lines:

        if len(line) == 0:
            continue

        cmd_string = 'docker stop %s > /dev/null' % (line)
        val = os.system(cmd_string)

        if val is 0:
            print("\t\tSuccessfully stopped docker instance %s" % line)
            containers_stopped_successfully.append(line)
        else:
            print("\t\tCouldn't stop docker instance %s" % line)
            containers_stopped_failure.append(line)

    print("\tNumber of containers successfully stopped: " + \
          str(len(containers_stopped_successfully)))
    print("\tList of containers successfully stopped: " + \
          str(containers_stopped_successfully))

    print("\tNumber of containers failed to stop: " + \
          str(len(containers_stopped_failure)))
    print("\tList of containers failed to stop: " + \
          str(containers_stopped_failure))


def docker_remove_docker_processes(docker_process_name):

    """
    This function removes the inactive docker container named
    'docker_process_name' if 'docker_process_name' is not None.
    Otherwise this function attempts to remove all inactive docker
    containers.
    """

    if docker_process_name is not None:
        cmd_string = 'docker rm %s > /dev/null' \
                     % (docker_process_name)

        val = os.system(cmd_string)

        if val is 0:
            print("Successfully removed adocker instance %s" \
                  % docker_process_name)
        else:
            print("Couldn't remove docker instance %s" \
                  % docker_process_name)

        return

    print("\n\tRemoving all docker containers on the machine")

    containers_removed_successfully = []
    containers_removed_failure = []

    output = subprocess.check_output('docker ps -a -q', shell=True)

    output_lines = output.split("\n")

    for line in output_lines:

        if len(line) == 0:
            continue

        cmd_string = 'docker rm %s > /dev/null' % (line)
        val = os.system(cmd_string)

        if val is 0:
            print("\t\tSuccessfully removed docker instance %s" % line)
            containers_removed_successfully.append(line)
        else:
            print("\t\tCouldn't remove docker instance %s" % line)
            containers_removed_failure.append(line)

    print("\tNumber of containers successfully removed: " + \
          str(len(containers_removed_successfully)))
    print("\tList of containers successfully removed: " + \
          str(containers_removed_successfully))

    print("\tNumber of containers failed to remove: " + \
          str(len(containers_removed_failure)))
    print("\tList of containers failed to remove: " + \
          str(containers_removed_failure))


def docker_cleanup_remove_docker_processes(docker_process_name):

    """
    This function stops and removes the active docker container named
    'docker_process_name'
    """

    print "\nCleaning up all docker containers"

    docker_stop_docker_processes(docker_process_name)
    docker_remove_docker_processes(docker_process_name)


def docker_cleanup_remove_docker_image(docker_image_name):

    """
    This function removes the docker image named 'docker_image_name'
    if 'docker_image_name' is not None. Otherwise this function attempts
    to remove all docker images on the machine.
    """

    if docker_image_name is not None:

        cmd_string = 'docker rmi %s > /dev/null' % (docker_image_name)
        val = os.system(cmd_string)

        if val is 0:
            print("Successfully removed docker image %s" \
                  % docker_image_name)
        else:
            print("Couldn't remove docker image %s" \
                  % docker_image_name)

        return

    print "\nCleaning up all docker images"

    images_removed_successfully = []
    images_removed_failure = []

    output = subprocess.check_output('docker images -q', shell=True)
    output_lines = output.split("\n")

    for line in output_lines:

        if len(line) == 0:
            continue

        cmd_string = 'docker rmi %s > /dev/null' % (line)
        val = os.system(cmd_string)

        if val is 0:
            print("\tSuccessfully removed docker image %s" % line)
            images_removed_successfully.append(line)
        else:
            print("\tCouldn't remove docker image %s" % line)
            images_remove_failure.append(line)

    print("Number of images successfully removed: " + \
          str(len(images_removed_successfully)))
    print("List of images successfully removed: " + \
          str(images_removed_successfully))

    print("Number of images failed to remove: " + \
          str(len(images_removed_failure)))
    print("List of images failed to remove: " + \
          str(images_removed_failure))


def ovsdb_perf_tool_print_tool_usage():
    """
    This function prints the usage CLI of the docker cleanup tool
    """
    print("Usage:  python docker_cleanup_script.py" + \
          " <option:all|images|processes>")


if __name__ == '__main__':

    now = datetime.datetime.now()

    if len(sys.argv) < 2:
        ovsdb_perf_tool_print_tool_usage()
    else:
        print("Executing the docker cleanup script at " + str(now))
        if sys.argv[1] == "processes":
            docker_cleanup_remove_docker_processes(None)
        elif sys.argv[1] == "images":
            docker_cleanup_remove_docker_image(None)
        elif sys.argv[1] == "all":
            docker_cleanup_remove_docker_processes(None)
            docker_cleanup_remove_docker_image(None)
