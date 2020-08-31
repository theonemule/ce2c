print(" * * * CODE IN SPACE * * *")
print()
print("A long time ago in a computer far, far away there was a program running that wanted to explorer the universe. It wasn't sure if wanted to go to a star or a planet.")
print()
action = input("Should he go to a (S)tar or a (P)lanet.")

if action == "S":
    print()
    print("The program went to the star and found it was made of bits, but he wanted bytes! The star told the program to go find bytes on Mars or stay for bits.")
    print()
    action = input("She he (S)tay for bits or (L) for bytes?")
    
    if action == "S":
        print()
        print("The program decided to stay. He ate bits and was satisfied. He then went home. THE END!")
        print()
    else:
        print()
        print("The program decided to leave to look for bytes. He came to the planet of bytes and bit into the bytes. He loved them and was happy! THE END!")
        print()
    
else:
    print()
    print("The program went to the planet and found nothing but vanilla. He wanted Chocolate! The planet said chocolate is in the Milky Way.")
    print()
    action = input("She he (S)tay for vanilla or (L) for chocolate?")
    
    if action == "S":
        print()
        print("The program decided to stay for vanilla and got lost in the delicious ice cream and cookies. He was never seen from again. THE END!")
        print()
    else:
        print()
        print("The program went to the chocolate planet in the Milky Way and enjoyed the cookies with milk. Every byte was delicious! THE END!")
        print()    