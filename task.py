name = input("Customer name: ")
address = input("Customer Address: ")
phone = int(input("Customer Phone Number: "))
width = float(input("Width of the lawn: "))
length = float(input("Length of the lawn: "))

if  width > 2 and width < 30:
    if length > 2 and length < 50:
        area = width*length
        qualityPrice = 0.00
        print("Please enter lawn care product:\n1) Luxury\n2) Standard\n3) Economy")
        quality = input("Choice: ")
        if quality == 1:
            qualityPrice = 1.15
        elif quality == 2:
            qualityPrice = 0.80
        else:
            qualityPrice = 0.45
        labourCost = 0.50 * area
        totalNoVAT = qualityPrice + labourCost
        totalWithVAT = totalNoVAT + (totalNoVAT * 0.20)
        print("Customer details:\n    Name: " + name + "\n    Address: " + address + "\n    Number: " + str(phone) + "\nTotal area: " + str(area) + "\nLabour cost: " + str(labourCost) + "\nTotal (excluding VAT): " + str(totalNoVAT) +"\nTotal: " + str(totalWithVAT))
    else:
        print("Length is too small or too large.")
else:
    print("Width is too small or too large.")
