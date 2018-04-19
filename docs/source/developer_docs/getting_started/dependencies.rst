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

Windows
-------

If you use Windows, you have my condolances.

For Windows 10 Professional or Enterprise 64-bit, use
`Docker for Windows <https://www.docker.com/docker-windows>`_.

For any other version of Windows, get
`Docker Toolbox <https://docs.docker.com/toolbox/overview/>`_.  This will
install VirtualBox, and your Docker containers will run inside of a Linux VM.

Alternatively, you may choose to spin up a Linux VM and run your containers
inside of it directly.


Mac
---

Docker for Mac requires OS X El Capitan 10.11 or newer with Intel hardware
support for MMU virtualization (2010 or newer).  If your system does not
satisfy these requirements, you can install Docker Toolbox.
