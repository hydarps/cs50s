filetype = input("Enter filetype: ").lower().strip()

if "." in filetype:
    name, ext = filetype.split(".")

if ext == "jpg":
    ext = "jpeg"

else:
    name = filetype
    ext = "octet-stream"



print(f"{name}/{ext}")
