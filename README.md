
# COST
CheapOpenSatTracker
Satellite Tracker based on a camera PTZ
Get information from Orbitron(http://www.stoff.pl/) or SDRConsole(https://www.sdr-radio.com/console) or other tools, 
then translate the AZ/EL to PELCO-D and put them to the PTZ via RS-485.
Note some PTZ is not precise， so I use a linear transfer to correct it.
The PTZ must support direct position command(0x4b, 0x4d).
DDE based on https://code.activestate.com/recipes/577654-dde-client/ and noisywiz's DDE client (https://gist.github.com/noisywiz/2661065) (it seems these are same one)
