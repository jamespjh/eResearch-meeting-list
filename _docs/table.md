---
title: Table of Meetings
tags: 
 - research
 - data
description: Master table of all meetings
---

# Table of Meetings

<table class="table table-bordered" id="meeting-table" width="100%" cellspacing="0">
    <thead>
    <tr>
    <th>Name</th>
    <th>Next Location</th>
    <th>Next Date From</th>
    <th>Next Date To</th>
    </tr>
    </thead>
    <tbody>{% for meeting in site.data %}{% if meeting[0] != "toc" and meeting[0] != "navigation" %}<tr>
    <td>{% if meeting[1].link %}<a href="{{ meeting[1].link }}" target="_blank">{{ meeting[1].name }}</a>{% else %}{{ meeting[1].name }}{% endif %}</td>
    <td>{{ meeting[1].next.location }}</td>
    <td>{{ meeting[1].next.date-from }}</td>
    <td>{{ meeting[1].next.date-to }}</td>
    </tr>{% endif %}{% endfor %}
</tbody>
</table>

<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<link href="https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css" rel="stylesheet" type="text/css" />
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js"></script>
<script>
$('#meeting-table').DataTable({
  "pageLength": 50
});
</script>
