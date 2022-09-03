print("hello! this is a celcius to fahrenheit converter.")
celc = float(input("please enter the celcius amount : "))
fh = (celc * 1.8) + 32

print(" %0.1f celcius is equal to %0.1f fahrenheit" %(celc,fh))

if fh >= 104 :
    print("its so hot!")

elif fh < 50 :
    print("its so cold!")

else :
    print("its pleasant!!")