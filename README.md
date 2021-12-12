<h1>Testing with Hypothesis</h1>

<h2>Getting Started</h2>

---

```
pip install -r requirements
```

In my experience, hypothesis is automatically picked up by pytest as a plugin; works out of the box when running pytest with a simple pip install.

` `  

<h2>Strategies</h2> 

---

A strategy is a way of generating data that makes your code sad. Strategies will automatically try to shrink as they generate, to distill the simplest example that most succinctly demonstrates how wrong you were.

* [Basic strategies](https://hypothesis.readthedocs.io/en/latest/data.html)
* Working with times & timezones
* [Composite strategies](https://hypothesis.readthedocs.io/en/latest/data.html#composite-strategies), Drawing, and [Assumptions](https://hypothesis.readthedocs.io/en/latest/details.html#hypothesis.assume)
* [Extended strategies](https://hypothesis.readthedocs.io/en/latest/numpy.html) (numpy, pandas; not covered)

` `  

<h2>Health Checks</h2>

---

A health check is a reminder that your code is sad and also not smart.

* [How to ignore them](https://hypothesis.readthedocs.io/en/latest/healthchecks.html)
* When to ignore them

` `  

<h2> Useful Hypothesis Settings </h2>

---

Settings are a way of making your code sad in a reproducible way.

* [Basic settings](https://hypothesis.readthedocs.io/en/latest/settings.html)
* [Settings profiles](https://hypothesis.readthedocs.io/en/latest/settings.html#settings-profiles)


` `  

<h2> Example </h2>

---

Suppose you have a class with some attributes, including a ```name``` (a str), a ```start``` and ```end``` value (datetime.datetime), and an ```action``` (float).

In this example, you've already written some validators, which will ensure that the user cannot give any silly inputs when creating an instance of your class.