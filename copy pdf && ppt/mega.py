from mega import Mega


mega = Mega()
email = "chiragpatil7378@gmail.com"  
password = "*********7" 
m = mega.login(email, password)


local_file_path = "C:\\Users\\CHIRAG\\Downloads\\1695557305376.jpg"
mega_folder_name = "ml"  # Replace with your desired folder name


file = m.upload(local_file_path, m.find(mega_folder_name)[0])

print("File uploaded successfully!")
