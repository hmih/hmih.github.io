Kubernetes DevEx
================

:date: 2024-05-26 17:45
:description: kubernetes, dev ex, programming
:status: draft

Problem
-------

You have the following setup:

1. Microservice architecture on top of Kubernetes (local single node cluster)
2. A set of with services, eg. **api**, **ui**, **shop**, and a database running inside the cluster
3. A single domain **\*.web.local** which is responsible for the services - eg. **api.web.local**, **db.web.local**, etc.

What's the most egonomic way to work with this setup?

These are the constraints of the solution:

1. Run **any** of the microservices with a from your IDE and have bidirection communication with the services in the cluster

   For example, programmer puts a breakpoin and starts the process, then any
   service in the cluster must detect the new process and send requests to the
   **localhost** service rather than the one running inside Kubernetes.

2. A mocked service does not require changing other services

   If a new **api.web.local** service is started on localhost, then other
   Kubernetes services must send queries to **api.web.local**. The queries must
   resolve to the new process. This must work with HTTPS.

3. Avoid changes to the existing Kubernetes resource files

   Avoid rewriting most Kubernetes resources to accomodate the solution. This
   avoid future maintenance too.

Solution
--------

It's somewhat complicated so lets bring in the elements one by one. First of all, our Kubernetes cluster.

.. figure:: /images/k8s-devex-p1.svg

   Isn't he lovely?
