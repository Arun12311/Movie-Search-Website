
# Movie Search Website

## Sample Images

### Home Page
![image](https://github.com/user-attachments/assets/22012dfc-dbf1-4eeb-85c4-acce8008a55e)


### Search Results
![image](https://github.com/user-attachments/assets/576fa9db-99b4-4341-a0f4-976e09d4534f)


### Movie Details
![image](https://github.com/user-attachments/assets/ea995bf0-5159-48a4-9bfd-9b79aa1d9f39)


## Overview

The **Movie Search Website** is a web application built using Flask, Python, HTML, CSS, and Bootstrap. It allows users to search for movies and view detailed information, including the title, year, rating, genres, directors, cast, plot, runtime, country, and language.

## Features

- **Search Movies**: Users can search for movies by entering a movie name in the search bar.
- **Display Search Results**: The application displays a list of movies matching the search query, including the title and release year.
- **Movie Details**: Users can click on a movie from the search results to view detailed information about the movie, such as the director, cast, plot, and more.
- **Responsive Design**: The website is designed to be responsive and works well on various screen sizes, thanks to Bootstrap.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Python**: The programming language used to build the backend logic.
- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **Bootstrap**: A popular CSS framework for responsive design.
- **IMDbPy**: A Python package used to retrieve movie data from IMDb.

## Installation and Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/movie-search-website.git
   cd movie-search-website
   ```

2. **Install Dependencies**:
   ```bash
   pip install IMDbPY flask
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Website**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.

### Directory Structure

```
movies_flask/
│
├── app.py               # Main Flask application file
├── templates/           # HTML templates
│   ├── index.html       # Home page with search form
│   ├── results.html     # Search results page
│   └── movie_info.html  # Movie details page
│

└── README.md            # Project documentation
```


## Usage

1. **Search for a Movie**:
   - Go to the home page, enter the movie name in the search bar, and click the "Search" button.

2. **View Search Results**:
   - Browse through the list of search results. Each result displays the movie title and year of release.

3. **View Movie Details**:
   - Click on any movie from the search results to view detailed information about it.

## Customization

You can easily customize the appearance of the website by modifying the CSS files in the `static/css/` directory or updating the HTML templates in the `templates/` directory.

## Contribution

Contributions are welcome! If you'd like to improve the project, feel free to fork the repository, make changes, and submit a pull request.

