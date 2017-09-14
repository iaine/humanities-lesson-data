'''
   Script to find the publication place from the XML
'''

from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
import urllib2
import sys

TCPURL = "https://raw.githubusercontent.com/textcreationpartnership/{0}/master/{0}.xml"

def _fetch_text(tcpid):
    '''
      Fetch the text 
    '''
    xmlstring = urllib2.urlopen(TCPURL.format(tcpid))
    return _find_place(xmlstring)

def _find_place(filestr):
    '''
       Use Xpath to find the pubPlace
    '''
    
    tree = xml.dom.minidom.parseString(filestr.read())
    collection = tree.documentElement
    place = None
    _tmp = collection.getElementsByTagName('pubPlace')

    if _tmp is not None:
        place = _tmp[1].firstChild.data
    if place.endswith(':'):
       place = place[:-1] 
    place = place.encode('utf-8').strip()
    return place

fname = sys.argv[1]

data = pd.read_csv(fname)
#find the free items 
ids = data.loc[data['Status'] == 'Free']
with open('places.csv', 'wb') as f:
    for idx, id in ids.iterrows():
        f.write(id["TCP"] + ',' + _fetch_text(id["TCP"]) + "\n")
        #print(id["TCP"])
        #print(_fetch_text(id["TCP"]))
