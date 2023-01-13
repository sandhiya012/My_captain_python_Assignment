mydic={ ".py": "python",
        ".java":"java",
        ".jpg":"jpg",
        ".c":"c",
        ".c++":"c++",
        ".txt":"text",
        ".pdf":"pdf",
        }

import os
file_name=input("Enter a file name: ")
file_extension=os.path.splitext(file_name)[1]
print("The file extension = ",file_extension)
new=mydic.get(file_extension)
print(new)
