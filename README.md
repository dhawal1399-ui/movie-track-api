# Movie Watchlist

A Django-based web application to manage and track your personal movie watchlist. Add, remove, and mark movies as watched, and keep your movie collection organized.

## Features

- Add movies to your watchlist
- Mark movies as watched or unwatched
- Remove movies from your watchlist
- User authentication (login/register)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dhawal1399-ui/movie-track-api.git
    cd movie-track
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

- `movies/` - Main app for managing the watchlist
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS)
- `postgresql` - postgresql

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)