# ZCounting

This code is to run over Z Counting histograms produced in DQM and produce a CSV file with Z rates. The output file format has been agreed upon with ATLAS in 2016.

A CMSSW environment needs to be set up to have the pandas library available.

The python file "testZCounting2.py" is the file to be executed. Parameters such as the time granularity, DQM file location and the brilcalc CSV input file can be changed.

Many aspects in the code can be improved.