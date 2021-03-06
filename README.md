# DynDNS OVH

This project was born of the boredom of all the limited dyndns services.

# Setup

Install dependencies :

    pip3 install ovh netifaces

Note that you may need the development package for python 3.

Setup your OVH application keys in `.env` based on the contents of `sample.env`,
then load it with `source .env`.

# Run

    . sample.env ./update.py <options>

# Options

 - `-i` : sets the interface to take the IPs from. Ex : `eth0`
 - `-d` : main domain to update. Ex : `example.com`
 - `-s` : subdomain to update. Ex : `server`. Leave blank to update the root domain.

# Cron

Let's face it, you ideally want to set this up in a crontab. Here is an
example to do nightly updates :

    0 0 * * * . path/to/repo/.env path/to/repo/update.py <options>

# License

Copyright (c) 2017-present Tuetuopay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

