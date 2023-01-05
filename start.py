from os.path import isfile
from user import getUser
from user import menu

option = menu.getMenuItems()

option = int(option)

if option == 1:
    username = getUser.getUsername()
    email = getUser.getEmail()
    if isfile("users.html") == True:
        ## the file exists
        with open("users.html", "r") as fileObject:
            data = fileObject.read()
            tbody_location = data.find("</tbody>")
            rest_part = data[tbody_location:]
            first_part = data[0:tbody_location]

            new_data = "<tr><td>"+ username + "</td><td>"+ email + "</td></tr>"
            first_part = first_part + new_data

            new_data_entry = first_part + rest_part

            new_file_object = open("users.html", "w")
            new_file_object.write(new_data_entry)
            new_file_object.close()


    else: 
        ## the file does not exist
        with open("users.html", "w") as fileObject:
            fileObject.write("<html><head><title>Users Data</title></head>")
            fileObject.write("<body>")
            fileObject.write("<table border='1'><thead><th>Username</th><th>Email Address</th></thead><tbody><tr><td>" +username+ "</td><td>"+ email + "</td></tr></tbody></table>")
            fileObject.write("</body></html>")

elif option == 2:
    email = input("Enter email address to delete: ")
    print("Delete entry with the email: " + email)


