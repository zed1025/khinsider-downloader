from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

BASE = 'https://downloads.khinsider.com'

link = str(input('Enter link: '))
# print('- Press 1 if mp3 only\n- Press 2 if site has both mp3 and flac')
# num = int(input())
num_files = int(input('Enter number of tracks for this album: '))
file_name = str(input('Enter file name: '))

page = requests.get(link)
# print(page.status_code)
# print(page.headers['content-type'])

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

link_list = []
link_list_final = []

counter = 0

for a in soup.select('table[id=songlist] td[class=clickable-row] > a'): 
	link_list.append(a.get('href'))	

t = len(link_list)/num_files
for i in range(len(link_list)):
	if i%t == 0:
		link_list_final.append(BASE + link_list[i])

# for i in link_list_final:
# 	print(i)
# print(len(link_list_final))

####################### Getting Audio Links from each song page ############################
song_links = []
# for i in link_list_final:
# 	page = requests.get(i)
# 	soup = BeautifulSoup(page.text, 'html.parser')
# 	links = soup.findAll('audio')
# 	song_links.append(links[0].get('src'))
	
for i in tqdm(range(len(link_list_final))):
	page = requests.get(link_list_final[i])
	soup = BeautifulSoup(page.text, 'html.parser')
	links = soup.findAll('audio')
	song_links.append(links[0].get('src'))

# for i in song_links:
# 	print(i)

print('Total links: ', len(song_links))


###################### Printing links to file ######################################
# file_name = str(input('Enter file name: '))
file_name = file_name+'.txt'
with open(file_name, "w") as outfile:
    outfile.write("\n".join(song_links))

print('Done...')