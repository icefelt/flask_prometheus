# Python Application Monitoring examples using Graphite and StatsD (Push) and Prometheus (Pull)

This Python code should create three URL's on your local machine using flask. This code should also


This Python code creates a Flask web application and three routes or URL's. The URL's are 1) the base URL `/`, 2) a `/database/` route, and 3) a `/metrics/` route. More specifically, we use the Prometheus instrumentation library for Python `prometheus_client` to add the counter: `requests` with the description: `Application Request Count`, and the label: `endpoint`. We also simulate an expensive database operation, tracking the start time and end time, and sending them to a histogram with `prometheus_client`. We also use StatsD to import a counter that increases by 1 for each request.

Counter, Gauge, Summary and Histogram.
Daemon for easy but powerful stats aggregation



### Install

Clone the code repo to your local machine and enter the directory you created with this command
```bash
$ `git clone git@github.com:icefelt/python_prometheus_graphite_examples.git && cd python_prometheus_graphite_examples`
```

Expected Output
```bash
$ `git clone git@github.com:icefelt/python_prometheus_graphite_examples.git && cd python_prometheus_graphite_examples`
Cloning into 'python_prometheus_graphite_examples'...
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
remote: Enumerating objects: 1364, done.
remote: Counting objects: 100% (1364/1364), done.
remote: Compressing objects: 100% (1232/1232), done.
remote: Total 1364 (delta 154), reused 1307 (delta 114), pack-reused 0
Receiving objects: 100% (1364/1364), 4.22 MiB | 3.88 MiB/s, done.
Resolving deltas: 100% (154/154), done.
```

**To run this code, clone the repo locally and run this command**
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

**Upon success, navigate your web browser to three URL's in this order to validate**

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




How do you know your application is running?

How do you know your application is running at peak performance?

How do you know your application is running at peak performance without wasting money on unnecessary infrastructure or costs?

**Application monitoring** using `application metrics` can answer these questions. With good monitoring, you can also analyze long-term trends, compare over time or experiment groups, and build the foundation for alerts and dashboards. With good monitoring, visualization, alerts, and logging, you'll know the health of your application quickly through a dashboard, receive a page when it's not healthy, or troubleshooting through the logs to

When choosing `application metrics`, using [**The Four Golden Signals**](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/) From [Google's SRE Book](https://landing.google.com/sre/sre-book/toc/index.html) is a baseline for confidence my service or application has enough coverage.

**Latency** is the time is takes to service a request.

**Traffic** is a measure of how much demand is being placed on your system

**Errors** is rate of requests that fail, either explicitly (e.g., HTTP 500s), implicitly (for example, an HTTP 200 success response, but coupled with the wrong content), or by policy (for example, "If you committed to one-second response times, any request over one second is an error").

**Saturation** is a measure of how "full" your system is. A measure of your system fraction, emphasizing the resources that are most constrained (e.g., in a memory-constrained system, show memory; in an I/O-constrained system, show I/O).

Answering **What** is broken and **Why** maps to **Symptoms** versus **Cause**.

| **What** (Symptoms)| **Why** (Cause)|
|------|------|
|400 or 500 errors | Database severs are refusing connections|
|application response times slow | AWS SNS queue is not decreasing fast enough |


There are two main paradigms most monitoring services belong. These are services that either pull or push. Knowing whether pull or push is a better choice for a particluar situation is valuable. Noah et al. have examples with **Graphite and StatsD for Push** and **Prometheus for Pull.**

Graphite does not collect data. StatsD pushes the metrics via TCP or UDP, and Python has instrumentation options that allow us to aggregrate metrics over UDP and ship them to graphite.

**Prometheus is a great choice for short-lived data or data that frequently changes; whereas Graphite is better suited for long-term historical information.**






















**The first URL the prometheus-backed flask application**
http://127.0.0.1:5000/ - Displays `Development Prometheus-backed Flash App`

**The second URL is designed to fake a long database query we can monitor**
http://127.0.0.1:5000/database/ - Displays `Completed expensive database operation`

**The third URL displays our application metrics**
http://127.0.0.1:5000/metrics/ - Displays list of application metrics


How do you know your application is running?

How do you know your application at peak performance?

How do you know your application is running at peak performance without wasting money on unecessary infrastructure or costs?

**Application monitoring** can answer these questions. With good monitoring, you can also analyze long-term trends, compare over time or experiment groups, and build the foundation for alerts and dashboards.  

With good monitoring, alerts, visualization, and logging, you'll know the health of your application.

Answering **What** is broken and **why?** maps to **Symptoms** versus **Cause**.

| What (Symptoms)| Why (Cause)|
|------|------|
|400 or 500 errors | Database severs are refusing connections|
|application response times slow | AWS SNS queue is not decreasing fast enough |

There are two main paradigms most monitoring services belong. These are services that either pull or push. Knowing whether pull or push is a better choice for a particluar situation is valuable. Noah et al. have examples with **Graphite and StatsD for Push** and **Prometheus for Pull.**

Graphite does not collect data. StatsD pushes the metrics via TCP or UDP, and Python has instrumentation options that allow us to aggregrate metrics over UDP and ship them to graphite.

**Prometheus is a great choice for short-lived data or data that frequently changes; whereas Graphite is better suited for long-term historical information.**

This is code is from _Monitoring and Logging_ Chapter of the 'Python for Devops' book by Noah Gift, Kennedy Behrman, Alfredo Deza, and Grig Gheorghiu.
You can buy this book on Amazon here: https://www.amazon.com/Python-DevOps-Ruthlessly-Effective-Automation/dp/149205769X

I used learnings from the _Monitoring Distributed Systems_ Chapter of Google's 'Site Reliability Engineering' book by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Murphy.
You can read it online here: https://landing.google.com/sre/sre-book/toc/
You can buy this book from Amazon here: https://www.amazon.com/Site-Reliability-Engineering-Production-Systems/dp/149192912X/

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
