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
