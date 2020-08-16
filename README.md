## Introduction

* My name is Meg Regan and I'm a 2nd year data science student in NUIG, Ireland. 
* I created this project to learn Javascrip, HTML, HTTP and GCP while also providing some useful, up-to-date COVID 19 stats.
* I plan to expand this project by using machine learning to analyse the data I've collected. 
* Here's a high level picture of what the architecture looks like. 
![Architecture](www/images/architecture.png)
* Below are project details, resources and tutorials that I've used. 

## COVID 19 stats 
* [Postman COVID-19 API Resource Center](https://covid-19-apis.postman.com/)  
* [API used in project to get country COVID stats](https://documenter.getpostman.com/view/8854915/SzS7R74n?version=latest)
* [API used in project to get global COVID stats](https://documenter.getpostman.com/view/11144369/Szf6Z9B3?version=latest)

## JavaScript
* [JavaScript library to select country and region](https://github.com/benkeen/country-region-selector) 
* [How to do single page web app in JavaScript](https://itnext.io/build-a-single-page-web-app-javascript-and-the-dom-90c99b08f8a9)

## Flask
* [Flask tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
* how to run flask on localhost: 
 * export FLASK_APP=corona_stats
 * export FLASK_ENV=development
 * flask run

## GCP 
* [good tutorial about GCP](https://medium.com/@dmahugh_70618/deploying-a-flask-app-to-google-app-engine-faa883b5ffab)

## My GCP Project 
* Project name: meg-corona-stats
* [Project deployment](https://client-dot-meg-corona-stats.ew.r.appspot.com)
* [Link to project](https://console.cloud.google.com/home/dashboard?q=search&referrer=search&project=meg-corona-stats&folder=&organizationId=)
 * [deployment logs](https://console.cloud.google.com/logs/)
 * [GCP trigger to deploy on Git push](https://console.cloud.google.com/cloud-build/triggers?project=meg-corona-stats&folder&organizationId)
 * [mirrored GCP repo](https://source.cloud.google.com/meg-corona-stats/github_megregan_covid-stats)
 * [buids](https://console.cloud.google.com/cloud-build/builds?project=meg-corona-stats)
 * [GCP app engine](https://console.cloud.google.com/appengine?project=meg-corona-stats&serviceId=default)
* how to deploy at command line (no longer needed as git trigger used in deployment): 
 * gcloud app deploy app.yaml server.yaml client.yaml
 * gcloud app browse


## Git push related commands
* git clone https://github.com/megregan/covid-stats.git
* git add . 
* git commit -m "initial version" 
* git push

# HTML
* [HTML template used in project](https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_webpage&stacked=h)
* [Other HTML templates](https://www.w3schools.com/w3css/w3css_templates.asp)