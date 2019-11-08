---
title: Meetings
tags: 
 - research
 - data
description: Master list of all meetings
---

# Meetings


{% for meeting in site.data %}{% if meeting[0] != "toc" and meeting[0] != "navigation" %}

<h3>{{ meeting[1].name }}</h3>

{% if meeting[1].link %}<a href="{{ meeting[1].link }}" target="_blank"><button style="float:right" class="btn btn-sm btn-primary">Website</button></a>{% endif %}

{% if meeting[1].next %}<h4>Next</h4>
 - **Location**: {{ meeting[1].next.location }}
 - **Data From**: {{ meeting[1].next.date-from }}
 - **Data To**: {{ meeting[1].next.date-to }}
{% endif %}
{% endif %}
<br>
<hr>
<br>{% endfor %}
