# Testing Document

The Minesweeper application has been tested using automated unit tests with the Python unittest library, as well as manual system-level tests.

## Unit and Integration testing

### Application Logic

The core logic of the game within the Minesweeper class is tested using the TestMinesweeper test class. Thus, this includes the Cell, Board and Minesweeper classes. A helper method set_mines_for_testing is used to inject specific mine positions into the board, allowing for predictable test scenarios. Classes responsible for the UI were not tested.

### Test Coverage

Test coverage is 100%

ADD IMAGE HERE

This can be verified by running **poetry run invoke coverage-report**

## System Testing

System testing has been performed manually to verify the integration between the logic and the graphical user interface.

The application has been installed and tested on both Windows and Linux environments.

All of the listed functionalities in the [Specification Document](documentation/specification_document.md) have been tested