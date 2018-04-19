############
Dependencies
############

You will need to install:

* Git
* Docker https://docs.docker.com/engine/installation/
* Docker Compose https://docs.docker.com/compose/install/

For linux environments, you may want to add yourself to the docker
group so that you don't have to use sudo to run docker or docker-compose.

``sudo usermod -aG docker $USER``

On Windows you must have Windows 10 Pro, Enterprise, or Education and
Microsoft Hyper-V to install Docker Engine.  If you don't, you'll need to
install Docker Toolbox instead (https://docs.docker.com/toolbox/overview/)
This will install VirtualBox and a linux VM, and your containers will
run inside of this VM instead of directly on your host.
