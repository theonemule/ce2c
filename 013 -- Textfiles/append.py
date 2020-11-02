try:
    x = input("Enter in some text: ")
    f = open("myfile.txt","a")
    f.write(x + "\n")
    f.close()
except:
    print("Something bad happened.")