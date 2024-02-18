file = input("File name: ").strip().lower()

if file.endswith(".jpg") or file.endswith(".jpeg") == True:
    print("image/jpeg")

elif file.endswith(".gif") == True:
    print("image/gif")

elif file.endswith(".png") == True:
    print("image/png")

elif file.endswith(".pdf") == True:
    print("application/pdf")

elif file.endswith(".zip") == True:
    print("application/zip")

elif file.endswith(".txt") == True:
    print("text/plain")

else:
    print("application/octet-stream")

#file = input("File name: ").strip().lower()

#mime_types = {
    #".jpg": "image/jpeg",
    #".jpeg": "image/jpeg",
    #".gif": "image/gif",
    #".png": "image/png",
    #".pdf": "application/pdf",
    #".zip": "application/zip",
    #".txt": "text/plain",
#}

#file_extension = file[file.rfind("."):]

#if file_extension in mime_types:
    #print(mime_types[file_extension])
#else:
    #print("application/octet-stream")
