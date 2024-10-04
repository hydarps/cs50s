filetype = input("Enter filetype: ").lower().strip()

if "." not in filetype:
    print("octet-stream")
    name = filetype
    ext = "octet-stream"  # Define ext here, since it doesn't have one
else:
    name, ext = filetype.split(".")

    if ext == "jpg":
        ext = "jpeg"

# Now it prints correctly, no matter what
print(name + "/" + ext)
