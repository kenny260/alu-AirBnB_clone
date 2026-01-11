#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit the console."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance, save it, and print its id."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances, optionally filtered by class."""
        args = shlex.split(arg)
        objects = storage.all()
        result = []

        if len(args) == 0:
            for obj in objects.values():
                result.append(str(obj))
            print(result)
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        for key, obj in objects.items():
            if key.startswith(args[0] + "."):
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance by adding or updating an attribute."""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3]

        # Cast attribute type if possible
        if hasattr(obj, attr_name):
            current_type = type(getattr(obj, attr_name))
            try:
                attr_value = current_type(attr_value)
            except Exception:
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
