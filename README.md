# Memory-Math-Master
An educational arithmetic-based memory matching game built using Python and Pygame, designed for primary school students. The game helps children improve both memory and maths skills through interactive gameplay.

## 📌 Overview

Memory Math Master challenges players to match arithmetic equations with their correct answers. The game includes animations, difficulty levels, a timer, scoring system, and a child-friendly interface.
Developed as part of the TIP project at Swinburne University.

## 🏗️ Architecture

The project follows a modular architecture to ensure clarity, reusability, and easy maintenance. Gameplay logic, UI rendering, constants, and assets all live in separate files.

## 📁 Project Structure

## main.py
Controls overall game flow — menu, how-to-play screen, gameplay transitions.

## menu.py
Displays buttons for Easy, Medium, Difficult, How to Play, Exit.

## game.py
Contains the Game class: card generation, timer, scoring, matches, and rendering logic.

## card.py
Defines the Card class with flip animations and match logic.

## ui.py
Reusable UI functions to draw cards, timer, score, and move counter.

## score_manager.py
Handles score updates during gameplay.

## constants.py
Centralised values like colours, dimensions, and fonts.

## assets / images
Fonts and images for congratulatory and game-over screens.


### Game Screenshots
<img width="995" height="722" alt="Screenshot 2025-11-19 at 3 28 25 PM" src="https://github.com/user-attachments/assets/9afc7484-dfa5-4cf9-b5b7-48d12ab22849" />
<img width="995" height="720" alt="Screenshot 2025-11-19 at 3 28 36 PM" src="https://github.com/user-attachments/assets/31739c9d-d18b-4b0c-b004-41f2bd12be84" />
<img width="998" height="724" alt="Screenshot 2025-11-19 at 3 25 10 PM" src="https://github.com/user-attachments/assets/c9a869ad-432d-4416-ab48-0b723a788cee" />
<img width="960" height="724" alt="Screenshot 2025-11-19 at 3 29 42 PM" src="https://github.com/user-attachments/assets/be1c9b6e-7ae4-4d9a-ba66-a75aae3be9fc" />


