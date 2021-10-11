# **Boosting Tutorial**

## Let's get started

The boosting is a powerful and convenient feature, it allows you to preoritize products which corresponds some condition.
To specify the condition you can use the filtering expressions.

The boosting specfication can be based on single field condition or multiple fields. You also can combine several specifications within one boosting request.

In this tutuorial you will see a couple of examples of products boosting, so let's start


**Time to complete**: About 4 minutes

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


## Boosting by one creteria

The boosting specification looks like that:
  
  ```condition_boost_specs {
         condition: string
         boost: double [-1;1]
    }```

To set the **```condition```** you should use a filtering expression, like:

```'(colorFamily: ANY("black"))'```  or  ```'(rating: IN(4.0, 5.0))'```

More detailed information about the filtering expressions can be found in [Retail API documentation](https://cloud.google.com/retail/docs/filter-and-order#filter) 

The field **```boost```** defines the strength of the condition boost, which should be in [-1, 1]. Negative boost means demotion.

To see the whole request with a product boosting open **search_with_boosting.py**

Run it in a terminal with a command:
```bash
python search_with_boosting.py
```

Now you can check the ```results[]```, the poducts which corresponds the boost condition became reranked.

Please note, that setting boost strength to 1.0 gives the item a big promotion. However, it does not necessarily mean that the boosted item will be the top result at all times, nor that other items will be excluded. 
Results could still be shown even when none of them matches the condition. And results that are significantly more relevant to the search query can still trump your heavily favored but irrelevant items.

You can combine up to 10 boost specifications in one search request. So that you may apply really sophisticated boosting rules to your search request.

## Success 

You have complete the tutorial and now we **encourage** you to **test the filtering by yourself**, try different combinations of different filter expressions.

**Thank you for compleating this tutorial!**
