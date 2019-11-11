# eResearch-meeting-list

This is a list of all the meeting series we know about in:

* eInfrastructure
* Research Data
* HPC
* Data Science for Science and Digital Humanities
* HTC and Research Clouds
* Research Networks
* Open Science and Open Data for Research
* Scientific Software Development
* Tech skills for research, RSE, ResOps, Research Infrastructure Engineering
* Research publishing beyond the PDF, software citation and preservation etc

## Data Files

Each meeting series is represented in a data file under [_data](_data). To
add another file, simply add it to this folder in the same format, and it
will render on the site. 

### Required Fields

Specifically, the following fields are required:

 - **name**: the name of the meeting
 - **link** a url to learn about it, must begin with http*
 - **next**: should be EITHER a string "TBA" or a single entry with:
    - date-from: the starting date in the format YYYY-MM-DD
    - date-to: the ending date, in the format YYYY-MM-DD
    - link: a link to the site for the specific event, or the same link for the global event
    - location: the location the event will take place

A minimum example might look like this:

```yaml
name: FORCE11
link: https://www.force11.org
next:
  date-from: 2019-10-16
  date-to: 2019-10-17
  link: https://www.force11.org/meetings/force2019
  location: Edinburgh, Scotland
```

An example with an event not yet scheduled might look like this:

```yaml
name: FORCE11
link: https://www.force11.org
next: TBA
```

### Optional Fields

If the event has had previous occurences, you should define these with a list
of `previous`. Note the extra dash to indicate that we have a list and not a single
entry:

```
name: FORCE11
link: https://www.force11.org
previous:
  - date-from: 2019-10-16
    date-to: 2019-10-17
    link: https://www.force11.org/meetings/force2019
    location: Edinburgh, Scotland
  - date-from: 2018-10-16
    date-to: 2018-10-17
    link: https://www.force11.org/meetings/force2018
    location: Edinburgh, Scotland
```

You should generally use 2 spaces as a convention for files.

## Contributing

We welcome contributions and support from the community.
For more information on ways to contribute, and ways to how we prefer contributions
to be made, please see [`CONTRIBUTING.md`](CONTRIBUTING.md).

