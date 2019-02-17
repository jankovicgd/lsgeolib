def check_directions(columns, points, measurements):
    if 'directions' not in measurements.keys():
        return columns

    columns_not_unique = []
    for point in points:
        if points[point]['state'] == 'approximate':
            for direction in measurements['directions']:
                if measurements['directions'][direction]['from'] == point:
                    columns_not_unique.append(point)

    columns_to_append = list(set(columns_not_unique))
    for dz in columns_to_append:
        columns.append(dz + '.dz')
    return columns
