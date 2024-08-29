# StudentHub
#### Video Demo:  <https://youtu.be/tXZ04hXQ67Q>
#### Description:

The StudentHub System is a robust console application designed to handle all the basic functions to manage the students of a university, the subjects, and the relations between these two, taking into account the grades. It is developed to handle specific error situations, complex functionalities, good performance, and good tracking of the information, ensuring data integrity, ease of access, and user-friendly interaction via the console.

## Project Overview

The StudentHub System is a Python-based system that leverages object-oriented programming principles to create an intuitive and modular structure. The system comprises several interdependent classes, each responsible for specific aspects of student data management. This modular approach facilitates easy maintenance, scalability, and future enhancements.

### Key Features

- **Student Information Management**: Allows detailed storage and management of student personal information, such as name, ID, age, height, and weight.
- **Course Enrollment**: Enables students to enroll in various courses and tracks their academic progress using the grades.
- **Data Validation**: Ensures that all student data inputs adhere to specified formats and constraints, maintaining data integrity.
- **Extensibility**: The system's design allows for easy addition of new features and modules.
- **Documentation**: The system's documentation is comprehensive, providing other developers with good insight into all classes, functions, tests, etc., using docstrings.

## Files and Structure

### `project.py`

This is the core file of the system. It imports all the classes and integrates all the main logic of the system through menus, calling functions, etc. It maintains two lists, one representing the students in the system and one for the subjects or courses. It contains the main logical functions like registering a student, a subject, reporting students, reporting grades, verifying duplicates of ID or subject codes, etc.

### `estudiante.py`

This file defines the `Estudiante` class, which handles all student-related data and operations. Key attributes include `nombre`, `cedula`, `edad`, `estatura`, `peso`, and `lista_materias`, which represents the subjects the student is enrolled in and their grades. The class provides methods for setting and getting these attributes, ensuring data validation through regular expressions and logical constraints.

### `materia.py`

This file contains the `Materia` class, which represents individual courses. Attributes include the course name and the code, which, thanks to system validations, is unique among all other subjects or courses. This class is fundamental in defining the courses that students can enroll in.

### `estudiante_materia.py`

This file defines the `Estudiante_Materia` class, which links students with their courses. It includes attributes for the course, semester, and a list of grades (each grade is an object of the `Nota` class). This class is crucial for making the relation between the student and a subject. Also, because it includes a semester number, a student can register the same subject multiple times in different semesters.

### `nota.py`

This file defines the `Nota` class, which is basic, containing two attributes: score and description. This class handles specific operations regarding grades in a separate entity, making the system easier to comprehend and develop.

### `test_project.py`

As one of the system's requirements, this file contains all the tests needed to ensure the system works perfectly, testing unit by unit or component by component of the `project.py` file. It was created using the `pytest` library.

## Design Choices

### Data Validation

One of the critical design choices was implementing rigorous data validation for student attributes. This ensures that all data entered into the system is consistent and error-free. Regular expressions are used for validating string inputs like `nombre` and `cedula`, while logical constraints ensure that numerical values like `edad`, `estatura`, and `peso` are within acceptable ranges.

### Object-Oriented Design

Adopting an object-oriented approach allows for a clean and organized codebase. Each class is responsible for a specific part of the system, promoting modularity and reusability. This design choice also makes it easier to extend the system in the future by adding new classes or enhancing existing ones.

### Extensibility and Scalability

The system is designed with future growth in mind. New features, such as additional student attributes or more complex academic tracking, can be seamlessly integrated into the existing structure. This is facilitated by the clear separation of concerns and the use of well-defined interfaces between classes.

## Future Enhancements

The StudentHub System is a robust foundation for a comprehensive student data management platform. Potential future enhancements include:

- **Enhanced Reporting**: Providing detailed academic performance reports and analytics.
- **Mobile Compatibility**: Developing a mobile application interface for easier access and management on the go.
- **Integration with Learning Management Systems**: Connecting with popular LMS platforms to streamline course management and academic tracking.

The StudentHub project demonstrates a commitment to creating a modern, efficient, and user-friendly system for managing student data. By leveraging the power of Python and adhering to best practices in software design, this project lays the groundwork for a scalable and maintainable solution in the educational domain.

## Conclusion

This system was created by Dava2310, or my real name Daniel Alberto Vetencourt Alvarez, at the age of 22. Thanks to all the knowledge gained in the course and my studies, as an Informatic Engineer and a current student of Systems Engineering, I aimed to design the best console-based system I could, using best practices for documentation, development, testing, etc. Thanks to CS50p for allowing people like me to understand more about the programming world.
