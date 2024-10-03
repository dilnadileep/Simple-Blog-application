# Simple Blog Application

## Overview

The Simple Blog Application is a feature-rich, user-friendly platform built using Django, allowing users to create, edit, and manage blog posts while providing a seamless user experience. The application supports authentication and user profiles, enabling logged-in users to manage their content. Additionally, the application includes a REST API to programmatically handle blog operations. 

The front-end is styled using **Tailwind CSS** for modern, responsive design, while **Django REST Framework** powers the back-end API. The application is designed with modularity and extensibility in mind, making it suitable for various blogging scenarios.

## Core Functionalities

### 1. User Authentication & Profile Management
- **Signup:** New users can register by providing a username, email, and password.
- **Login/Logout:** Existing users can log in and log out securely.
- **Profile Management:** Logged-in users can update their profile information such as their username and email.
- **User-Specific Content:** Only the logged-in users can view and manage their own posts, ensuring personalized access to content.

### 2. Blog Post Management
- **Create Blog Posts:** Logged-in users can create a new blog post. Each post contains a title and content, which supports rich text formatting via a **rich text editor** (powered by Django CKEditor).
- **View All Posts:** Users can view a list of all published blog posts. Pagination is implemented to ensure efficient browsing through posts.
- **View Single Post:** Users can click on a specific blog post to view its full content, along with the post's creation and update details.
- **Edit Blog Posts:** Users can edit the content of their own blog posts.
- **Delete Blog Posts:** Users can delete their own blog posts.
- **Author Ownership:** Posts are owned by their creators, ensuring that only the post author has permission to edit or delete a post.

### 3. REST API
The application also includes a REST API to allow external applications or clients to interact with the blog posts. The API uses **Token-based authentication** to secure access.

- **POST** `/api/posts/`: Create a new blog post (authentication required).
- **GET** `/api/posts/`: Retrieve a list of all blog posts.
- **GET** `/api/posts/<id>/`: Retrieve a specific blog post by ID.
- **PUT** `/api/posts/<id>/`: Update a specific blog post (authentication required; only the author can update their post).
- **DELETE** `/api/posts/<id>/`: Delete a specific blog post (authentication required; only the author can delete their post).

### 4. Rich Text Editor
The blog post content supports rich text formatting, allowing users to create well-structured posts with features like:
- Text styling (bold, italics, underline)
- Bullet points and numbered lists
- Hyperlinks, images, and videos

This is achieved using **Django CKEditor**, which provides a user-friendly interface for text editing.

### 5. Pagination
- The blog post listing view supports pagination, ensuring that users can browse through blog posts efficiently, even when the number of posts grows large.
- Users can navigate between pages to see older or more recent posts.

### 6. Navigation and User Experience
The application includes a clean and intuitive navigation bar, styled with **Tailwind CSS**, allowing users to easily access the following:
- **Profile page**: Users can update their profile.
- **Create post**: Users can add a new blog post.
- **View all posts**: A paginated list of all blog posts.
- **Logout**: Users can securely log out from their account.

## Technical Stack

### Front-End:
- **Tailwind CSS**: For responsive, modern styling without the need for complex custom CSS.
- **Django CKEditor**: For rich text content editing in blog posts.

### Back-End:
- **Django**: The web framework that handles routing, ORM, and templating.
- **Django REST Framework**: For building a robust and extensible API.
- **MySQL**: The relational database used to store user data, blog posts, and related information.

### Other Tools:
- **Django Token Authentication**: Used to secure the API endpoints, ensuring that only authenticated users can perform certain actions.
- **Pagination**: Built-in Django functionality for efficient display and navigation through lists of content.

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/simpleblog.git
cd simpleblog
