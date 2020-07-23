---
title: Application Programming Interface
description: Getting started to create an API
---

You can create an application programming interface easily, and the gcp-flask-template
provides an easy example for doing this. For more detailed examples, see the [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html#) API documentation. If you need help
authenticating your API or adding addition views, please reach out to us at [Research Software Engineering Services](https://stanford-rc.github.io/rse-services/request).

## Creating your API

You have several ways that you might populate data for an API:

### Read only, small data
For data files that are relatively small, it's easy to read in text or data files to store in memory for the application to serve. This is the example that we provide in the [views/api.py](https://github.com/stanford-rc/gcp-flask-stanford/tree/master/gcpflask/views/api.py) by reading in a list of crayons from a csv file, and then
providing views to list or get a particular crayon by name.

### Read and Write
For most applications, you will want to create models that feed into the standard GET, POST, DELETE
views, possibly use [blueprints](https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html)
and add [authentication](https://flask-restful.readthedocs.io/en/latest/extending.html?highlight=authentication#resource-method-decorators). There is a nice tutorial [here](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful) for request argument parsing, and please
don't hesitate to reach out to [Research Software Engineering Services](https://stanford-rc.github.io/rse-services/request) if you want any help. If you are familiar with Swagger or want to make it easy to map models onto
API views, we recommend [Flask-Restplus](https://flask-restplus.readthedocs.io/en/stable/swagger.html).

## Using your API

Once your've started your development server:

```bash
python main.py
```

It's fairly easy to use standard curl to interact with your crayons API, and note
that you could also copy paste these endpoints into your browser to see the same data. Here
is how we can see an "index" of all endpoints:

```bash
$ curl http://127.0.0.1:8080/api/
{
  "/api/": "http://127.0.0.1:8080/api/", 
  "/api/crayons/": "http://127.0.0.1:8080/api/crayons/", 
  "/api/crayons/<string:name>/": "http://127.0.0.1:8080/api/<string:name>"
}
```

And a listing of all the crayons (truncated in the middle):

```bash
$ curl http://127.0.0.1:8080/api/crayons/
[
  {
    "hex": "EFDBC5", 
    "name": "Almond", 
    "rgb": "239,219,197", 
    "url": "http://127.0.0.1:8080/api/crayons/almond"
  }, 
  {
    "hex": "CD9575", 
    "name": "Antique Brass", 
    "rgb": "205,149,117", 
    "url": "http://127.0.0.1:8080/api/crayons/antique-brass"
  }, 
  {
    "hex": "FDD9B5", 
    "name": "Apricot", 
    "rgb": "253,217,181", 
    "url": "http://127.0.0.1:8080/api/crayons/apricot"
  }, 
...
  {
    "hex": "FC6C85", 
    "name": "Wild Watermelon", 
    "rgb": "252,108,133", 
    "url": "http://127.0.0.1:8080/api/crayons/wild-watermelon"
  }, 
  {
    "hex": "CDA4DE", 
    "name": "Wisteria", 
    "rgb": "205,164,222", 
    "url": "http://127.0.0.1:8080/api/crayons/wisteria"
  }, 
  {
    "hex": "FCE883", 
    "name": "Yellow", 
    "rgb": "252,232,131", 
    "url": "http://127.0.0.1:8080/api/crayons/yellow"
  }, 
  {
    "hex": "C5E384", 
    "name": "Yellow Green", 
    "rgb": "197,227,132", 
    "url": "http://127.0.0.1:8080/api/crayons/yellow-green"
  }, 
  {
    "hex": "FFB653", 
    "name": "Yellow Orange", 
    "rgb": "255,182,83", 
    "url": "http://127.0.0.1:8080/api/crayons/yellow-orange"
  }
]
```

And finally, using the url we find in one of our crayons above, we can retrieve
just that crayon. Note that it's customary to provide a subset of metadata for a list view,
and then more details for the single view (not shown here).

```bash
$ curl http://127.0.0.1:8080/api/crayons/yellow-orange/
{
    "url": "http://127.0.0.1:8080/api/crayons/yellow-orange/",
    "name": "Yellow Orange",
    "hex": "FFB653",
    "rgb": "255,182,83"
}
```

This is a fairly simple example, and it's likely you'll want to build upon this,
and add more complex views, more query parameters, and even DELETE and POST endpoints.
If you would like further detail for using or customizing an API, please don't hesitate to 
[open an issue](https://www.github.com/{{ site.github_repo }}/{{ site.github_user }}).
