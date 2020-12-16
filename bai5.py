import webbrowser

secret_k = str(input("Nhap ma bi mat: "))
if secret_k == "PIIC":
    webbrowser.get("C:/Users/DELL/AppData/Local/CocCoc/Browser/Application/browser.exe %s").open("https://www.facebook.com/PDU-ICT-Innovation-Club-113919850516929")
    # webbrowser.open('{https://www.facebook.com/PDU-ICT-Innovation-Club-113919850516929}')
else:
    print("Access denied")