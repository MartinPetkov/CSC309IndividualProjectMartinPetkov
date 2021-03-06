# CSC309 Winter 2015: Individual Project - MartinPetkov
Github repo for the Individual Project component of CSC309 Winter 2015 at UofT St. George.

## General
URL of Repo: https://github.com/MartinPetkov/CSC309IndividualProjectMartinPetkov

This is a Django app, and the folder structure reflects this. It has one project called "ip" and one app called "ip\_app".

Currently it can only be run locally and requires having django installed.

Instructions for running:
* Install Django if not already installed, using the command: "sudo pip install Django"
* In the ip_app directory, run the following command: "python manage.py runserver"
* In a browser, go to: "localhost:8000/ip\_app"


## API Requests:
The two API requests are:
* /ip\_app/bestkideas/?api\_token=&lt;api\_token&gt;?&amp;k=&lt;k\_value&gt;&amp;from\_date=&lt;YYYY-MM-DD&gt;&amp;to_date=&lt;YYYY-MM-DD&gt;/
* /ip\_app/industryDistributionGraph/?api\_token=&lt;api\_token&gt;/  

Both API requests outlined in the instructions are GET requests that require an API token. Usually this would be secret but currently it is stored in the ip\_app/views.py file and is nothing more than a previously generate string or 40 random characters. The API request for the best k ideas in the date span returns JSON data while the one for the distribution by industries returns a URL to a world-readable Plotly bar graph. A file with sample cURL statements exists in the ip/ip\_app/ directory as an example.
