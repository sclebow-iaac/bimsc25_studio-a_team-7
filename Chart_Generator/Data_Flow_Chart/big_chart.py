import os

class DataNode:
    def __init__(self, sender, receiver, data_name, software):
        self.sender = to_list(sender)
        self.receiver = to_list(receiver)
        self.data_name = data_name
        self.software = to_list(software)

def to_list(obj):
    if isinstance(obj, list):
        return obj
    return [obj]
    
def write_data(file_name, data):
    with open(file_name, 'w') as f:

        for d in data:
            # Write the data node to the file
            # Remember that sender, receiver, and software are lists

            # Convert the lists to strings
            sender = '|'.join(d.sender)
            receiver = '|'.join(d.receiver)
            software = '|'.join(d.software)
            
            f.write(f'{sender},{receiver},{d.data_name},{software}\n')

def read_data(file_name):
    data = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            # Read the data node from the file
            sender, receiver, data_name, software = line.strip().split(',')
            sender = sender.split('|')
            receiver = receiver.split('|')
            software = software.split('|')

            add_data_node(data, sender, receiver, data_name, software)
    return data

all_teams = [
    'Services',
    'Residential',
    'Industrial',
    'Structure',
    'Facade',
    'Data'
]

all_software = [
    'Revit',
    'Rhino',
    'Grasshopper',
    'Dynamo',
    'Excel',
    'Drive',
    'Speckle',
    'Miro',
    'Slack',
]

def check_list(l1, l2):
    # print(f'Checking {l1} and {l2}, result: {set(l1) == set(l2)}')
    return set(l1) == set(l2)
    
def add_data_node(data, sender, receiver, data_name, software):
    # Check if the sender, receiver, and software are valid
    sender = to_list(sender)
    receiver = to_list(receiver)
    software = to_list(software)

    # print(f'Sender: {sender}')
    # print(f'Receiver: {receiver}')
    # print(f'Data Name: {data_name}')
    # print(f'Software: {software}')

    
    # Check if the data node already exists
    for d in data:
        # Check if the sender, receiver, data_name, and software are the same        
        if check_list(d.sender, sender):
            if check_list(d.receiver, receiver): 
                if d.data_name == data_name: 
                    if check_list(d.software, software):

                        print('Data node already exists')
                        return data
        
        
    data.append(DataNode(sender, receiver, data_name, software)) # Add the data node
    print('Data node added')

    return data

if __name__ == '__main__':
    # Check if data.txt exists
    if not os.path.exists('data.txt'):
        print('data.txt does not exist')
        
        # Create a blank data.txt file
        with open('data.txt', 'w') as f:
            f.write('')

    data = read_data('data.txt')
    for d in data:
        print(d.sender, d.receiver, d.data_name, d.software)

    # Add a new data node
    data = add_data_node(data, ['Services'], ['Data'], 'Concept Visualization', ['Miro'])
    data = add_data_node(data, ['Services'], ['Residential', 'Industrial', 'Structure'], 'Topological Map', ['Excel', 'Drive', 'Speckle', 'Miro'])
    data = add_data_node(data, ['Services'], ['Residential', 'Industrial', 'Structure'], 'Neighborhood Program', ['Grasshopper', 'Excel'])

    # Make a command line interface to add data nodes
    run = True
    while run:
        print('Exit any time by typing "exit"')

        # Get the senders one by one
        senders = []
        while True:
            sender = input('Enter the sender team: ')
            if sender == 'exit':
                run = False
                break
            elif sender == '':
                break
            if sender in all_teams:
                senders.append(sender)
            else:
                print('Invalid team')

        if not run:
            break

        # Get the receivers one by one
        receivers = []
        while True:
            receiver = input('Enter the receiver team: ')
            if receiver == 'exit':
                run = False
                break
            elif receiver == '':
                break
            if receiver in all_teams:
                receivers.append(receiver)
            else:
                print('Invalid team')

        if not run:
            break

        # Get the data name
        data_name = input('Enter the data name: ')
        if data_name == 'exit':
            run = False
            break

        # Get the software one by one
        softwares = []
        while True:
            software = input('Enter the software: ')
            if software == 'exit':
                run = False
                break
            elif software == '':
                break
            if software in all_software:
                softwares.append(software)
            else:
                print('Invalid software')

        if not run:
            break

        data = add_data_node(data, senders, receivers, data_name, softwares)
    
    write_data('data.txt', data)
    data = read_data('data.txt')
    for d in data:
        print(d.sender, d.receiver, d.data_name, d.software)