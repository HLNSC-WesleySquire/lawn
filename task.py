name = ""
address = ""
phone = ""
width = ""
length = ""

while True:
    name = input("Customer name: ")
    address = input("Customer Address: ")
    try:
        phone = int(input("Customer Phone Number: "))
        width = float(input("Width of the lawn: "))
        length = float(input("Length of the lawn: "))
        if  width > 2 and width < 30:
            if length > 2 and length < 50:
                break
            else:
                print("Length is too small or too large.")
        else:
            print("Width is too small or too large.")
    except:
        print("Invalid input. Please recheck your values.")
    
area = width*length
qualityPrice = 0.00
print("Please enter lawn care product:\n1) Luxury\n2) Standard\n3) Economy\n4) None")
quality = input("Choice: ")
if quality == 1:
    qualityPrice = 1.15
elif quality == 2:
    qualityPrice = 0.80
elif quality == 3:
    qualityPrice = 0.45
else:
    qualityPrice = 0.00
labourCost = 0.50 * area
qualityPrice *= area
totalNoVAT = qualityPrice + labourCost
totalWithVAT = totalNoVAT + (totalNoVAT * 0.20)
print("Customer details:\n    Name: " + name + "\n    Address: " + address + "\n    Number: " + str(phone) + "\nTotal area: " + str(area) + "\nLabour cost: " + str(labourCost) + "\nTotal (excluding VAT): " + str(totalNoVAT) +"\nTotal: " + str(totalWithVAT))
