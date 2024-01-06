# ToDoList App

This is a simple ToDoList application built with Django. It allows users to register, log in, and manage their todo items.

## Features

- User registration: Users can create an account with a unique username and email.
- User login: Registered users can log in to their accounts.
- ToDoList management: Users can create, view, and delete their todo items.
- Mark as completed: Users can mark todo items as completed.

## Installation

1. Clone the repository:
  git clone <https://github.com/bomberman2099/django_todolist.git>
2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Apply database migrations:
```
python manage.py migrate
```

4. Start the development server:
   
```
python manage.py runserver
```

5. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Register a new account by providing a unique username and email.
2. Log in to your account using your credentials.
3. Add new todo items by typing them into the input field and pressing Enter.
4. View your todo list with the added items.
5. Mark items as completed by clicking the checkbox next to them.
6. Delete items by clicking the delete button next to them.

