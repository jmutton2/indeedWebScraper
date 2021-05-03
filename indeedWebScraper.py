import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

#import fire

counts = {}
keywords = ['angular','angularjs','jquery','bigdata','googlecloud','ruby','agile','typescript','html','css','mongodb','database','nosql','express.js','node.js','node','javascript','meteor.js','flutter','react','flask','django','bootstrap','redux','react','docker','node','rest','graphql','mysql','sql','python','c#','c','c++','java','kotlin','reactJS','springBoot','ruby','rails','next.js','nuxt.js','semantic']

def scrub(job="full+stack+intern", loc="Toronto", max_pages=2):
#       job = job.strip().replace(" ", "+") <<Need to be able to register spaces in input.
#       loc = loc.strip().replace(" ", "+") <<Just write inputs with + for now

	for page in range(0,max_pages):
		search="https://ca.indeed.com/jobs?q=" + job + "&l=" + loc
		# + "&start=" + str(page)
		#search="https://www.google.com"
		lookup=requests.get(search)
		soup=BeautifulSoup(lookup.text, "html.parser")

		for link in soup.select('a[onmousedown*="rclk(this,jobmap"]'):
			subURL = "https://ca.indeed.com" + link['href']
			subPage=requests.get(subURL)
			subSOUP=BeautifulSoup(subPage.text, "html.parser")
			print("Parsing: " + subURL)

			for desc in subSOUP.find_all("ul"):
				print(desc)

				words = desc.get_text().lower().split()
				for word in words:
					word=word.strip().replace['.js', ' ']
					if word.endswith("'s"):
						word=word[:-2]
					if len(word) < 2:
						continue
					if word not in keywords:
						continue
					if word in counts:
						counts[word] += 1
					else:
						counts[word] = 1
	wordFreq = []
	for key, value, in counts.items():
		wordFreq.append((value,key))

	wordFreq.sort(reverse=True)
	print(wordFreq)

#if __name__ == '__main__':
	#fire.Fire()
scrub()


