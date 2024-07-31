# Messaging System API
A RESTful Django-based API to create and retrieve messages between users.

## Installation
1. Clone the project locally: `git clone git@github.com:georgeburry/messaging-system-api.git`.
2. Create a virtual environment using the latest version of Python (version 3.12.4).
3. Install the required packages: `pip install -r requirements.txt`.
4. Copy the file `messaging_system/settings_template.py` within the same directory with the name `settings.py`.
5. Add the secret key by assigning it to the variable `SECRET_KEY` in the `settings.py file`.
6. Run `python manage.py migrate` in the terminal to apply tables/schema to the database.
7. Create a superuser in the terminal: `python manage.py createsuperuser` and follow the instructions.

## Usage instructions
1. Run the Django server in the terminal: `python manage.py runserver`.
2. Go to the browser, navigate to: http://127.0.0.1:8000/admin and login with your superuser credentials.
3. You can now go to the `User` table (see the pane on the left) and create some fictional users.
4. Log out and log back in as one of the fictional users.
5. If you now go to: http://127.0.0.1:8000/threads/messages/, you can use the API browser to create, retrieve and search for messages.
6. To create a message, go to: http://127.0.0.1:8000/threads/messages/create/ and in the Content box, add the following JSON string and click `POST`:
```html
{
    "content": "Your message here.",
    "user_ids": [2]    # The ID of another user
}
```
7. You can now log out and log back in as other users to create more messages authored by different users.
8. After you have created messages going back and forth between different users, you can see the messages in a thread by going to:
http://127.0.0.1:8000/threads/messages/retrieve/?user_id=ID, where ID is the id of another user. This will show you the thread in chronological order.
9. You can also search for a message like so (note that there are two query parameters): http://127.0.0.1:8000/threads/messages/search/?user_id=3&keyword=Hello
