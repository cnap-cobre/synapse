############################
Primer on Docker and Compose
############################

`Intended Audience: Developers who are less familiar with Docker.  If you
have worked with Docker in the past, feel free to skip ahead.`

Docker
------

To simplify the way we specify our project's execution environment, we will be
using Docker containers.

A container is a lot like a virtual machine...it provides an isolated
environment for code to execute.  Virtual machines are an abstraction of
physical hardware.  Each VM runs a full copy of an operating system with one or
more applications and can have a footprint of many GBs.  A container is lighter
weight.  Containers are an abstraction at the application layer which package
code and dependencies together.  All containers share the host OS's kernel.
Because they are lighter weight, they take up less space (MBs rather than GBs)
and have much faster startup times.

What is most important about containers (Docker, specifically) is that they are
immutable infrastructure.  By default, files saved to the filesystem inside of
a container are `not` persisted across restarts of the container.  While this
sounds like a weakness, it is a strength.  Default immutibility encourages us
to store data in a database where it belongs.  By not preserving any state
across restarts, containers are `predictable`.  Because they isolate their
filesystem, networking, process, and other system namespaces, they are
`portable`.  If an application runs in a container version on your PC, it will
run on my Mac.  While immutibility is default, we can specify persistant data
"volumes" which are mounted onto the container's filesystem.  We can also
set up bindings from the host filesystem to the container's.

Docker containers are specified in a ``Dockerfile``.  Typically these start
with pulling down Docker base image.  For example, ``FROM ubuntu:17.10``.  From there,
dependencies are installed, and application code is copied into the container.


Docker Compose
--------------

In a microservices architecture, an application takes the form of many small,
loosely coupled components, each of which has a single, focused job.  Docker
pairs nicely with this style of application.  Each microservice runs in its
own lightweight container.

To orchistrate the running of two or more containers and specifty the
networking between them as well as with the outside world, we use Docker
Compose.  See the ``docker-compose.yml`` file at the root of the repository for
and example.

In our case, we have the following containers:

* db: Runs PostgreSQL
* backend: Runs our Django application
* frontend: Builds and serves our frontend React application
* webserver: Proxies incoming requests (details vary between dev. and prod.)

Further down the road, there will likely be more containers as data modeling,
image processing, and collaboration tools are added.


Python Virtual Environments
---------------------------

(We're not using them.  Read on...)

Imagine a scenario where you are working on two seperate projects.  Your first
project requires Django version 1.09 while your second project requires
Django version 2.0.  Ordinarily, your system can only have one version of
Django installed at a time because packages are globally installed.

Virtual Environments solve this proble by creating a local directory where
copies of your project's dependencies are stored.  When keeping your code in a
Git repository, the convention is to write a ``requirements.txt`` file that
lists your project's dependencies while leaving the dependencies themselves
out of the repo.  If a friend wants to clone your repository and run your
project, all they would need to do is create and enter a new virtual
environment, run ``pip install -r requirements.txt`` to install the
dependencies to that virtual environment, and they are good to go.

Once you are done working on a project, you can exit the virtual environment.
Your global python package directory remains untouched.

**For our purposes, we will not need virtual environments because the Docker
container already provides the encapsulation we are looking for.**  We do,
however, have a ``requirements.txt``.  Really, we have a requirements
directory with seperate files for development and production environments.  See
``backend/requirements/`` for details.
