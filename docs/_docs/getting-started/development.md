---
title: Development
description: Cloning the repository and browsing views
---

# Getting Started

This guide includes setup, configuration, and basic development steps.

## Setup

You will want to follow the instructions [here](https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service)
and:

 - create a Google Cloud Project, you can request one at Stanford [here](https://stanford.service-now.com/it_services?id=sc_cat_item&sys_id=fa9f80bddbf05b401df130cf9d96198b)
 - install the gcloud command line client and Python3+
 - authenticate on the command line with `gcloud auth application-default login`

For example, after I've created my project and I've installed gcloud, I might login and
then set the default project to be my new project:

```bash
$ gcloud auth application-default login
$ gcloud config set project <myproject>
```

## Config

In the [config.py](config.py) file, you can define as many or
as few of the custom variables (e.g., a Twitter alias) as you like. These are
rendered in various pages by default. You can also choose to disable authentication
with `disable_auth = True`.

## Development

To develop locally, you'll want to create a local environment and then install
dependencies to it.

```bash
python -m venv env
source env/bin/activate
pip install  -r requirements.txt
```

Then you will want to copy the .example-env file to .env, populate it with your secrets,
and source it:

```bash
source .env
```

And then to run the application locally, issue this command:

```bash
python main.py
```

And then you can open up your browser to [http://localhost:8080](http://localhost:8080).
The main index view is a small portal to direct you to views and features available.

![{{ site.baseurl }}/assets/images/stanford-flask-templates.png]({{ site.baseurl }}/assets/images/stanford-flask-templates.png)

## Testing

A set of example tests are provided in [test_gcpflask.py](https://github.com/stanford-rc/gcp-flask-stanford/blob/master/test_gcpflask.py), and you can read more about testing in flask [here](https://flask.palletsprojects.com/en/1.1.x/testing/). You can run local testing with pytest as follows:

```bash
pytest -sv test_gcpflask.py
```

## Deployment

The instructions here will show you how to deploy on Google App Engine (not written yet).

**under development**
