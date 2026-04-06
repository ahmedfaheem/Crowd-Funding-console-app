# Crowdfunding App

A simple Python command-line crowdfunding application with user registration, login, and project management stored in a local JSON file.

## Features

- Register a new user
- Log in with email and password
- Create crowdfunding projects
- View your projects
- View all projects
- Search projects by date
- Edit a project you own
- Delete a project you own

## Project Structure

- `main.py` starts the application
- `menu.py` contains the main menu and navigation flow
- `auth.py` handles registration and login
- `project.py` contains project CRUD and search logic
- `validation.py` contains input validation helpers
- `db.py` reads from and writes to `data.json`
- `data.json` stores users and projects

## Requirements

- Python 3.x
- No third-party packages are required

## How to Run

From the project folder, run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Usage Notes

- Register with a valid first name, last name, email, password, and phone number
- Passwords must be at least 8 characters
- Phone numbers must match the pattern `01XXXXXXXXX`
- Project dates must use the format `YYYY-MM-DD`
- Project titles must contain only letters
- Only the project owner can edit or delete a project

## Data Storage

All application data is stored locally in `data.json`. The file includes two top-level keys:

- `users`
- `projects`

If you want to reset the app, edit or replace `data.json` manually.

## Example Login Data

The sample `data.json` file already contains test users. You can log in with one of those accounts or register a new one.

## Notes

- This is a console-based app with no web interface
- Date comparisons are done using the entered `YYYY-MM-DD` strings