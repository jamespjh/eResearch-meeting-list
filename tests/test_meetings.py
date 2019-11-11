#!/usr/bin/env python

# Read in each of the data files and validate the contents
# name: International Symposium on Cluster, Cloud and Internet Computing
# link: http://cloudbus.org/ccgrid2020/
# next:
#  location: Melbourne, Australia
#  date-from: 2020-05-11
#  date-to: 2020-05-14
#  link: http://cloudbus.org/ccgrid2020/

import pytest
import yaml
from datetime import date
from glob import glob
import os

here = os.path.dirname(os.path.abspath(__file__))

def test_meetings(tmp_path):
    """test that meetings data files are valid.
    """
    data_files = os.path.join(os.path.dirname(here), '_data', '*.yml')

    # required fields, and cannot be empty
    requireds = ['name', 'link', 'next']

    for data_file in glob(data_files):

        # Basename for easier reference
        name = os.path.basename(data_file)

        # Navigation and table of contents
        if name in ['navigation.yml', 'toc.yml']:
            print("Skipping non meeting or event file %s" % data_file)
            continue    

        assert os.path.exists(data_file)
        print("Testing loading of %s" % name)

        # Read in the event
        with open(data_file, 'r') as stream:
            event = yaml.safe_load(stream)

        # Ensure required fields present
        for required in requireds:
            print('Looking for %s in %s' % (required, name))
            assert required in event

        for field in event.keys():
            if field not in requireds:
                print('Warning: %s is a custom field in %s, not used.' % (name, field))   

        # Link must be url
        assert event['link'].startswith('http')

        # Next can either be defined, or TBA
        if isinstance(event['next'], dict):

            # next requires date-to, date-from, location, link
            for field in ['date-to', 'date-from', 'link', 'location']:
                print("Checking for next.%s in %s" % (field, name))
                assert field in event['next']

            # must be datetims
            assert isinstance(event['next']['date-to'], date)
            assert isinstance(event['next']['date-from'], date)

        else:
            assert event['next'] == "TBA"
