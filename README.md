# AirBnB Clone - The Console

## Description
This is the first step towards building a full web application: an AirBnB clone. This project implements a command interpreter to manage AirBnB objects.

## Command Interpreter
The command interpreter allows you to:
- Create new objects (ex: User, State, City, Place)
- Retrieve objects from a file or database
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

### How to Start
```bash
./console.py
```

### How to Use
The console works in both interactive and non-interactive mode.

**Interactive mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) quit
$
```

**Non-interactive mode:**
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update
(hbnb)
$
```

### Available Commands
- `create <class>` - Creates a new instance
- `show <class> <id>` - Shows an instance
- `destroy <class> <id>` - Destroys an instance
- `all [class]` - Shows all instances or all instances of a class
- `update <class> <id> <attribute> <value>` - Updates an instance
- `quit` or `EOF` - Exits the console

### Examples
```bash
(hbnb) create User
b6a6e15c-c67d-4312-9a75-9d084935e579
(hbnb) show User b6a6e15c-c67d-4312-9a75-9d084935e579
[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)}
(hbnb) all
["[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)}"]
(hbnb) update User b6a6e15c-c67d-4312-9a75-9d084935e579 first_name "Betty"
(hbnb) show User b6a6e15c-c67d-4312-9a75-9d084935e579
[User] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 3, 49401), 'first_name': 'Betty'}
(hbnb) destroy User b6a6e15c-c67d-4312-9a75-9d084935e579
(hbnb) show User b6a6e15c-c67d-4312-9a75-9d084935e579
** no instance found **
```

## Testing
Run all tests:
```bash
python3 -m unittest discover tests
```

Run specific test file:
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
See AUTHORS file
