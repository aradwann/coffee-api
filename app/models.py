from app import db


machine_type = {
    'COFFEE_MACHINE_LARGE': 'CM1',
    'COFFEE_MACHINE_SMALL': 'CM0',
    'ESPRESSO_MACHINE': 'EM0',
}

machine_model = {
    'base': '1',
    'premium': '2',
    'deluxe': '3',
}

pod_type = {
    'COFFEE_POD_LARGE': 'CP1',
    'COFFEE_POD_SMALL': 'CP0',
    'ESPRESSO_POD': 'EP0',
}
pod_flavor = {
    'VANILLA': '0',
    'CARAMEL': '1',
    'PSL': '2',
    'MOCHA': '3',
    'HAZELNUT': '4',
}

pod_size = {
    'dozen_12': '1',
    'dozen_36': '3',
    'dozen_60': '5',
    'dozen_84': '7',
}


class CoffeeMachine(db.Document):
    """Coffee Machine Mongo Document sub-class to provide
    data validation for monogodb documents
    """
    product_type = db.StringField(
        required=True, max_length=50, choices=tuple(machine_type.keys()))
    model = db.StringField(required=True, max_length=50,
                           choices=tuple(machine_model.keys()))
    water_line_compatible = db.BooleanField(required=True, default=False)
    code = db.StringField()

    def clean(self):
        # deluxe models have a water line compatible property
        if self.model == 'deluxe':
            self.water_line_compatible = True
        # add CoffeMachine code property before saving
        self.code = machine_type.get(self.product_type) +\
            '0' +\
            machine_model.get(self.model)


class CoffeePod(db.Document):
    """Coffee Pod Mongo Document sub-class to provide
    data validation for monogodb documents
    """
    product_type = db.StringField(
        required=True, max_length=50, choices=tuple(pod_type.keys()))
    coffee_flavor = db.StringField(
        required=True, max_length=50, choices=tuple(pod_flavor.keys()))
    pack_size = db.StringField(required=True, choices=tuple(pod_size.keys()))
    code = db.StringField()

    def clean(self):
        # add CoffePod code before saving
        self.code = pod_type.get(self.product_type) +\
            pod_flavor.get(self.coffee_flavor) +\
            pod_size.get(self.pack_size)
