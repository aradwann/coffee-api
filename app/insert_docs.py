from app.models import CoffeeMachine, CoffeePod

"""
script to insert coffee machine and coffee pod documents in mongodb
"""

machine_type = {
    'CM1': 'COFFEE_MACHINE_LARGE',
    'CM0': 'COFFEE_MACHINE_SMALL',
    'EM0': 'ESPRESSO_MACHINE',
}

machine_model = {
    '1': 'base',
    '2': 'premium',
    '3': 'deluxe',
}

pod_type = {
    'CP1': 'COFFEE_POD_LARGE',
    'CP0': 'COFFEE_POD_SMALL',
    'EP0': 'ESPRESSO_POD',
}
pod_flavor = {
    '0': 'VANILLA',
    '1': 'CARAMEL',
    '2': 'PSL',
    '3': 'MOCHA',
    '4': 'HAZELNUT',
}

pod_size = {
    '1': 'dozen_12',
    '3': 'dozen_36',
    '5': 'dozen_60',
    '7': 'dozen_84',
}


def machine_code_to_model(code):
    """
    transform a machine code into
    a machine model object and save it in mongodb
    Args:
        code (String): machine code
    """
    machine = CoffeeMachine()
    machine.product_type = machine_type.get(code[0:3])
    machine.model = machine_model.get(code[-1])
    machine.save()


def pod_code_to_model(code):
    """
    transform a pod code into
    a pod model object and save it in mongodb
    Args:
        code (String): pod code
    """
    pod = CoffeePod()
    pod.product_type = pod_type.get(code[0:3])
    pod.coffee_flavor = pod_flavor.get(code[3])
    pod.pack_size = pod_size.get(code[-1])
    pod.save()


def insert_machine_docs():
    """
    open txt file with a machine code in each line
    and transform it into a saved document in mongodb
    """
    with open('machine.txt') as f:
        for line in f:
            code = line.split()[0]
            machine_code_to_model(code)
    print('sucessfully inserted machine models')


def insert_pod_docs():
    """
    open txt file with a machine code in each line
    and transform it into a saved document in mongodb
    """
    with open('pod.txt') as f:
        for line in f:
            code = line.split()[0]
            pod_code_to_model(code)
    print('sucessfully inserted pod models')
