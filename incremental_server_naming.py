"""
This is my solution to the challenge at https://www.careercup.com/question?id=5716032870678528.
The exercise was to create a program that can incrementally name servers of different types. When one server is taken
offline (it was called exploded in the task, so that's what I called it as well) it's name can be given to a new one.
Servers should always have the lowest available number at the end of their name.
"""
import re


class Hypervisor:
    """
    I called it Hypervisor because you might use one to manage servers. I really didn't know what to call this class tbh
    """

    servers = {}
    """
    A dictionary containing all server types.
    The types themselves will contain all servers that belong to them.
    """

    def add_server(self, kind):
        """
        Ads a server of the given kind.
        Returns the server's full name with number
        :param str kind:
        :return str:
        """
        try:
            found_nums = sorted(self.servers[kind])
            # Gets all server numbers from the given kind and sorts them
            smallest_num = None
            largest_num = found_nums[len(found_nums) - 1]
            c = 1
            while smallest_num is None and c < largest_num:
                if not found_nums[c - 1] == c:
                    """
                    checks if there is a gap in the function at c. If there is one use c for the number of the next 
                    server
                    """
                    smallest_num = c
                c += 1
            if smallest_num is None:
                # if there was no gap, use the largest given number + 1
                smallest_num = largest_num + 1
            new_name = kind + str(smallest_num)
            self.servers[kind].append(smallest_num)
        except KeyError:
            # If the kind is not defined, define it and add the server with the number 1
            new_name = kind + "1"
            self.servers[kind] = [1]
        return new_name

    def blow_server_up(self, name):
        """
        Removes the server with the given name.
        Returns False if there is no server with that name and true otherwise.
        :param str name:
        :return bool:
        """
        server = re.search(r"([a-zA-z]+)([0-9]+)", name)
        try:
            self.servers[server.group(1)].remove(int(server.group(2)))
            return True
        except KeyError:
            return False

    def list_servers(self):
        """
        Returns a list of all servers
        :return list:
        """
        ret = []
        for index, server_kind in self.servers.items():
            for server_num in server_kind:
                ret.append(index + str(server_num))
        return ret


def main():
    user_input = "start"
    visor = Hypervisor()
    while not user_input == "":
        print("What do you want to do?")
        print("0: Add a server")
        print("1: Blow a server up")
        print("2: List all servers")
        print("Don't enter anything to exit.")
        user_input = input()
        if user_input == "0":
            print("What is the kind of the server you want to add?")
            print(visor.add_server(input()))
        elif user_input == "1":
            print("Which server do you want to blow up?")
            if visor.blow_server_up(input()):
                print("Server was destroyed.")
            else:
                print("Server could not be found.")
        elif user_input == "2":
            for server_name in visor.list_servers():
                print(server_name)
        elif user_input == "":
            print("Goodbye")
        else:
            print("Unrecognized input. Please try again")


main()
