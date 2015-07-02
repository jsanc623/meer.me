class Conversion(object):
    conversions = {
        'mi': {
            'km': 0.621371,
            'in': 0.0000157828,
            'm': 0.000621371,
            'cm': 0.00000621371
        },
        'km': {
            'mi': 1.60934,
            'in': 0.0000254,
            'm': 0.001,
            'cm': 0.00001
        },
        'in': {
            'mi': 63360,
            'km': 39370.1,
            'm': 39.3701,
            'cm': 0.393701,
        },
        'm': {
            'mi': 1609.34,
            'km': 1000,
            'in': 0.0254,
            'cm': 0.01
        },
        'cm': {
            'mi': 160934,
            'km': 100000,
            'in': 2.54,
            'm': 100
        }
    }

    def __init__(self):
        pass

    def convert(self, measurement, from_unit, to_unit):
        accepted_values = ['mi', 'km', 'in', 'm', 'cm']
        if from_unit not in accepted_values or to_unit not in accepted_values:
            raise ValueError('Not a correct unit value')

        return measurement * self.conversions[to_unit][from_unit]