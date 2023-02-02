from math import ceil as shaik
# calculate cost of wall
# area of wall
# tiles are pack in box per meter ^2

def validate_number(the_number):
    rpt = True


nbox = 0
price = [19.50, 25.95, 35.75, 12.50, 11.00, 52.95, 65.00, 58.98, 85.00, 62.75]
tiles = ["sbg", "sgm", "spb", "msy", "mbr", "mgp", "lowe", "lbg", "lbe", "elwm"]
for i in range(10):
    print(i+1, "--->", tiles[i], " ", price[i])

while rpt or nwalls > 4 or nwalls < 1:
    try:
        nwalls = int(input("Please enter the amount of wall ranging from 1 --> 4 : "))
        rpt = False
    except ValueError:
        print("Please enter a number")

tl = int(input("Please select your choice of tiles : "))
tlarea = 0
for x in range(nwalls):
    print("Dimension of wall ", x+1)
    height = float(input("Please enter the height : "))
    width = float(input("Please enter the width : "))
    area = height*width
    tlarea += area

nbox = shaik(tlarea)

print("Your total area of the wall is : ", tlarea)
print("The number of boxed tiles will be  : ", nbox)
print("The total cost will be : ", price[tl-1]*nbox)


git config --global user.email "joseph.opio@bisp.edu.my"
git config --global user.name "Teacher Joseph"







