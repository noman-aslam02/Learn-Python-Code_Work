with open("my_truncate.txt", "w+") as f:
    f.write("I love Python and remove me using truncate")
    print(f.tell())  # yeh abhi 42 position pr hai
    f.seek(0)  # yeh ab wapis start pr aa gaya
    print(f.tell())  # starting position ab 0 ho agey "ab hum truncate kr sakhte hai"
    f.truncate(13)  # yeh iss nay 13 characters "I love Python" leliye
    print(f.read())  # ab baaki k characters print nahi ho sakhte