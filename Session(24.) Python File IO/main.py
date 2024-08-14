# # Python File IO
#
# # ___"r" read Primary___
# # yeh just data ko read krne k liay use hota hai, as a read-only file open hoghi
#
# f = open("my_read.txt", "r")  # yeh step just read only file bana raha hai
# print(f.read())  # yeh file ko read kr k as a string return karegha using "read()" function
# f.close()  # file ko close krna zahroori hai wrna yeh temp pr khuli reh jaeyghi
# # jss say hamara system slow ho sakhta hai
#
#
# # f.close() use kiay bagayr bhi hum file ko close kr sakhte hai using "with open() as def_name"
# with open("my_read.txt") as f:
#     print(f.read())
#
# print("-----")
#
# # ___"w" (Write) Primary___
# # yeh just data ko write krne k liay use hota hai, as a write-only file open hoghi
# # but yeh old data ko delete krdegha
# with open("my_write.txt", "w") as f:
#     print(f.write("Maynay purana data delete kr k, Hello world data bhej diya txt file may"))
#
# print("-----")
#
# # ___"a" (Append) Primary___
# # yeh file may new contents append kr deta hai file k data k end may
# with open("my_append.txt", "a") as f:
#     print(f.write(" May ek appended data ho"))
#
# print("-----")
#
# # ___"x" (Create) Primary___
# # yeh file create krne k liay use hota hai
# # yeh bar bar ek name ki file nahi create kr sakhta
# # make sure kare k file create krte waqt file exist nahi krti ho
# with open("my_create.txt", "x") as f:
#     print(f.write("May ek new file ho"))
#
#
# print("-----")
#
# # ___"t" Text Mode___
# # yeh "text mode" file ko as string return krta hai
#
# # yaha hum write kr rahe hai
# with open("my_text_mode.txt", "wt") as f:
#     f.write("hello may name is noman \n and learning course python")
#
# # # yaha hum read kr rahe hai
# with open("my_text_mode.txt", "rt", encoding="utf-8") as f:
#     print(f.read())
#
#
# print("-----")
#
# # # ___"t" Binary Mode___
# with open("my_binary_bin.bin", "wb") as f:
#     f.write(b"Hello i am written\nas bytes mode")
#
# with open("my_binary_bin.bin", "rb") as f:
#     print(f.read())
#
# print("-----")
#
# # ___readline()___
# f = open("my_readline.txt", "r")
# # f.readline()  # aghr yaha hum phele say 'readline()' likhe ghay to yeh first line skip krdegha
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} is in maths is {m1}")
#     print(f"Marks of student {i} is in english is {m2}")
#     print(f"Marks of student {i} is in chemistry is {m3}")
#
# print("___or___")
#
# # yaha phir simple line by line data kuch asya bhi kr sakhte hai
# f = open("my_readline.txt", "r")
# for i in f:
#     print(i)
# print("___or___")
#
# # or this way (best way)
# f = open("my_readline.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
#
# print("-----")
#
# # ___writelines()___
# # yaha hum nay "w" kiya hai hai jss say old content delete ho kr naya content aa gaya
# with open("my_writelines.txt", "w") as f:
#     # yeh hamay manually newline deni paray ghi :)
#     lines = ["ahsan is learning\n", "noman is writing\n", "asad is looting crate"]
#     f.writelines(lines)
#
# # yaha hum nay "a" use kiya hai iss say new content append ho gaya ek old data may
# with open("my_writelines.txt", "a") as f:
#     # yeh hamay manually newline deni paray ghi :)
#     lines = ["\nPython is greatest", "\nPython is love\n", "Python is world"]
#     f.writelines(lines)
#
# with open("my_writelines.txt", "r") as f:
#     # print(f.read())  # best way
#     # or
#     print(f.readline().strip())  # strip() ka use kr k spacing remove krdi ta k content clear dikhe
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline())
#
# print("-----")
#
# # ___readlines()___
# # readlines say hum saari lines ko ek list may hi print kr sakhte hai
# # yeh bata bhi deta hai "\n" k zariay k ktini lines maujood thi
# with open("my_readline.txt", "r") as f:
#     print(f.readlines())
#
# print("-----")
#
# # ___seek()___
# # offset: Jitne bytes move karne hain
# # whence: Starting point specify karta hai (default is 0)
# with open("my_seek.txt", "r") as f:
#     print(f.seek(9,0))  # 0 default hota hai
#     print(f.read(4))  # 4 characters read kiye hai
#
# with open("my_seek.txt", "rb") as f1:  # yaha pr binary format ki support kareghi
#     print(f1.seek(9,1))  # current position say start krta hai
#     print(f1.read(4))  # 4 characters read kiye hai
#
# with open("my_seek.txt", "rb") as f1:  # yaha pr binary format ki support kareghi
#     print(f1.seek(-15,2))  # file k end say start krta hai
#     print(f1.read(5))  # 5 characters read kiye hai
#
# # iss tareeqay say hamara content delete hone say bach jata hai
# with open("my_seek.txt", "r+") as f:
#     f.seek(5)  # yeh 5 characters takh move kr gaya hai
#     f.write(" myself is punjabi")  # yeh 5 position say write krta hai
#     f.seek(0)  # Wapas start par le jata hai
#     # aghr hum "f.seek(0)" use nahi krte to yeh current position say shuru karegha not starting
#     print(f.readline())  # Read krta hai file ko starting say
#
# print("-----")
#
# # ___tell()___
# with open("my_tell.txt", "r+") as f:
#     # aghr hum read nahi krwate to yeh isski current position 0 hoti q k iss nay koi data read hi nahi kara
#     f.read()  # File ke start se likhna
#     position = f.tell()  # Current position return karega
#     print(position)  # Output: 5 (Hello likhne ke baad position 5 par hai)
#     f.seek(0)  # File pointer ko wapas start par le jaana
#     print(f.tell())  # Output: 0 <--"current position" (q k ab hum starting may aa chuke hai)
#     print(f.read(2))  # Do characters read karna
#     position = f.tell()  # Current position return karega
#     print(position)  # Output: 2 (Do characters read karne ke baad position 2 par hai)
#
# print("-----")
#
# with open("my_truncate.txt", "w+") as f:
#     f.write("I love Python and remove me using truncate")
#     print(f.tell())  # yeh abhi 42 position pr hai
#     f.seek(0)  # yeh ab wapis start pr aa gaya
#     print(f.tell())  # starting position ab 0 ho agey "ab hum truncate kr sakhte hai"
#     f.truncate(13)  # yeh iss nay 13 characters "I love Python" leliye
#     print(f.read())  # ab baaki k characters print nahi ho sakhte
