# **Querying Tutorial**

## Let's get started

This tutorial will show you how to send simple search query to the Retail Service and analyze the response

**Time to complete**: About 1 minute

## Before you begin

To run Python code samples from this tutorial you will need to setup your virtual environment.

Please use this commands in a terminal:
```bash
pip install virtualenv
```
```bash
virtualenv <your-env>
```
```bash
source <your-env>/bin/activate
```

Now install google packages:
```bash
pip install google
```
```bash
pip install google-cloud-retail
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal to run it.

## Simple query request

The simple search request contains only required fields which are: 
  - ```placement``` - The resource name of the search engine placement
  - ```visitor_id``` - A unique identifier for tracking visitors
  - ```query``` - Raw search query or search phrase

There is a request ready to be run on a catalog full of different products, so you will see the results right away, 
but first please open the **search_simple_query.py** to review the request.

To send this request to the search service, open a terminal and run:
```bash
python search_simple_query.py 
```

## Simple query. Response analyze

Now in a field **```results[]```** you can see A list of matched items returned by Retail Search service.

**```total_size```** it's the estimated total count of matched items.

**```attribution_token```** it's a unique search token which enables accurate attribution of search model performance.

**```next_page_token```** A token that points to the next page in the search response. By default the number of products per page is 100. If this field is omitted, there are no subsequent pages.

## Success 

You have complete the tutorial and now we **encourage** you to **test the search by yourself**, right here in the CloudShell environment, using different search queries.

**Thank you for compleating this tutorial!**





