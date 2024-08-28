# 2D Sand Simulation

This project is a simple 2D sand simulation created using Python and the Pygame library. It visually simulates falling sand particles that react to the environment, producing natural and interesting patterns.

## Features

- Realistic Sand Physics: Sand particles fall under gravity and interact with each other, mimicking real-world sand behavior.
- Interactive Simulation: Users can add sand particles by clicking and holding the left mouse button, allowing for the creation of custom patterns.
- Grid-Based Particle Management: The simulation uses a grid system to efficiently manage particle positions and movement.
- Smooth Animation: The simulation runs smoothly with a consistent frame rate for an engaging user experience.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SaiSrikarK03/Sand-Simulation-2D.git
    cd 2d-sand-simulation
    ```

2. Install required packages:
    Ensure you have Python installed. Then, install the required packages using pip:
    ```bash
    pip install pygame numpy
    ```

3. Run the simulation:
    ```bash
    python sand_simulation.py
    ```

## How to Use

- Add Sand: Click and hold the left mouse button to continuously add sand particles at the mouse's location.
- Quit Simulation: Click the close button on the window or press `Esc` to exit.

## Code Overview

- Grid Class: Manages the sand particles in a 2D grid, updating their positions and handling interactions.
- Main Function: Sets up the Pygame window, handles user input, and runs the simulation loop.

## Potential Improvements

- Add different types of particles with unique behaviors, such as water or oil.
- Introduce obstacles or boundaries to interact with the sand particles.
- Optimize performance for larger grids or more complex interactions.

## Requirements

- Python 3.x
- Pygame
- NumPy

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pygame](https://www.pygame.org/) - Python game development library.
- [NumPy](https://numpy.org/) - Library for numerical computations.

---

Enjoy experimenting with this 2D sand simulation and have fun exploring the world of physics-based animations!
Additionally i have also created cement failling simulation , do check that out aswell!
