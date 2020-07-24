---
title: Templates and Features
description: Templates and Features available
---

# Features

Features include:

 - [several branded themes to choose from](#templates)
 - a basic user and registration model
 - [a restful API example](api)
 - several database options, sqlite, postgres and mysql
 - examples of testing for your code

Details about templates are included below. If you would like further detail
for using or customizing any of the features above, please don't hesitate to 
[open an issue](https://www.github.com/{{ site.github_repo }}/{{ site.github_user }}).


# Templates

The gcp flask application provides several templates and examples for you to start work
for your project! If you need any help, please don't hesitate to [open an issue](https://github.com/stanford-rc/gcp-flask-stanford/issues)
or reach out to [Research Software Engineering Services](https://stanford-rc.github.io/rse-services/request).

## Single Page

It's a common use case to want to quickly deploy a single page portal to share a project description, collaborators,
and perhaps some results. The single page template provides an example of that, using [Chart.js](https://www.chartjs.org/) to render
a plot of data. See the [visualization](#visualization) section for quick tips on different strategies to create charts.

**top**

The top of this template can proudly show a title for your page, and quick description:

![{{ site.baseurl }}/assets/images/singlepage/top.png]({{ site.baseurl }}/assets/images/singlepage/top.png)

<br>


**navigation**

The navigation bar is sticky, meaning that it moves with the page. Here we scroll to the collaborators section
and the navigation bar moves with us.

![{{ site.baseurl }}/assets/images/singlepage/nav.png]({{ site.baseurl }}/assets/images/singlepage/nav.png)

<br>


**tool**

Finally, the main tool shows an interactive chart, courtesy of Chart.js. You could imagine having a tool, form,
or other analysis write up here.

![{{ site.baseurl }}/assets/images/singlepage/tool.png]({{ site.baseurl }}/assets/images/singlepage/tool.png)

<br>



## Cardinal Theme

The [Stanford Cardinal Theme](http://web.stanford.edu/group/webdev/cardinal/) provides you with standard views for:

**home**

![{{ site.baseurl }}/assets/images/cardinal/home.png]({{ site.baseurl }}/assets/images/cardinal/home.png)

<br>

**right sidebar**

![{{ site.baseurl }}/assets/images/cardinal/right-sidebar.png]({{ site.baseurl }}/assets/images/cardinal/right-sidebar.png)

<br>

**left sidebar**

![{{ site.baseurl }}/assets/images/cardinal/left-sidebar.png]({{ site.baseurl }}/assets/images/cardinal/left-sidebar.png)

<br>

**no sidebars**

![{{ site.baseurl }}/assets/images/cardinal/no-sidebars.png]({{ site.baseurl }}/assets/images/cardinal/no-sidebars.png)

<br>

**two sidebars**

![{{ site.baseurl }}/assets/images/cardinal/two-sidebars.png]({{ site.baseurl }}/assets/images/cardinal/two-sidebars.png)

<br>

**wide**

![{{ site.baseurl }}/assets/images/cardinal/wide.png]({{ site.baseurl }}/assets/images/cardinal/wide.png)


Along with login and registration views.

**login**

![{{ site.baseurl }}/assets/images/cardinal/login.png]({{ site.baseurl }}/assets/images/cardinal/login.png)

<br>

**register**

![{{ site.baseurl }}/assets/images/cardinal/register.png]({{ site.baseurl }}/assets/images/cardinal/register.png)

<br>



## Visualization

For visualization, you can generally take a few approaches:

 1. Render plots on the server side and display them as png images
 2. Generate data on the server side and send to a front end view
 3. Embed both data and JavaScript in the front end to generate a visualization

For point 2, this could either be done with templating, or a more interactive get/post request
to customize data for the user. If you would like help with any of these approaches, please
reach out to [Research Software Engineering Services](https://stanford-rc.github.io/rse-services/request).

## Extra Features

The following extra features might be useful to you, and if you would like help to develop
them for your application, please reach out to [Research Software Engineering Services](https://stanford-rc.github.io/rse-services/).

 - **Custom Search** of pages or models (the current search goes to Stanford search)
 - **Social Authentication** for login with social identities such as Twitter, Google, Globus, etc.
 - **SAML authentication** for more specific Stanford-only access.
