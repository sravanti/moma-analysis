from __future__ import division
import sqlite3
import json
from collections import Counter, defaultdict

MOMA_OPENED = 1929
CURRENT_YEAR = 2016

conn = sqlite3.connect('momadata.sqlite')
c = conn.cursor()

def getQuery(command):
  """ Returns result of querying database with given command  """
  c.execute(command)
  return c.fetchall()

def getYear(year):
  """ Returns year given format "YYYY-MM-DD" as a string """
  return str(year.split('-')[0])

def getGenders(genderString):
  """ Returns tally of (female, male) artists in tuple form """
  if genderString is "Female": 
    return (1, 0)
  elif genderString is "Male": 
    return (0, 1)
  else:
    genders = genderString.split()
    return (genders.count("Female"), genders.count("Male"))

def getYearDict(value):
  """ Returns a dictionary of year / value pairs from MOMA's opening to today """
  return {str(year): value for year in range(MOMA_OPENED, CURRENT_YEAR + 1)}    

def artByYear():
  """ Returns a dictionary of year, num artworks acquired """
  years = getQuery('SELECT DateAcquired FROM Artworks')
  years = [getYear(year[0]) for year in years]
  return Counter(years)

def nationalitiesByYear():
  """ Returns a nested dictionary of {nationality: {year: number of pieces acquired
  that year} """
  nationalities = {}
  nationalitiesAndYears = getQuery('SELECT Nationality, DateAcquired'
                                   ' FROM Artworks')
  for (nationality, year) in nationalitiesAndYears:
    year = str(getYear(year))
    if year and nationality:
      if nationality not in nationalities:
        nationalities[nationality] = getYearDict(0)
      nationalities[nationality][year] = nationalities[nationality][year] + 1
  return nationalities

def genderByYear():
  """ Returns a dictionary of year, % women artists acquired that year """
  #(F, M) tuple initally to tally male + female artists
  yearDict = getYearDict((0,0))
  genderAndYears = getQuery('SELECT DateAcquired, Gender'
                            ' FROM Artworks')
  for (year, genders) in genderAndYears:
    if year:
      yearDict[getYear(year)] = map(sum, zip(getGenders(genders), 
                                             yearDict[getYear(year)]))

  yearDict = {year: f / (f + m) for year, [f, m] in yearDict.iteritems()}
  return yearDict

if __name__ == "__main__":
  with open('genderbyyear.csv', 'w') as f:
    years = genderByYear()
    for year in years.items():
      f.write(year[0] + ',' + str(year[1]) + '\n')
      
    f.close()
