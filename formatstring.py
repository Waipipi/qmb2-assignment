item='laptop'
exchangeRate=1.3238763214
price=1299
#formatting a strong using the % operator
message='The %s costs %5d USD. The exchange rate is %4.2f USD to 1 EUR' % (item,price,exchangeRate)
print(message)

#formatting the stroing using the format method
message='The {0:s} costs {1:5d} USD. The exchange rate is {2:4.2f} USD to 1 EUR'.format(item,price,exchangeRate)
print(message)

message = f"The {item.upper()} costs {price:5d} USD. The exchange rate is {exchangeRate:4.2f} USD to 1 EUR."
print(message)