from rest_framework.exceptions import ErrorDetail

def extract_error_detail(error):
    field_list = []
    for field, value in error.items():
        if type(value) is str or type(value) is ErrorDetail:
            error_message = value
        else:
            try:
                error_message = value[0]
            except IndexError:
                error_message = str(value)

        field_list.append({'field_name': field, 'error_message': error_message})

    return field_list
