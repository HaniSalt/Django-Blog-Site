# Mini Blog Web Application

This is a mini web application built with Django to manage blog posts. It allows users to add new posts, list posts, filter posts through a keyword search, view posted pages, and like posts.

## Features
- **Add a new post**: Users can create a new blog post with a title and content. Once done they are able to submit this post which would appear in the list.
- **List posts**: All posts are displayed on the home page, sorted by creation date (newest first).
- **Filter posts**: Users can search for posts by entering a substring in the search bar. The search checks both the title and content of posts.
- **View post details**: Clicking on a post title takes the user to a detailed view of the post. Once done, the user may return to the main page.
- **Like a post**: Users can like a post without reloading the page. The like button updates dynamically.

## Requirements
- Python 3.8+
- Django 4.2+

## Installation
1. Clone the repository:
   git clone <repository-url>

2. Move to the cloned directory: cd blog

3. Create a virtual environment and activate it:
python -m venv venv

4. Install dependencies: pip install -r requirements.txt

5. Apply migrations to set up the database: python manage.py migrate

6. Run the development server: python manage.py runserver