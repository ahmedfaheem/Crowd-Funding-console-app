from db import read_data, write_data
from validation import valid_name, valid_date, valid_amount, valid_empty

def listAll():
    print("----------List all projects---------------")
    data = read_data()
    if data is None:
        print("\n\nNo data found")
        return
    if len(data['projects']) == 0:
        print("\n\nNo projects found")
        return
    for project in data['projects']:
        print(f"ID: {project['id']}")
        print(f"Owner ID: {project['owner_id']}")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Total Target: {project['total_target']}")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print("-" * 40)



def listMyProjects(userId):
    print("----------List my projects---------------")
    data = read_data()
    if data is None:
        print("\n\nNo data found")
        return
    count = 0
    for project in data['projects']:
        if project['owner_id'] == userId:
            count += 1
            print(f"ID: {project['id']}")
            print(f"Owner ID: {project['owner_id']}")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']}")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print("-" * 40) 

    if count == 0:
        print("\n\nNo projects found")

def createProject(userId):
    print("----------Create project---------------")
    title = input("Title: ").strip()
    if not valid_name(title):
        print("\n\nInvalid title")
        return
    details = input("Details: ").strip()
    if not valid_empty(details):
        print("\n\nInvalid details")
        return
    total_target = input("Total Target: ").strip()
    if not valid_amount(total_target):
        print("\n\nInvalid total target")
        return
    start_date = input("Start Date: ").strip()
    if not valid_date(start_date):
        print("\n\nInvalid start date")
        return
    end_date = input("End Date: ").strip()
    if not valid_date(end_date):
        print("\n\nInvalid end date")
        return
    
    if start_date > end_date:
        print("\n\nStart date must be before end date")
        return

    data = read_data()

    project = {
        "id": len(data['projects']) + 1,
        "owner_id": userId,
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date
    }

    data['projects'].append(project)
    write_data(data)

    print("\n\nProject created successfully")


def searchProjectsByDate():
    print("----------Search projects by date---------------")
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not valid_date(date):
        print("\n\nInvalid date")
        return

    data = read_data()
    if data is None:
        print("\n\nNo data found")
        return
    if len(data['projects']) == 0:
        print("\n\nNo projects found")
        return
    
    for project in data['projects']:
        if project['start_date'] <= date  and project['end_date'] >= date:
            print(f"ID: {project['id']}")
            print(f"Owner ID: {project['owner_id']}")
            print(f"Title: {project['title']}")
            print(f"Details: {project['details']}")
            print(f"Total Target: {project['total_target']}")
            print(f"Start Date: {project['start_date']}")
            print(f"End Date: {project['end_date']}")
            print("-" * 40)


def deleteProject(userId):
    print("----------Delete project---------------")
    project_id = input("Enter project ID: ").strip()
    if not valid_empty(project_id) and project_id.isdigit():
        print("\n\nInvalid project ID")
        return

    data = read_data()
    if data is None:
        print("\n\nNo data found")
        return
    if len(data['projects']) == 0:
        print("\n\nNo projects found")
        return
    
    project_id = int(project_id)
    
    for project in data['projects']:
        if project['id'] == project_id and project['owner_id'] == userId:
            data['projects'].remove(project)
            write_data(data)
            print("\n\nProject deleted successfully")
            return
    
    print("\n\nProject not found or you dont have permission")



def editProject(userId):
    print("----------Edit project---------------")
    project_id = input("Enter project ID: ").strip()
    if not valid_empty(project_id) and project_id.isdigit():
        print("\n\nInvalid project ID")
        return

    data = read_data()
    if data is None:
        print("\n\nNo data found")
        return
    if len(data['projects']) == 0:
        print("\n\nNo projects found")
        return
    
    project_id = int(project_id)
    
    for project in data['projects']:
        if project['id'] == project_id and project['owner_id'] == userId:
            title = input("Title: ").strip()
            if not valid_name(title):
                print("\n\nInvalid title")
                return
            details = input("Details: ").strip()
            if not valid_empty(details):
                print("\n\nInvalid details")
                return
            total_target = input("Total Target: ").strip()
            if not valid_amount(total_target):
                print("\n\nInvalid total target")
                return
            start_date = input("Start Date: ").strip()
            if not valid_date(start_date):
                print("\n\nInvalid start date")
                return
            end_date = input("End Date: ").strip()
            if not valid_date(end_date):
                print("\n\nInvalid end date")
                return
            
            if start_date > end_date:
                print("\n\nStart date must be before end date")
                return
            
            project['title'] = title
            project['details'] = details
            project['total_target'] = total_target
            project['start_date'] = start_date
            project['end_date'] = end_date

            write_data(data)

            print("\n\nProject edited successfully")
            return
    
    print("\n\nProject not found or you dont have permission")