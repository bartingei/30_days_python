import qrcode

url = input("Enter Your url or text ")

img = qrcode.make(url)

img.save('qrcode.png')

print("qrcode created successfully") 