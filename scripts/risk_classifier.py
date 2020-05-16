import pandas as pd
import numpy as np
from googlegeocoder import GoogleGeocoder
geocoder = GoogleGeocoder("AIzaSyAhhWzdBeS-eG33_mU_S4qjFzIbVW83Mrc")

#Define key variables with their weighted values
fml = 0.2
geo = 0.2
occ = 0.2
tra = 0.2
sym = 0.2

#Geographic Centers
centers = [114.23724199,114.13673885,113.97385556,114.17992336]

print('Welcome to the COVID-19 Epidemiology based risk classifer. \nWe aim to provide an assesment for the risk score based on \n1.geographic location\n2.family ties\n3.occupation\n4.travel history\n')

#Step 1: Calculating the spatial distance from key clusters
add = input('Please enter your Address in Hong Kong\n>')
add =  add + " Hong Kong"
try:
    search = geocoder.get(add)
except ValueError:
    search = 'Hong Kong'
lat = float(search[0].geometry.location.lat)
long = float(search[0].geometry.location.lng)
dist = []
for i in centers:
    dist.append(abs(i-long))

#This score lies between 0 and 0.5
geo_score =(max((dist))/0.4)*100
if (geo_score> 100):
    geo_score = 100
# print(geo_score)
#Step 2: Calculating risk score based on occupation
job = input("\nPlease enter the sector that you work in. If you're studying, please enter Student.\nExamples include but not limited to\nAviation\nFinance\nDomestic Worker\nRestaurant & Entertainment\nCab Driver\nGovernment Employee\n>")
risk_list = ['Student', 'Aviation', 'Cab Driver', 'Education', 'Domestic Worker', 'Finance', 'Restaurant', 'Cleaner', 'Medical Services']
if job in risk_list:
    job_score = 100
else:
    job_score = 10
# print(job_score)

#Step 3: Calculating risk score based on travel history
travel = input("\nPlease indicate Y/N if you have travelled outside HK in the past month.\n>")
epi_travel = input("\nPlease indicate Y/N if you have been in contact with someone who's been outside HK in the past month\n>")

if travel == 'Y':
    tra_score = 100
else:
    tra_score = 0
if epi_travel == 'Y':
    fam_score = 50
else:
    fam_score = 0

#Step 4: Symptotic Score
symp = input('\nAre you feeling symptoms like fever, dry cough, tirednes or shortness of breath. Y/N\n>')
if symp == 'Y':
    symp_score =100
else:
    symp_score = 0

over = fml* fam_score + geo*geo_score + occ*job_score + tra*tra_score + sym*symp_score
print('\nThank you for entering your data. Your risk score is '+str(round(over,2))+ "%")
