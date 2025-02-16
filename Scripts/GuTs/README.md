# BasicAirData GPS Logger CTime Python script
 
This script can align the timestamp of GPS Logger generated TXT files to match your timezone .<br>
Offered by [BasicAirData](https://www.basicairdata.eu) - Open and free DIY air data instrumentation and telemetry 


## Description

Example file. The python script should be launched at the command line >>python CTime.py "20240825-095302 - Lago nero e rifugio segantini.txt"
Once launched the script will create a file called _20240825-095302 - Lago nero e rifugio segantini.txt
The first timestamp in the original file "20240825-095302 - Lago nero e rifugio segantini.txt" is at 07:53:02.048. The namefiles contains "20240825-095302" string, that was saved with the local timezone of the recording device.
To align all the time an offset of (9 - 7)=2 hours should be added to all the timestamps within the file.

