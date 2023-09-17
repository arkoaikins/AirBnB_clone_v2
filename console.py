#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import shlex    # Unix shell-like syntax analyzer
from utility import param_to_dict
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    # Some attributes that are not allowed to be modified manually
    not_updatable = ['id', 'created_at', 'updated_at']

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    # def do_create(self, args):
    #    """ Create an object of any class"""
    #   if not args:
    #       print("** class name missing **")
    #       return
    #   elif args not in HBNBCommand.classes:
    #       print("** class doesn't exist **")
    #       return
    #   new_instance = HBNBCommand.classes[args]()
    #   storage.save()
    #   print(new_instance.id)
    #   storage.save()

    def do_create(self, args):
        """
        Create a new instane

        Param syntax: <key name>="<value>"

        * Any double quote inside the value must be escaped with a bacsklash
        * All underscores in the value are replaced by spaces.

        Usage:
        ======
        * create <Class name>
        * create <Class name> <param 1> <param 2> ... <param n>
        """
        # Fetcah all arguments
        try:
            args = shlex.split(args, posix=True, comments=False)
        except Exception as e:
            print("** Error: {} **".format(e))

        """
        Test to see actual arguments
        for pos in range(len(args)):
            print("\targ[0]: '{}'".format(pos, args[pos]))
        """
        if not args:
            print("** class name missing **")
            return

        _class = args[0]
        if _class not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # Create a dictionary of attributes for the instance
        attr = dict()
        for arg in args[1:]:
            # convert paameter string to dictionary
            element = param_to_dict(arg)
            if (type(element) == dict) and (len(element) != 0):
                attr.update(element)

        # print ("\nAttributes: '{}'\n".format(attr))   # test
        new_instance = HBNBCommand.classes[_class]()

        # Update the instance with the attributes
        for key, value in attr.items():
            setattr(new_instance, key, value)

        # Save the instance to storage
        new_instance.save()
        print(new_instance.id)
        storage.save()

        """
        Test object in storage
        for key, obj in storage.all().items():
            print("{} -> {}".format(key, obj))
        """

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in models.storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in models.storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in models.storage.all().items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return

                # Restrict updating of specifi attributes
                if att_name in HBNBCommand.not_updatable:
                    info = "** The \"{}\" attribute is not allowed \
to be updated **"
                    print(info.format(att_name))
                    return

                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    # AUTO-COMPLETION

    def complete_create(self, text, line, begidx, endix):
        """
        Auto-completion for the 'create' command
        """
        return [completion for completion in self.classes
                if completion.startswith(text)]

    def complete_show(self, text, line, begidx, endix):
        """
        Auto-completion for the 'show' command
        """
        return [completion for completion in self.classes
                if completion.startswith(text)]

    def complete_destroy(self, text, line, begidx, endix):
        """
        Auto-completion for the 'destroy' command
        """
        return [completion for completion in self.classes
                if completion.startswith(text)]

    def complete_all(self, text, line, begidx, endix):
        """
        Auto-completion for the 'all' command
        """
        return [completion for completion in self.classes
                if completion.startswith(text)]

    def complete_update(self, text, line, begidx, endix):
        """
        Auto-completion for the 'update' command
        """
        return [completion for completion in self.classes
                if completion.startswith(text)]

    # HELP

    def help_update(self):
        """
        Provide documentation on the 'update' command
        """
        print("Update an instance based on class name and id by adding or \
updating attributes")
        print("Usage: update <class name> <id> <attribute> <value>")
        print()

    def help_all(self):
        """
        Provide documentation on the 'all' command
        """
        print("Print all string representation of all instances based or not \
on the class name")
        print("Usage:\n\tall [<class name>]")
        print()

    def help_destroy(self):
        """
        Provide documentation on the 'destroy' command
        """
        print("Delete an instance based on the class name and id")
        print("Usage:\n\tdestroy <class name> <id>")
        print()

    def help_show(self):
        """
        Provide documentation on the 'show' command
        """
        print("Print the string representation of an instance based on \
the class name and id")
        print("Usage:\n\tshow <class name> <id>")
        print()

    def help_create(self):
        """
        Provide documentation on the 'create' command
        """
        print("Create a new instance without attributes")
        print("Usage:\n\tcreate <class name>")
        print()
        print("Or create a new instance with attributes")
        print("Usage:\n\tcreate <Class name> <param 1> ... <param n>")
        print("Param syntax: <key name>='<value>'")
        print("Eg. name='My_little_house'")
        print("Any double quote inside value must be escaped with a slash")
        print("All underscores in the value will be replaced by spaces.")
        print()

    def help_quit(self):
        """
        Provide documentation on the quit command
        """
        print("Quit command to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
