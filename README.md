# Python Application Monitoring examples using Graphite and StatsD (Push) and Prometheus and prometheus_client (Pull)

---------------------------------------------------------------------

### Purpose

This Python code creates a [Flask](https://palletsprojects.com/p/flask/) web application with three routes or URL's.
1. http://127.0.0.1:5000/ - Displays `Development Prometheus-backed Flash App`
1. http://127.0.0.1:5000/database/ - Displays `Completed expensive database operation`
1. http://127.0.0.1:5000/metrics/ - Displays list of application metrics, like `total number of requests` and `number of slow database requests`

This code uses `python-statsd` [StatsD](https://github.com/statsd/statsd) to push application metrics to [Graphite](https://graphiteapp.org/).  This code also uses `prometheus_client` [Prometheus Python Client](https://github.com/prometheus/client_python), a prometheus instrumentation library for Python applications. 

---------------------------------------------------------------------

### Install

**To install this code, clone [the repo](https://github.com/icefelt/python_prometheus_graphite_examples) locally and enter the directory you created.**
```bash
$ git clone git@github.com:icefelt/python_prometheus_graphite_examples.git && cd python_prometheus_graphite_examples
```

---------------------------------------------------------------------

**The expected outout includes**
```bash
$ git clone git@github.com:icefelt/python_prometheus_graphite_examples.git && cd python_prometheus_graphite_examples
Cloning into 'python_prometheus_graphite_examples'...
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
remote: Enumerating objects: 1364, done.
remote: Counting objects: 100% (1364/1364), done.
remote: Compressing objects: 100% (1232/1232), done.
remote: Total 1364 (delta 154), reused 1307 (delta 114), pack-reused 0
Receiving objects: 100% (1364/1364), 4.22 MiB | 3.88 MiB/s, done.
Resolving deltas: 100% (154/154), done.
```

---------------------------------------------------------------------

**To run this code, clone [the repo](https://github.com/icefelt/python_prometheus_graphite_examples) locally and run this command**
```bash
$ FLASK_APP=web.py flask run
```
**The expected output includes**
```bash
$ FLASK_APP=web.py flask run
 * Serving Flask app "web.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

**Upon successful installation, navigate your web browser to three URL's to validate**

http://127.0.0.1:5000/ - Displays `Development Prometheus-backed Flash App`

http://127.0.0.1:5000/database/ - Displays `Completed expensive database operation`

http://127.0.0.1:5000/metrics/ - Displays list of application metrics

To validate the metrics,
1. navigate to the base URL (http://127.0.0.1:5000/)
2. navigate to the database page (http://127.0.0.1:5000/database)
3. navigate to the metrics page (http://127.0.0.1:5000/metrics)

The metrics page should now include both `total number of requests` and `number of slow database requests`

**The total number of requests** on http://127.0.0.1:5000/
```
# TYPE requests_total counter
requests_total{endpoint="/"} 20.0
```
**The number of slow database requests** as determined by http://127.0.0.1:5000/database/
```
# TYPE slow histogram
slow_count{endpoint="/database"} 6.0
```

---------------------------------------------------------------------

There are two main paradigms most monitoring services belong. These are services that either pull or push. Knowing whether pull or push is a better choice for a particluar situation is valuable. Noah et al. have examples with **Graphite and StatsD for Push** and **Prometheus for Pull.**

Graphite does not collect data. StatsD pushes the metrics via TCP or UDP, and Python has instrumentation options that allow us to aggregrate metrics over UDP and ship them to graphite.

**Prometheus is a great choice for short-lived data or data that frequently changes; whereas Graphite is better suited for long-term historical information.**

---------------------------------------------------------------------

This code is from the _Monitoring and Logging_ chapter of the ["Python for DevOps"](https://www.amazon.com/Python-DevOps-Ruthlessly-Effective-Automation/dp/149205769X) book by Noah Gift, Kennedy Behrman, Alfredo Deza, and Grig Gheorghiu. [You can buy this book on Amazon](https://www.amazon.com/Python-DevOps-Ruthlessly-Effective-Automation/dp/149205769X)

I used learnings from the _Monitoring Distributed Systems_ Chapter of Google's ["Site Reliability Engineering"](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/) book by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Murphy. You can read it online here: [https://landing.google.com/sre/sre-book/toc/](https://landing.google.com/sre/sre-book/toc/). [You can also buy this book on Amazon](https://www.amazon.com/Site-Reliability-Engineering-Production-Systems/dp/149192912X/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
