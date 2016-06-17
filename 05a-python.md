# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are pretty similar, but the big disitinguishable difference is that tuple values cannot be changed, while lists are mutable. Tuples also tend to have a heterogeneity, while lists tend to be more homogenous. Therefore, tuples work better as keys in a dictionary because they do not change and can represent a complex concept with heterogeneous information in one contained data structure (similar to structs in C++). For example, one could use a tuple of coordinates as a key for a particular location.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Unlike lists, sets have unordered values and therefore, do not have an index because they use a hash lookup so they require all items in list to be hashable. Sets also cannot have duplicate data and can perform operations like union, intersectinoe, difference, and symmetric difference. For example, you would use a set to keep track of the different cities that an airline goes to, but you would use a list to keep track of the order of cities in a flight trajectory. Performance is substantially faster in sets for finding an element in the structure because it uses a hash table to determine if an item is contained in the set. But, sets are slower than lists when iterating through the contents since there is no indexing. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda serves as a tool to build an anonymous, single expression function that allows the easy incorporation of function objects in a setting that requires them. The contained expression is always returned. For example, it is commonly used in GUI callbacks that require a function object as in the Tkinter Button command attribute: tk.Button(frame, text = "1", command = lambda: self.printNum(1)). In 'sorted', 'key' uses a function as a comparison key from each element in a list. For example sorted(list, key = lambda x: x[2]) would sort by the second element in a list of tuples. 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is the concept of transforming one list into another list using principles from mathemetical set notation. All comprehensions can be written out as for loop.
* List comprehension to find names that start with S: 
s_list = [n for n in names if n.startswith('S')]
* Filter for findings names that start with S:
s_filter = filter(lambda n: n.startswith('S'),names)
* Set comprehension to find names that start with S:
s_set = {n for n in names if n.startswith('S')}
* Dictionary comprehension for keys that start with S:
s_dict = {k:v for k,v in names.iteritems() if k.startswith('S')}

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





