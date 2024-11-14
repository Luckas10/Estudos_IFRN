# Race Registration Project

## Description

This project consists of a race registration system where users can log their races, associating each one with a specific event. The system allows user authentication, event management, and viewing registered races.

## Features

- **User Registration**: Allows new users to sign up for the system and log in.
- **Event Management**: Users can view and select existing events to associate with their races.
- **Race Registration**: Users can log races, providing the date, time, distance, and related event.
- **Race List**: Displays all registered races with details about each one, including the event name.
- **Race Removal**: Allows users to delete previously registered races.

## Technologies Used

- **Flask**: Web framework used to build the application.
- **MySQL**: Relational database for storing information about users, events, and races.
- **Flask-Login**: Library for managing user authentication.

## Database Structure

- **Users**: Table that stores information about system users.
- **Events**: Table that contains events to which races are associated.
- **Races**: Table that logs races, including date, time, distance, and event reference.

## How to Run the Project

1. Clone the repository:
   ```bash
   https://github.com/Renezin13/Sistema-Web-Corridas.git
