# Django Blog Application

This is a simple blog application built with Django. It allows users to view, share, comment on, and read posts. It also includes functionality for filtering posts by tags, viewing posts from specific authors, and sharing posts via email. The app also displays similar posts based on shared tags and offers pagination for the post list.

## Features

- **Post List**: Displays all posts with pagination. Users can filter posts by tags.
- **Post Detail**: Displays the details of a specific post, including comments and similar posts.
- **Post Share**: Allows users to share a post via email.
- **Post Comment**: Users can comment on posts, and the comments are displayed on the post detail page.
- **Author Details**: Displays a profile page for each author, including a list of posts written by that author.

## Requirements

- Python 3.10
- Django 5.1 or higher
- PostgreSQL (or another database backend)
- Django Taggit for managing tags on posts

## Setup Instructions

### Step 1: Clone the repository
```bash
git clone https://github.com/ABHISHEKGHARAMI/django-blog-1.0/
cd mysite