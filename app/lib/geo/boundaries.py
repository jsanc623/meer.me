def boundary(latitude, longitude, miles):
    if -90 >= latitude >= 90:
        raise ValueError('Latitude exceeds minmax')

    if -180 >= longitude >= 180:
        raise ValueError('Longitude exceeds minmax')

    if miles >= 1000:
        raise ValueError('Miles exceeds 1000')

    latitude_bound = 0.0144697 * miles
    longitude_bound = 0.0144812 * miles

    bounds = {
        'latitude': {
            'min': (latitude - latitude_bound),
            'max': (latitude + latitude_bound)
        },
        'longitude': {
            'min': (longitude - longitude_bound),
            'max': (longitude + longitude_bound)
        }
    }

    return bounds