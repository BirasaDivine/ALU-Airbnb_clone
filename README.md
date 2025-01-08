# ALU-Airbnb_clone

## Project Overview
This project is a foundational clone of the AirBnB website, focusing on developing a command-line interface (CLI) for managing application data. The first phase includes building a backend console for handling various objects, such as users, places, and states.

---

## Command Interpreter Description
The command interpreter enables users to manipulate data models. Key functions include:
- **Creating objects** (e.g., `User`, `Place`)
- **Retrieving objects** from storage
- **Performing operations** on objects
- **Updating object attributes**
- **Deleting objects**

---

### Launching the Command Interpreter
Run `./console.py` to start the interpreter. Use the `help` command for guidance on available commands.

---

### Using the Command Interpreter

**Create an object:** `create <ClassName>`

**Show an object:** `show <ClassName> <id>`

**Update an object:** `update <ClassName> <id> <attribute_name> <value>`

**Delete an object:** `destroy <ClassName> <id>`

---

### Project Structure
#### Console Development Tasks
1. Create a `BaseModel` parent class for:
   - Initialization
   - Serialization
   - Deserialization
2. Implement serialization/deserialization:
   - Instance ↔ Dictionary ↔ JSON String ↔ File
3. Build models (`User`, `State`, `City`, `Place`, etc.) inheriting from `BaseModel`.
4. Develop a file-based storage engine.
5. Write unittests to ensure functionality.

---

### Running Tests
Run all tests:
```bash
$ python3 -m unittest discover tests
```
Run a specific test:
```bash
$ python3 -m unittest tests/test_models/test_city.py
```
