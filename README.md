# alu-AirBnB_clone

## Description of the Project

This repository contains a simplified clone of the AirBnB web application. The goal of the project is to understand how to build a full web application from the ground up by incrementally developing its components. The project covers concepts such as object-oriented programming, serialization/deserialization, file storage, and building a command-line interface (CLI) to manage application data.

At this stage, the project focuses on implementing a **command interpreter (console)** that allows users to create, update, destroy, and retrieve objects representing core AirBnB entities such as users, places, states, cities, amenities, and reviews.

## Description of the Command Interpreter

The command interpreter, also referred to as the **console**, is a command-line tool used to manage the objects of the AirBnB clone application.

It enables the following operations:

* Create new objects (e.g., User, Place)
* Retrieve objects from storage
* Update attributes of existing objects
* Delete objects
* List all objects or all objects of a specific class

The console serves as the foundation for later stages of the project, including the web interface and database integration.

## How to Start the Command Interpreter

1. Clone the repository:

   ```bash
   git clone https://github.com/kenny260/alu-AirBnB_clone.git
   ```
2. Navigate to the project directory:

   ```bash
   cd alu-AirBnB_clone
   ```
3. Run the console:

   ```bash
   ./console.py
   ```

You should see the prompt:

```
(hbnb)
```

## How to Use the Command Interpreter

The console works in interactive mode and non-interactive mode.

### Interactive Mode

Start the console and type commands at the `(hbnb)` prompt.

### Non-Interactive Mode

Commands can be piped into the console:

```bash
echo "help" | ./console.py
```

## Examples

### Create an Object

```bash
(hbnb) create User
```

Output:

```
<unique_id>
```

### Show an Object

```bash
(hbnb) show User <unique_id>
```

### Update an Object

```bash
(hbnb) update User <unique_id> first_name "John"
```

### Destroy an Object

```bash
(hbnb) destroy User <unique_id>
```

### List All Objects

```bash
(hbnb) all
```

### Exit the Console

```bash
(hbnb) quit
```

or

```bash
(hbnb) EOF
```

## Repository Structure

* `console.py` — The command interpreter
* `models/` — Contains the base model and other classes
* `models/engine/` — Storage engine (file storage)
* `tests/` — Unit tests

## Authors

See the `AUTHORS` file for the complete list of contributors.
 BINTHIA NITONDE
