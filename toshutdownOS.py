import os


def shutdown_pc():
    decision_making = int(input("This pc will shutdown:\n1.To  Restart press 1 \n2.To continue press 2\n3.Log out"))
    if decision_making == 1:
        os.system("Restart /r /t 1")
    elif decision_making == 2:
        os.system("shutdown /s /t 1")
    elif decision_making == 3:
        os.system("shutdown -l")
    else:
        print("Please follow the instruction next time")
        exit()


shutdown_pc()
