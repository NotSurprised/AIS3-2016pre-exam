from hashpumpy import hashpump
import requests
import urlparse
import re

for i in xrange(61)
	mac, ext = hashpump('41fe78ff2c2c51e758bf4501fd8e6a9b8d478f4e', 'expire=1467391984', '&expire=2577390020', i)

	ext = urlparse.parse_qs(ext)

	r = requests.get('https://quiz.ais3.org:8014/', params=[('expire', ext["expire"][0]), ('expire', ext["expire"][1]), ('auth', mac)])

	failed = re.search('<div id="flag">.*ais3{.*', r.content)
	if failed:
		print "{}: {}".format(i, failed.group())
		break