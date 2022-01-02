# UK Lateral Flow Test Checker
A simple CLI app written in Python that checks [gov.uk](https://www.gov.uk/) for availability of lateral flow tests for COVID-19. It does this by visiting [The LFT order page](https://test-for-coronavirus.service.gov.uk/order-lateral-flow-kits) and searching for text that indicates unavailability. This may stop working if the unavailability page is updated or changed.

Why? During December 2021 in the UK there were major shortages in lateral flow test kits. At some point the government advice was to keep trying, and refresh the page every hour or so. That seemed like a bit of a pain to do manually, so I took this as an opportunity to learn how to make a basic web bot in Python. It's nothing fancy, but it was a fun little project.

## Install
You will need the dependencies `selenium` and `plyer`. Install these as follows:
```bash
pip install selenium
pip install plyer
```

Clone the repository and then you can run the script with `./lateral-flow.py`. You may have to set the executable bit if you get a permission error:
```bash
chmod +x lateral-flow.py
```

Alternatively just run the following:
```bash
python3 lateral-flow.py
```

## Usage
Run as follows:
```bash
./lateral-flow.py
```

This will print lateral flow availability into the console every 30 minutes. For extra functionality, such as desktop notifications, see the help text:
```bash
./lateral-flow.py --help
```

A useful argument pushes a desktop notification once lateral flow tests are available:
```bash
./lateral-flow.py -n
```

Please be reasonable when using the `-t` setting, and respect [robots.txt](https://www.gov.uk/robots.txt). You're trying to check for LFT availability, not perform a Denial of Service attack.
