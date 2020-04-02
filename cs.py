#!/usr/bin/python3
import time
import sys
import requests as r
from bs4 import BeautifulSoup as bs
import html5lib
import re
import subprocess as s


class Curr:

	def multiple_replacer(*key_values):
	    replace_dict = dict(key_values)
	    replacement_function = lambda match: replace_dict[match.group(0)]
	    pattern = re.compile("|".join([re.escape(k) for k, v in key_values]), re.M)
	    return lambda string: pattern.sub(replacement_function, string)

	def multiple_replace(string, *key_values):
	    return Curr.multiple_replacer(*key_values)(string)

	def strength():

		#get the site and parse the html
		x = r.get("http://www.livecharts.co.uk/currency-strength.php").text

		cur = bs(x, "html5lib")

		#Find all Currency by id
		pairs = [c for c in cur.find_all(id="map-innercontainer-symbol")]

		#To be excluded
		y = str('style="background-image:none"')

		#EURO CURRENCY index=0 or pair[0]
		#Finding the current level we need to loop through all levels

		levels = [
			'map-innercontainer-strong3',
			'map-innercontainer-strong2',
			'map-innercontainer-strong1',
			'map-innercontainer-weak1',
			'map-innercontainer-weak2',
			'map-innercontainer-weak3',
		]


		lv = [l for l in cur.find_all(id=levels)]

		mine = lv

		# #Show out the results to the user
		replacements = (u"div", u""),(u'id="map-innercontainer-',u""),(u"<",""),(u'style="background-image:none"',u""),(u'">',""),(u"/",u""),(u"",u""),(u">",u""),(u'"',u"")
		
		print(f'Currency\t\tStrength\n')
		print(f'{pairs[0].text}\t\t\t{Curr.multiple_replace(str(mine[0:6]), *replacements)}\n')
		print(f'{pairs[1].text}\t\t\t\t{Curr.multiple_replace(str(mine[6:12]), *replacements)}\n')
		print(f'{pairs[2].text}\t\t\t\t{Curr.multiple_replace(str(mine[12:18]), *replacements)}\n')
		print(f'{pairs[3].text}\t\t\t\t{Curr.multiple_replace(str(mine[18:24]), *replacements)}\n')
		print(f'{pairs[4].text}\t\t\t\t{Curr.multiple_replace(str(mine[24:30]), *replacements)}\n')
		print(f'{pairs[5].text}\t\t\t\t{Curr.multiple_replace(str(mine[30:36]), *replacements)}\n')
		
# 		#EURO
# 		s.call(['notify-send','Currency\t\tStrength',f'{pairs[0].text}\t\t{Curr.multiple_replace(str(mine[0:6]), *replacements)}'])
# 		# GBP
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[1].text}\t\t{Curr.multiple_replace(str(mine[6:12]), *replacements)}'])
# 		#USD
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[2].text}\t\t{Curr.multiple_replace(str(mine[12:18]), *replacements)}'])
# 		#AUD
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[3].text}\t\t{Curr.multiple_replace(str(mine[18:24]), *replacements)}'])
# 		#JPY
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[4].text}\t\t{Curr.multiple_replace(str(mine[24:30]), *replacements)}'])
# 		#CHF
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[5].text}\t\t{Curr.multiple_replace(str(mine[30:36]), *replacements)}'])
# 		#NZD
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[6].text}\t\t{Curr.multiple_replace(str(mine[36:42]), *replacements)}'])
# 		#CAD
# 		s.call(['notify-send','Currency\t\t\tStrength',f'{pairs[7].text}\t\t{Curr.multiple_replace(str(mine[42:48]), *replacements)}'])


if __name__ == '__main__':
	Curr.strength()


