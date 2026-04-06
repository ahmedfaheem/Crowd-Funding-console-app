
from auth import login,register
from project import listAll,listMyProjects,createProject,searchProjectsByDate,deleteProject,editProject

def menu():
    while True:
        print("\n\nWelcome to Crowdfunding App")
        print("1- Login")
        print("2- Register")
        print("3- Exit")

        slection = input("select option: ").strip()
   
        if slection == "1":
            user = login()
            if user:
                print(f"\n\nWelcome {user['first_name']} {user['last_name']}")
                while True:
                    print("\n\n1- Create Project")
                    print("2- View My Projects")
                    print("3- View All Projects")
                    print("4- Search Projects By Date")
                    print("5- Delete Project")
                    print("6- Edit Project")
                    print("7- Logout")

                    option = input("select option: ").strip()

                    if option == "1":
                        createProject(user['id'])
                    elif option == "2":
                        listMyProjects(user['id'])
                    elif option == "3":
                        listAll()
                    elif option == "4":
                        searchProjectsByDate()
                    elif option == "5":
                        deleteProject(user['id'])
                    elif option == "6":
                        editProject(user['id'])
                    elif option == "7":
                        print("\n\nLogout successful")
                        break
                    else:
                        print("Invalid option")


        elif slection == "2":
            register()
        elif slection == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option")
            menu()
