'''
Stato.py Calculate the average and the variance of all the data collected. Mean to be used with stationary data.
Right now error trapping  is not implemented 
 * Created by J.Larragueta on 03/02/2025
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
import pandas as pd
import sys
inputFile=' '  # Input GPSLogger txt file
#Parse the command line arguments

na=len(sys.argv)
if na != 2:   #Correct number of arguments not provided, display information
    print('Stato.py util, calculate basic statistics of GPSLogger txt files')
    print('Please enter GPS Logger txt file name to process')
    print('Usage: Python <Input file name>')
    sys.exit(-1)
if na == 2:   #One argument has been provided
    argo=sys.argv[1]
    inputFile=argo
    print('Stato.py util, calculate basic statistics of GPSLogger txt files')
    print('Selected file name:', inputFile)

dataset = pd.read_csv(inputFile)
dataset = dataset[['latitude', 'longitude']]
numRows = len(dataset)
print('Number of samples: ', numRows)
print('Mean latitude: ', dataset['latitude'].mean())
print('Latitude variance: ', dataset['latitude'].var())
print('Mean longitude: ', dataset['longitude'].mean())
print('Longitude variance: ', dataset['longitude'].var())