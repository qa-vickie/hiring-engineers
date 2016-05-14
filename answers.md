#Level 1 - Collecting your Data#

**•	Sign up for Datadog (use "Datadog Recruiting Candidate" in the "Company" field), get the Agent reporting metrics from your local machine.**

To see a metric from my local machine please see a screenshot below or click [here] (https://app.datadoghq.com/metric/explorer?live=true&page=0&is_auto=false&from_ts=1463179182357&to_ts=1463182782357&tile_size=m&exp_metric=system.cpu.system&exp_scope=qa_vickie_tag&exp_group=host&exp_agg=avg&exp_row_type=metric) 

![metric-system.cpu.system](/qa.vickie/images/metric1.png)

**•	Bonus question: In your own words, what is the Agent?**

>The Datadog Agent is piece of software that runs on my hosts and collects events and metrics for the easier way to monitor them. The Agent has three main parts: the collector, dogstatsd, and the forwarder. Each part does its own job:
>>1.	The collector runs checks on the current machine for whatever integrations the user has and it will capture system metrics like memory and CPU.
>>2.	Dogstatsd is a statsd backend server you can send custom metrics to from an application.
>>3.	The forwarder retrieves data from both dogstatsd and the collector and then queues it up to be sent to Datadog.

**•	Add tags in the Agent config file and show us a screenshot of your host and its tags on the Host Map page in Datadog.**

To see the Dashboard itself, the host and its tag please see a screenshot below or click [here] (https://app.datadoghq.com/dash/131804/testdash?live=true&page=0&is_auto=false&from_ts=1463091670112&to_ts=1463178070112&tile_size=m)

![the host and its tag](/qa.vickie/images/metric2.png)

**•	Install a database on your machine (MongoDB, MySQL, or PostgreSQL) and then install the respective Datadog integration for that database.**

 >(Please see a screen print and the URL above)
 
**•	Write a custom Agent check that samples a random value. Call this new metric: test.support.random**

>(Please see a checked in code vickie_test.py)

Here is a link on a Dashboard TestDash to [a newly added metric test.support.random] 
(https://app.datadoghq.com/dash/131804/testdash?live=true&page=0&is_auto=false&from_ts=1463091670112&to_ts=1463178070112&tile_size=m)

![metric-test.support.random](/qa.vickie/images/picture3.png)

#Level 2 - Visualizing your Data#

######Since your database integration is reporting now, clone your database intergration dashboard and add additional database metrics to it as well as your test.support.random metric from the custom Agent check.

To see a cloned dashboard and additional database metrics please see a screenshot below or click [here] (https://app.datadoghq.com/dash/list)

![cloned Dashboard and additional database metrics ](/qa.vickie/images/picture4.png)
 
**•	Bonus question: What is the difference between a timeboard and a screenboard?**

>There are two types of dashboards: TimeBoard and ScreenBoard. 
>>On a timeboard all graphs scopes to the same time. For example: The Past Day. Graphs will always appear in a grid-like fashion. This makes them generally better for troubleshooting and correlation. Also graphs on a timeboard can be shared individually. A user can edit or share any graph on a timeboard, by using a pencil icon in the top right corner of the graph and going from there.
A screenboard is flexible, far more customizable and is great for getting a high-level look into a system. It is created with drag-and-drop widgets, which can each have a different time frame. A screenboard can be shared as a whole because it is a live and read-only entity. Sharing can be done by using a cog icon in the top right corner of the dashboard and selecting a ‘Generate public URL’ option from the menu. That URL will give read-only access to just the content of that particular screenboard.

**•	Take a snapshot of your test.support.random graph and draw a box around a section that shows it going above 0.90. Make sure this snapshot is sent to your email by using the @notification**

![a snapshot of the box around the section in question](/qa.vickie/images/picture5a.png)

#Level 3 - Alerting on your Data#

######Since you've already caught your test metric going above 0.90 once, you don't want to have to continually watch this dashboard to be alerted when it goes above 0.90 again. So let's make life easier by creating a monitor.######

**•	Set up a monitor on this metric that alerts you when it goes above 0.90 at least once during the last 5 minutes**

![an email alert I've got](/qa.vickie/images/picture6.png)

**•	Bonus points: Make it a multi-alert by host so that you won't have to recreate it if your infrastructure scales up.**

Please click [here] (https://app.datadoghq.com/monitors#616500/edit) to see the details of the monitor settings

![a multi-alert by host](/qa.vickie/images/picture7.png)

**•	Give it a descriptive monitor name and message (it might be worth it to include the link to your previously created dashboard in the message). Make sure that the monitor will notify you via email.**

![a descriptive monitor name and message](/qa.vickie/images/picture8.png)

**•	This monitor should alert you within 15 minutes. So when it does, take a screenshot of the email that it sends you.**

![an email alert I've got for a multi-alert monitoring](/qa.vickie/images/picture9.png)

**•	Bonus: Since this monitor is going to alert pretty often, you don't want to be alerted when you are out of the office. Set up a scheduled downtime for this monitor that silences it from 7pm to 9am daily. Make sure that your email is notified when you schedule the downtime and take a screenshot of that notification.**

![a scheduled downtime for this monitor](/qa.vickie/images/picture10.png)

![a scheduled downtime for this monitor - settings](/qa.vickie/images/picture10A.png)



##QA Notes
1.	To set up monitoring of my metrics, I followed steps from the following [link] (http://docs.datadoghq.com/guides/monitoring/). After I clicked a Save button I did not get any indication that monitoring was saved and the Save button was still enabled. Making changes to the previously set up monitor, I am getting a notification of a successful update but the Saved button was still enabled. 
2.	I did not get an email as requested. Please see a screenshot for more information
![a screenshot from the real time graph annotation](/qa.vickie/images/picture5a.png)
3. There are a few typos in the documentation:
_The word “Navigate” is spelled as “Nagivate” under the title Creating Monitor_ [here](http://docs.datadoghq.com/guides/monitoring/)
4. The **Is there a way to share graphs?** section of FAQ contains a few [typos] (http://docs.datadoghq.com/faq/)
  1. The word 'cog' appears when 'pencil icon' is expected.
  2. There are only two buttons in the upper right of a custom screenboard, and the cog should be used to generate public URL. 

