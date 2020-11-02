try:
    f = open("myfile.txt","r")
    x = f.read()
    f.close()
    print(x)
except:
    print("Something bad happened.")