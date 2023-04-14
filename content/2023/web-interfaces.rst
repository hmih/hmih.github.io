Web Intefaces
================================

:date: 2023-04-13 11:30
:description: out of the tar pit

What is the high-level architecture behind a typical CRUD web application?

REST
####

.. image:: /images/rest-schema-crud.svg
  :alt: Typical REST architecture with a SPA and a relational database

In the diagram we see the following:

* UI has a set of DTOs that are presented to the customer.

* REST endpoints are an informal interface between the UI and the server.

* Backend has a set of DTOs that both validate the data from the UI and
  transform the inputs into a suitable form for the relational database.

* The schema of the database contains for the final result from the client
  interaction.

There are several components to keep in sync, otherwise the application will
crash at runtime:

#. REST interface - This is the router exposed by the backend and consumed by
   the facade. Almost always these are two sets of strings that must be kept in
   sync. Add a slash, parameter, or letter to one but forget the other and you
   will be sent to the JIRA mines.

#. DTOs - There are two sets of objects to synchronize. Even more room for
   entity definitions to drift or accrue edge case logic that results in
   special handling of values that are externally insible to *any* of the
   *three* sides.

#. Relational Schema - The source of truth, or so we think. It's completely
   disconnected from the other two sets of entities and the exposed router.

What are the alternatives?

gRPC
####

.. image:: /images/grpc-schema-crud.svg
  :alt: gRPC based service that shares DTOs with the facade and the backend

I have written several gRPC-based CRUD applications that use a Protobuf
definition to generate: 1) DTOs for the facade, 2) DTOs the backend, 3) routing
layer between the two. This is a good solution to entity drift and
synchronization. The database can immediately map rows into DTOs that get
filterd and sent directly to the UI. The additional benefit of this is not
writing your own router. Just through auto-completion you will get type safe
routes that will never request a non-existing endpoint.

However, the database schema might drift, so Protobuf messages must be kept
synchronized with the database columns and types. The problem is that Protobuf
is not suited for relational data. The format lacks the semantics to express
the intent. The issue is fundamental to mapping relational to non-relational
data. Perhaps the code-first approach has run its course.

What if we start from the database?

PostgREST
#########

PostgREST is a program that runs on top of a PostgreSQL database and exposes
the schema as a set of REST API endpoints. Having written a PostgREST-based
service that constructs and analyzes time series data I can say it works very
well. There is no backend synchronization to keep track of, and there is an
option to expose an OpenAPI specification from the REST API. This allows the
client to construct a router with DTOs on demand, meaning that we get a type
safe router.

.. image:: /images/postgrest-schema-rest.svg
  :alt: PostgREST architecture

There is a whole section in the PostgREST documentation about authentication,
security, users, etc. But they've thought about it and it's impressive how I
was able to push the product using stored procedures and basic SQL.

My only issue is that stored procedures are not very popular. Writing out your
backend logic in a language few people get and maintain will cause headaches
down the road. It would be easier to handle some of the essential business
logic in a regular programming language like C# or Python. Luckily PostgreSQL
has several plugin which allow writing stored procedures in your language of
choice.

What about versioning? How about unit testing? Well, I never wrote any
¯\\_(ツ)_/¯ Even stimulants fail to capture the adrenaline rush of executing
destructive queries on production. You think to yourself: "Did I put this in a
transaction?". Those were the days.
