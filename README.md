# Intermediate Studies Project: Minesweeper App
This application allows the user to play the game minesweeper. The player uses they mouse to reveal and flag tiles until they fully clear the board or lose because they found a mine.

# Documentation
- [Specification Document](documentation/specification_document.md)
- [Time Tracking Document](documentation/time_tracking.md)
- [Changelog Document](documentation/changelog.md)
- [Architecture Document](documentation/architecture.md)

# Python version requirements
This application was tested on python version 3.12.10. 3.12 in general should be fine, but newer versions lack pygame functionality, and older ones may have other problems.

# User Guide
- Use **poetry install** to install dependencies
- Use **poetry run invoke start** to run the app
- Use **poetry run invoke test** and **poetry run invoke coverage-report** to run tests
- Use **poetry run invoke pylint** to check code quality
