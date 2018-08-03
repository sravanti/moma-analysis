import json
import codecs
import os
import sys
from collections import Counter

nationality_list = codecs.open("Countries-list.csv", 'r').readlines()
nationalities = {}
for line in nationality_list:
  line = line.split(',')
  nationalities[line[2]] = line[1]

def get_cities():
#Parse file and return dict of the form title : city
  with open("Artworks.json") as jsonfile:
    top_countries = {}
    art_data = json.load(jsonfile)
    for item in art_data:
      artist_bio = item["ArtistBio"]
      nationality = artist_bio.split(',')[0][1:]
      print "nationality: ", nationality
      country = nationalities.get(nationality)
      print "country: ", country
      top_countries[country] = top_countries.get(country, 0) + 1
    return sorted(top_countries, key=top_countries.get, reverse=True)
      
    """
    top_cities = {}
    for item in art_data:
      title = item["Title"]
      art_city = [city for city in cities if city in title]
      print art_city
      #naively adding longest string (i.e. "New York," not "York")
      if art_city:
        top_city = max(art_city, key=len)
        top_cities[top_city] = top_cities.get(top_city, 0) + 1
    return sorted(top_cities, key=top_cities.get, reverse=True)
    """
def get_living_artists():
  with open("Artworks.json") as jsonfile:
      art_data = json.load(jsonfile)
      living_art = {}
      for item in art_data:
        if "born" in item["ArtistBio"]:
          living_art[item["Artist"]] = living_art.get(item["Artist"], 1)
      return living_art

def get_gifts():
   num_gifts = 0
   non_gifts = []
   with open("Artworks.json") as jsonfile:
      art_data = json.load(jsonfile)
      for item in art_data:
        creditline =  item["CreditLine"]
        if creditline:
          if "gift" or "Gift" in creditline:
            num_gifts = num_gifts + 1 
          else:
            non_gifts.append(creditline)
   return non_gifts

def get_date_acq():
  num_acq = 0
  with open("Artworks.json") as jsonfile:
    art_data = json.load(jsonfile)
    for item in art_data:
     if item["DateAcquired"]:
        num_acq = num_acq + 1
  return num_acq 
