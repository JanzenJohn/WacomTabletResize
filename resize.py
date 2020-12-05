import os

factor = 10

def m(x):
    return (x/factor)/2

borders = {"x":{"starting":0, "ending":0, "total":15200}, "y":{"starting":0, "ending":0, "total":9500}}

print(os.popen("xsetwacom --list devices").read())
device_id = input("enter id of pencil : ")
os.system(f"xsetwacom --set {device_id} resetarea")
output = os.popen(f"xsetwacom --get {device_id} area").read()
output = output.split()
borders["x"]["total"] = int(output[2])
borders["y"]["total"] = int(output[3])
factor = int(input("The 1/n area you want to use : "))

for i in borders:
    length = borders[i]["total"]
    borders[i]["starting"] = int(length/2 - m(length))
    borders[i]["ending"] = int(length/2 + m(length))



command = f'xsetwacom --set {device_id} area {borders["x"]["starting"]} {borders["y"]["starting"]} {borders["x"]["ending"]} {borders["y"]["ending"]}'

os.system(command)
