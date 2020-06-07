# Application Monitoring with Flask and Prometheus wth Python
This code is taken from the _Monitoring and Logging_ chapter of the 'Python for Devops' book by Noah Gift, Kennedy Behrman, Alfredo Deza, and Grig Gheorghiu. 

This python code shows you how to setup prometheus using flask.

How do you know your application is running?

How do you know your application at peak performance? 

How do you know your application is running at peak performance without wasting money on unecessary infrastructure or costs? 

**Application monitoring** can answer these questions. With good monitoring, you can also analyze long-term trends, compare over time or experiment groups, and build the foundation for alerts and dashboards.  

I'm not necessarily writing about CPU, memory or hard drive space. We'd like to abstract that infrastructure layer away and not really worry about it. 
I'm writing about finding the bottlenecks or in your application that may eventually cause performance issues, or even outages. 
For example, if find performance issues and your application has a queue, you could monitor the size of the queue or the rate the queue is increasing or decreasing. 
Another example is you could ping the domain name and/or path of your website. A better test may be checking for specific html text near the end of a page. This way you'll know if your website is rendering, and you'd catch errors with nginx, apapvhe, or whatever web server you're using.
With good monitoring, alerts, visualization, and logging, you'll know the health of your application. 

Answering **What** is broken and **why?** maps to **Symptoms** versus **Cause**. 

| What (Symptoms)| Why (Cause)|
|------|------|
|400 or 500 errors | Database severs are refusing connections|
|application response times slow | AWS SNS queue is not decreasing fast enough |

There are two main paradigms most monitoring services belong. These are services that either pull or push. Knowing whether pull or push is a better choice for a particluar situation is valuable. Noah et al. have examples with **Graphite and StatsD for push** and **Prometheus for pull.** 

Graphite does not collect data, StatsD pushes the metrics via TCP or UDP, and Python has instrumentation options that allow us to aggregrate metrics over UDP and ship them to graphite. 

**Prometheus is a great choice for short-lived data or data that frequently changes; whereas Graphite is better suited for long-term historical information.**

This is code is from _Monitoring and Logging_ Chapter of the 'Python for Devops' book by Noah Gift, Kennedy Behrman, Alfredo Deza, and Grig Gheorghiu. 
You can buy this book on Amazon here: https://www.amazon.com/Python-DevOps-Ruthlessly-Effective-Automation/dp/149205769X

I used learnings from the _Monitoring Distributed Systems_ Chapter of Google's 'Site Reliability Engineering' book by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Murphy. 
You can read it online here: https://landing.google.com/sre/sre-book/toc/
You can buy this book from Amazon here: https://www.amazon.com/Site-Reliability-Engineering-Production-Systems/dp/149192912X/

