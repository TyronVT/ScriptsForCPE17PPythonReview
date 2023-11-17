f = open("devices.txt", "a")
while True:
    newItem = input("Enter a new device: ")
    if newItem == "exit":
        break
    f.write(newItem + "\n")
f.close()
print("All done!")