Title: My New Website: epidemic.co.il
Date: 2018-12-09 21:00
Modified: 2018-12-09 21:00
Status: published
Category: Web
Tags: bokeh, health, open data
Slug: introducing-epidemic
Author: Dean
og_image: img/img_posts/epidemic.png

My new website [Epidemic](http://www.epidemic.co.il) (Hebrew) is up and running.  
Epidemic is an open data public health project focused on making disease data accessible to the public.
The website uses mainly Bokeh with some basic css and javascript, and has many options such as:  

* Viewing disease progression chart for dozens of disease
* Viewing disease progression by regions in the country
* Downloading data as machine-readable CSVs
* Viewing disease information
* Dynamic ranges
* Bar chart to easily understand aggregated cases by region

I am really proud of this project as the Israeli Ministry of Health serves this data in a non friendly website with
many messy Excel files. The first part of this project was to crawl the website and get the data.
This project is in my [github](https://github.com/DeanLa/imoh) and is free for use.
The second part is the Bokeh server on top of this crawler, which has taught my a lot. I will hopefully show some the
things I've learned in future posts.
