# Dice Dance

A simple web-based dice roller built with Django, allowing users to roll single or multiple dice with various sides and keeping a history of rolls within their session.

## Features

* **Single and Multiple Dice Rolling:** Easily switch between rolling just one die or several at once.
* **Selectable Number of Sides:** Choose from standard dice sizes (D6, D8, D10, D12, D20).
* **Persistent State:** Your selected mode (single/multiple), number of dice, and number of sides are remembered across requests using Django sessions.
* **Latest Roll Display:** See the results and total of your most recent roll.
* **Roll History:** View a list of your previous rolls during the current session.
* **Clear History:** Option to clear your roll history.

## Prerequisites

Before you begin, ensure you have the following installed:

* Python (3.7+)
* Django (3.2+)
* A database system supported by Django (SQLite is used by default for development and is sufficient).

## Setup

Follow these steps to get the Dice Dance component running locally:

1.  **Clone the Repository:** (Assuming your project is in a Git repository)
    ```bash
    git clone <https://github.com/AlokKumar-04/Dice-Simulator>
    cd <Dice-Simulator>
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    * On Windows: `venv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate`

3.  **Install Dependencies:**
    ```bash
    pip install Django
    ```

4.  **Configure Database:**
    If you are not using the default SQLite database, update the `DATABASES` setting in your project's `settings.py`.

5.  **Apply Database Migrations:**
    The session framework requires database tables. Run migrations to create them.
    ```bash
    python manage.py migrate
    ```
    *(This command creates necessary tables, including `django_session` for database-backed sessions).*

6.  **Include Dice URLs:**
    Ensure your project's `urls.py` file includes the URLs for the Dice app, preferably with a namespace. Assuming your Dice app is named `dice` (lowercase) and your project is set up to include its URLs:

    ```python
    # <Dice>/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('dice.urls', namespace='Dice')), # Updated app name to lowercase 'dice'
        # Add other project URLs here
    ]
    ```
    *(Note: I've changed `Dice.urls` to `dice.urls` and the namespace remains `Dice` as used in your template, assuming your app directory is named `dice` in lowercase).*

7.  **Verify App in `INSTALLED_APPS`:**
    Make sure `'dice'` (lowercase) and `'django.contrib.sessions'` are included in the `INSTALLED_APPS` list in your project's `settings.py`.

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1.  Open your web browser and navigate to the URL where the dice application is served (e.g., `http://127.0.0.1:8000/dice/`).
2.  Select either "Single Die" or "Multiple Dice" mode.
3.  If in "Multiple Dice" mode, enter the number of dice you want to roll in the input field.
4.  Select the desired number of sides from the "Number of Sides" dropdown.
5.  Click the "Roll Dice" button.
6.  The latest roll results and total will appear.
7.  Your roll will be added to the "Roll History" list.
8.  Click the "🗑️ Clear history" button to remove all entries from the roll history for your session.

## Project Structure (Relevant Files)

* `manage.py`: Django's command-line utility.
* `<DiceDance>/settings.py`: Project settings, including `INSTALLED_APPS`, `DATABASES`, etc.
* `<DiceDance>/urls.py`: Project-level URL configurations, including the include for the Dice app.
* `dice/views.py`: Contains the `RollDice` and `clear_dice_history` view functions.
* `dice/urls.py`: Contains URL patterns specific to the Dice app, including patterns for `RollDice` (named `roll_dice`) and `clear_dice_history` (named `clear_dice_history`).
* `dice/templates/dice/index.html`: The main HTML template for the dice roller interface.
