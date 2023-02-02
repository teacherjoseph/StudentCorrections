from math import ceil as shaik
# calculate cost of wall
# area of wall
# tiles are pack in box per meter ^2
nbox = 0
price = [19.50, 25.95, 35.75, 12.50, 11.00, 52.95, 65.00, 58.98, 85.00, 62.75]
tiles = ["sbg", "sgm", "spb", "msy", "mbr", "mgp", "lowe", "lbg", "lbe", "elwm"]
for i in range(10):
    print(i+1, "--->", tiles[i], " ", price[i])
height = float(input("Please enter the height : "))
width = float(input("Please enter the width : "))
tl = int(input("Please select your choice of tiles : "))
nbox = shaik(height * width)
print("Your total area of the wall is : ", height * width)
print("The number of boxed tiles will be  : ", nbox)
print("The total cost will be : ", price[tl-1]*nbox)
