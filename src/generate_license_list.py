# Given a list of audio files and sound ids from Jamendo, generate a file
# containing the licenses of each of these files.

# The recordings file should be a csv with 2 columns, the first being the
# recording id from jamendo, and the second being the filename that the
# recording is named in the final archive

# The data file should be a json file with the output of the Jamendo API
# This file can be generated using `getplaylist.py` from
# https://github.com/AudioCommons/jamendo-downloader

import argparse
import csv
import json
from typing import List
import urllib.parse

ATTRIBUTES = dict(
    by = 'Attribution',
    nc = 'Non-Commercial',
    nd = 'No Derivatives',
    sa = 'Share-Alike',
    )

def parse_cc_license_url(url: str) -> List[str]:
    """Return a sequence of attributes for the given license URL.
    From https://wiki.creativecommons.org/wiki/License_Properties"""

    # get the path portion of the URL
    path = urllib.parse.urlparse(url)[2]

    # extract the license code portion
    pieces = path.split('/')
    assert(pieces[1] == 'licenses')

    # split the individual codes
    attribute_codes = pieces[2].split('-')

    return [ATTRIBUTES[n] for n in attribute_codes]

def get_license(license_url):
    if "creativecommons.org" in license_url:
        return parse_license_cc(license_url)
    elif "artlibre.org" in license_url:
        return parse_license_lal(license_url)
    elif license_url == "":
        # empty license seems to be by-nc
        return parse_license_cc("http://creativecommons.org/licenses/by-nc/3.0/")
    else:
        assert False, "unknown license url: %s" % license_url


def parse_license_cc(license_url):
    license_parts = parse_cc_license_url(license_url)
    return 'Available under a Creative Commons {} license: {}'.format('-'.join(license_parts), license_url)


def parse_license_lal(license_url):
    return 'Available under License Art Libre: http://artlibre.org/licence/lal/'


def cc_attribution(recording_metadata):
    print('{} by {} from Jamendo: {}'.format(recording_metadata['name'], recording_metadata['artist_name'], recording_metadata['shareurl']))
    license_url = recording_metadata['license_ccurl']
    license_string = get_license(license_url)

def generate_attribution(archive_recordings, jamendo_metadata):
    for rid, filename in archive_recordings:
        print(filename)
        cc_attribution(jamendo_metadata[rid])
        print()

def main(recordingsfile: str, datafile: str):
    archive_recordings = []
    with open(recordingsfile) as fp:
        cr = csv.reader(fp)
        for l in cr:
            archive_recordings.append(l)

    jamendo_recordings = {}
    with open(datafile) as fp:
        j = json.load(fp)
        for recording in j:
            rid = recording['id']
            jamendo_recordings[rid] = recording

    generate_attribution(archive_recordings, jamendo_recordings)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('recordingsfile')
    parser.add_argument('datafile')

    args = parser.parse_args()
    main(args.recordingsfile, args.datafile)
