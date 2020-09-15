from app.models import CoffeeMachine, CoffeePod


def test_machine_code(client):
    """
    test that machine model has a code attribute after saving
    """
    machine = CoffeeMachine()
    machine.product_type = 'COFFEE_MACHINE_SMALL'
    machine.model = 'base'
    machine.save()
    assert machine.code == 'CM001'


def test_machine_waterline(client):
    """
    test that machine model has a water_line_compatible attribute
    set to True after saving a delux model
    """
    machine = CoffeeMachine()
    machine.product_type = 'COFFEE_MACHINE_SMALL'
    machine.model = 'deluxe'
    machine.save()
    assert machine.code == 'CM003'
    assert machine.water_line_compatible is True


def test_pod_code(client):
    """
    test that machine model has a code attribute after saving
    """
    pod = CoffeePod()
    pod.product_type = 'COFFEE_POD_LARGE'
    pod.coffee_flavor = 'VANILLA'
    pod.pack_size = 'dozen_12'
    pod.save()
    assert pod.code == 'CP101'
