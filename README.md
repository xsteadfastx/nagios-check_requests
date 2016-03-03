# check_requests

Nagios / Icinga check using [requests](http://docs.python-requests.org/en/master/).

```
Usage: check_requests [OPTIONS] URL

Options:
  --text TEXT             Looking for text in response body.
  --verify / --no-verify  Verify SSL certificate.
  --help                  Show this message and exit.

```

## Installation

1. Install the dependencies with `apt-get install build-essential python-dev libffi-dev libssl-dev`.
2. Install the package with `pip install -e git+https://github.com/xsteadfastx/nagios-check_requests.git#egg=check_requests`.
