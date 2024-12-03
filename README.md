# Quiz App README

## Overview

This is a simple **Quiz App** built with **Python Django** and **Bootstrap**. The application allows users to take a multiple-choice quiz, see their performance, and navigate through questions with feedback. Users can view their total attempted questions, number of correct answers, and overall score or percentage.

---

## Features

### 1. **Dashboard Page**
   - Displays user performance:
     - Total questions attempted.
     - Number of correct answers.
     - Overall score or percentage.
   - A button labeled **"Take Quiz"** to navigate to the **Quiz Page**.

### 2. **Quiz Page**
   - Displays one random multiple-choice question (MCQ) from the database.
   - Allows the user to select an answer and submit it.
   - After submission:
     - Displays feedback: correct or incorrect.
     - Provides two options:
       - **"Answer More"**: Load another random question.
       - **"End Quiz"**: Redirect the user back to the Dashboard Page.

### 3. **Database**
   - Questions are pre-populated in the database.
   - The database holds the questions and multiple-choice options for the quiz.
   - No interface for creating questions, as they are pre-filled in the database.

---

## Requirements

- **Python 3.9+**: The project is built using Python 3.
- **Django 5.x**: The web framework used for building the application.
- **SQLite** (default database for Django): For storing the questions and quiz data.

---

## Installation Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dhriti987/quiz-app.git
   cd quiz-app
2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
1. **Start the development server**:

   ```bash
   python manage.py runserver
## Running the App

1. **Dashboard Page**:
   - The **Dashboard Page** will display the user's performance, including:
     - Total questions attempted.
     - Number of correct answers.
     - Overall score (percentage).

2. **Quiz Page**:
   - The **Quiz Page** will display a random multiple-choice question from the database.
   - The user can select an answer and submit it.
   - After submitting the answer:
     - The app will check if the answer is correct.
     - Feedback will be displayed: correct or incorrect.
   - The user will have two options after submission:
     - **"Answer More"**: This will load another random question.
     - **"End Quiz"**: This will redirect the user back to the **Dashboard Page**.

3. **End of Quiz**:
   - After completing the quiz, the user's performance data will be displayed on the **Dashboard Page**, including:
     - Total questions attempted.
     - Number of correct answers.
     - Overall score or percentage.
