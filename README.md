# Python Roguelike Game

This is a Python-based Roguelike game that uses `tcod` and `SDL2` for the graphical interface and game driver.

## Table of Contents
- [Setup Development Environment](#setup-development-environment)
- [Install Dependencies](#install-dependencies)
- [Install SDL2](#install-sdl2)
- [Run the Game](#run-the-game)
- [Credits](#credits)

## Setup Development Environment

First, create and activate a Python virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `.\env\Scriptsctivate`
```

## Install Dependencies

Use `pip` to install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Install SDL2

To run the game, you need to have `SDL2` installed on your system. On a Linux machine, you can install SDL2 using the following commands:

### Ubuntu/Debian:

```bash
sudo apt update
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
```

### Fedora:

```bash
sudo dnf install SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel
```

### Arch Linux:

```bash
sudo pacman -S sdl2 sdl2_image sdl2_mixer sdl2_ttf
```

## Run the Game

To start the game, run the following command:

```bash
python main.py
```

Make sure you are in the virtual environment and the dependencies are installed.

## Credits

This project was developed based on the tutorial available at [Roguelike Tutorials](https://rogueliketutorials.com/). Full credit goes to the author of the tutorial.

Feel free to contribute, report issues, or suggest improvements.
