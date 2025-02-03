'''
CTime.py change the time of GPS Logger TXT exported files to that specified into the file name
Right now error trapping  is not implemented 
 * Created by J.Larragueta on 02/02/2025
 * This file is part of BasicAirData GPS Logger Utils
 *
 * Copyright (C) 2011 BasicAirData
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
'''
import csv
import sys
from datetime import datetime, timedelta
labelCol="date time" #Column description for date time 
inputFile=' '  # Input GPSLogger txt file
outputFile=' ' # Output GPSLogger txt file
offsetHours=0  #Desired time offset

#Parse the command line arguments

na=len(sys.argv)
if na != 2:   # Worng number of arguments provided, display information
    print('CTime util, shift times of GPSLogger txt files')
    print('Please enter GPS Logger txt file name to process')
    print('Usage: Python <Input file name>')
    sys.exit(-1)
if na == 2:   #One argument has been provided
    argo=sys.argv[1]
    inputFile=argo
    outputFile='_' + argo
    print('CTime util, shift times of GPSLogger txt files')
    print('Selected file name:', inputFile)
    print('Output file name:', outputFile)
#Open input GPS Logger file, copy file to output GPSLogger txt file and apply time offset of specified offsetHours amount
with open(inputFile, newline='') as f:
    reader = csv.reader(f)
    listOFColumnNames = []  #Columns names
    outdata=[] #Output table
    indexRow=0 #row number
    for row in reader:
        riga=row #Modified row
        if  indexRow < 1:
            listOFColumnNames.append(row)
            puntaData =listOFColumnNames[0].index(labelCol);  # number of column with date time
        if  indexRow == 1:  #Second line of the file
            a=int(row[puntaData][11:13]) #Extract hour value from GPSLogger file and cast to int
            b=int(inputFile[10:11]) #Extract hour value from GPSLogger file name and cast to inn
            offsetHours=b-a
            OldDate = datetime.strptime(row[puntaData],"%Y-%m-%d %H:%M:%S.%f")
            NewDate = OldDate + timedelta(hours = offsetHours)
            riga[puntaData]= NewDate.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            print(riga[puntaData])
        if row[0].find('T') != -1 and indexRow != 1:
            OldDate = datetime.strptime(row[puntaData],"%Y-%m-%d %H:%M:%S")
            NewDate = OldDate + timedelta(hours = offsetHours)
            riga[puntaData]= NewDate.strftime("%Y-%m-%d %H:%M:%S") 
        outdata.append(riga)
        indexRow=indexRow+1
with open(outputFile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(outdata)
