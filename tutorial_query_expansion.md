# **Query Expansion Tutorial**

## Let's get started

This tutorial will show you how to enable the query expansion feature, which allows you to increases the recall for query terms with few results,
especially long tail queries.

If the query expansion disabled, only the exact search query is used, even if total size of search result is zero.

Enable query expansion feature and let Google Retail Search ti build an automatic query expansion.

You can also pin unexpanded products so they will always be at the top of the search results, followed by the expanded results

This is really usefull feature thet helps you to enchance customer expirience. So let's look at it closely


**Time to complete**: About 2 minutes

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


## Query expansion

Open **search_with_query_expansion_spec.py**, take a look at the search request, here you see the query expansion condition set with value "AUTO",
that means the query expansion feature is turned on and the search results will be expanded.

Run the sample in a terminal with a command:
```bash
python search_with_query_expansion_spec.py
```

Now you can see the ```results[]``` has products which does not exactly match the search query but are really close to it

Next let's change the condition value to "DISABLED"

Just find the comment 

 # [TRY DIFFERENT QUERY EXPANSION CONDITION HERE:] 

and change the condition to: 
```condition = SearchRequest.QueryExpansionSpec.Condition.DISABLED```

Run the sample in a terminal with a command:
```bash
python search_with_ordering.py
```

Now you see the results contains only items with exact match

## Ordering by multiple fields

Ordering by multiple fields is supported through the use of comma-separated fields in order of priority. 

The lower priority fields will be used to order items with equal values for higher priority fields. 


For example, **```rating desc, price```** would order items by their rating first, then the products with the same rating will be ordered by price.

To try that, please change the ordering expression to:
```
order = 'rating desc, price'
```

Run the code sample in a terminal using command:
```bash
python search_with_ordering.py
```

## Success 

You have complete the tutorial and now we **encourage** you to **test the query expansion by yourself**, try different search phrases with and without query expansion

**Thank you for compleating this tutorial!**
