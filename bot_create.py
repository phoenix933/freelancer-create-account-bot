import pyautogui as pag
import pyperclip
import time
import json

profile = None
with open("./profile.json", "r+") as file:
    profile = json.load(file)
print(profile["skills"])
pag.FAILSAFE = False
if pag.confirm("Are you ready? Please go to browser.") != "OK":
    exit()
pag.hotkey("ctrl", "t")
pag.typewrite("freelancer.com\n")
time.sleep(3)
pag.click(1348, 107)
pag.hotkey("ctrl", "t")
pag.typewrite("yopmail.com\n")
time.sleep(3)
pag.click(523, 552)
time.sleep(2)

pag.click(831, 572)
time.sleep(1)
pag.click(1289, 710)
time.sleep(1)
pag.click(1073, 570)
time.sleep(0.5)
pag.hotkey("ctrl", "shift", "tab")

time.sleep(0.5)
pag.click(870, 396)
pag.hotkey("ctrl", "v")
pag.click(859, 477)
pag.typewrite("pwd1234!@#$")
time.sleep(0.5)
pag.click(807, 544)
time.sleep(0.5)
pag.click(807, 544)
time.sleep(0.5)
pag.click(959, 611)

# Page 2
time.sleep(1.5)
pag.click(912, 395)
time.sleep(1)
pag.click(939, 484)
time.sleep(1)
pag.click(963, 336)
if pag.confirm("Continue?") != "OK":
    exit()
time.sleep(5)
# pag.click(557, 450)
# time.sleep(4)
# pag.click(557, 450)

# skill input for loop
for skill in profile["skills"]:
    time.sleep(0.5)
    pag.click(472, 295, 3)
    pag.typewrite(skill)
    time.sleep(1)
    pag.click(853, 444)
if pag.confirm("Continue?") != "OK":
    exit()
pag.click(1466, 968)
# Page 3
time.sleep(2)
pag.click(1093, 742)
# Page 4
time.sleep(2)
pag.click(784, 614)
pag.typewrite(profile["firstName"])
# time.sleep(0.5)
pag.click(775, 712)
pag.typewrite(profile["lastName"])
# time.sleep(2)
pag.click(1189, 848)
# Page 5
time.sleep(0.5)
pag.click(1187, 856)
# Page 5-2
time.sleep(0.5)
pag.click(725, 549)
pyperclip.copy(profile["heading"])
pag.hotkey("ctrl", "v")
# time.sleep(2)
pag.click(795, 677)
pyperclip.copy(profile["description"])
pag.hotkey("ctrl", "v")
time.sleep(0.5)
pag.click(1189, 848)
# Page 6
time.sleep(2.5)
pag.click(739, 667)
pag.typewrite(profile["birth"])
time.sleep(0.5)
pag.click(1185, 611)
time.sleep(0.5)
pag.click(1185, 811)
# Page 7
if pag.confirm("Continue?") != "OK":
    exit()
time.sleep(0.8)
pag.click(1189, 924)
# Page 8
time.sleep(0.5)
pag.hotkey("ctrl", "tab")
time.sleep(0.5)
pag.click(525, 211)
time.sleep(3)
pag.click(653, 454)
# Emali Verify
time.sleep(4)
pag.hotkey("ctrl", "w")
time.sleep(0.5)
pag.hotkey("ctrl", "w")
time.sleep(0.5)
pag.click(1185, 666)
# Page 9
time.sleep(1)
pag.click(1432, 894)
# Page 10
time.sleep(1)
pag.click(1452, 1015)
# Page 11
time.sleep(2)
pag.click(816, 544)
time.sleep(5)
pag.click(1480, 358)  # showcase

pag.alert("Done")
# while True:
#     print(pag.position())
