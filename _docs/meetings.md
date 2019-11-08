---
title: Meetings
tags: 
 - research
 - data
description: Master list of all meetings
---

# Meetings


{% for meeting in site.data %}{% if meeting[0] != "toc" and meeting[0] != "navigation" %}

{% if meeting[1].link %}<a href="{{ meeting[1].link }}" target="_blank"><button style="float:right" class="btn btn-sm btn-primary">Website</button></a>{% endif %}<a target="_blank" href="{{ site.tag_search_endpoint }}{{ meeting[1].name }}"><button style="float:right; margin-right:10px; margin-bottom:20px" class="btn btn-sm btn-primary">Search</button></a>

<h3>{{ meeting[1].name }}</h3>

{% if meeting[1].next %}<p style="font-style:italic">When is the next meeting?</p>
 - **Location**: {{ meeting[1].next.location }}
 - **Data From**: {{ meeting[1].next.date-from }}
 - **Data To**: {{ meeting[1].next.date-to }}
{% endif %}
{% endif %}

<br>
<hr>
<br>{% endfor %}
