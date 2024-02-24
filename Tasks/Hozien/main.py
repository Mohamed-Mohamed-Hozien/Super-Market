def admin_Pass(oldPass, newPass):
    oldPass = input('enter your old password: ')
    with open("adminPass.txt", "r+") as filereader:
        Pass_read = filereader.readline()
        for i in Pass_read:
            if oldPass == i:
                newPass = input('enter your new password: ')
                newPassWrite = filereader.write(newPass)
                return 1
            else:
                return print('please enter a valid password')
print(admin_Pass())