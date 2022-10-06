#!/Users/jb3mbp/Desktop/nLeaf/leafEnv/bin/python3

from nanoleafapi import Nanoleaf
from time import sleep

nl = Nanoleaf("192.168.1.165")


powerResp = nl.power_on()

sleep(2)

check = nl.check_connection()

brightness = nl.get_brightness()

cFx = nl.get_current_effect()

cHue = nl.get_hue()

cIds = nl.get_ids()

#cInfo = nl.get_info()

#cLayout = nl.get_layout()

cName = nl.get_name()

#cSatu = nl.get_saturation()

#cId = nl.identify()

currentInfo = [powerResp, check, cFx, cHue, cIds, cName]

for theInfo in currentInfo:
	print(theInfo)
