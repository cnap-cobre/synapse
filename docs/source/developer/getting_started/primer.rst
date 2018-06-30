############################
Primer on Docker and Compose
############################

`Intended Audience: Developers who are less familiar with Docker.  If you
have worked with Docker in the past, feel free to skip this section.`

Docker
------

To simplify the way we specify our project's execution environment, we will be
using Docker containers.

A container is a lot like a virtual machine...it provides an isolated
environment for programs to execute that is consistent, no matter the host
operating system or hardware.  Containers are like VMs but not quite the same.
Virtual machines are an abstraction of physical hardware.  Each VM runs a full
copy of an operating system with one or more applications and can have a
footprint of many GBs.  A container is lighter weight.  Containers are an
abstraction which make use of the host OS's kernel but otherwise isolate
program execution.  Containers tend to package together code and dependencies
with one process per container.  Because they are lighter weight, containers
take up less space (MBs rather than GBs) and have much faster startup times.

What is most important about containers (Docker, specifically) is that they are
immutable infrastructure.  By default, files saved to the filesystem inside of
a container are `not` persisted across restarts of the container.  While this
sounds like a weakness, it is a strength.  Default immutability encourages us
to store data in a database where it belongs and to be intentional about what
files, or more generally "state" that we do persist.  By not preserving any
state across restarts, containers are `predictable`.  Because they isolate
their filesystem, networking, process, and other system namespaces, they are
`portable`.  If an application runs in a container version on your PC, it will
run on my Mac.  While immutability is default, we can specify persistent data
"volumes" which are mounted onto the container's filesystem.  We can also
set up mappings from the host filesystem to the container's.

Docker containers are specified in a ``Dockerfile``.  Typically these start
with pulling down a Docker base image.  For example, ``FROM ubuntu:17.10``
is found as the first line of many Dockerfiles.  From there, dependencies are
installed, and application code is copied into the container.


Docker Compose
--------------

In a microservices architecture, an application takes the form of many small,
loosely coupled components, each of which has a single, focused job.  Docker
pairs nicely with this style of application.  Each microservice runs fully
isolated in its own lightweight container.

To orchestrate the running of two or more containers and specify the
networking, both between them as well as with the outside world, we use Docker
Compose.  See the ``docker-compose.yml`` file at the root of the repository for
an example.

In our case, we have the following containers:

* ``db``: Runs PostgreSQL
* ``backend``: Runs our Django application
* ``frontend``: Builds and serves our frontend React application
* ``webserver``: Proxies incoming requests (details vary between dev. and prod.)

Further down the road, there will likely be more containers as data modeling,
image processing, and collaboration tools are added.

Note that directories exist at the repository root for all ``backend``,
``frontend``, and ``webserver``, but db is pulled in as an image from
DockerHub and requires no further code or configuration besides setting
environment variables in the ``docker-compose.yml``.


Python Virtual Environments
---------------------------

(Worth knowing about, but we're not using them.  Here's why...)

Imagine a scenario where you are working on two separate projects.  Your first
project requires Django version 1.09 while your second project requires
Django version 2.0.  Ordinarily, your system can only have one version of
Django installed at a time because packages are globally installed.

Virtual Environments solve this problem by creating a local directory where
copies of your project's dependencies are stored.  When keeping your code in a
Git repository, the convention is to write a ``requirements.txt`` file that
lists your project's dependencies.  The dependencies themselves are left
out of the repo.  If a friend wants to clone your repository and run your
project, all they would need to do is create and enter a new virtual
environment, run ``pip install -r requirements.txt`` to install the
dependencies to that virtual environment, and they are good to go.

Once you are done working on a project, you can exit the virtual environment.
Your global python package directory remains untouched.

**For our purposes, we will not need virtual environments because the Docker
container already provides the isolation we are looking for.**  Within the
context of the container, we can install pip packages globally without worry
of conflicts because there is only one program per container.  We still follow
the ``requirements.txt`` convention.  For ease of configuring multiple
environments (development, production, testing), we do have separate files
for each.  See the ``backend/requirements/`` directory and note that each of
the environment-specific ```.txt`` files import all requirements from
``base.txt``.