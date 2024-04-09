from datetime import datetime


def infer_data_type(value):
    if value.isdigit():
        return "integer"
    elif value.replace(".", "", 1).isdigit():
        return "float"
    elif is_valid_date(value):
        return "date"
    else:
        return "string"


def is_valid_date(value):
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass
    return False


def parse_and_validate_row(row, data_types):
    for field, value in row.items():
        if data_types[field] == "integer":
            row[field] = str(int(float(value)))
        elif data_types[field] == "float":
            row[field] = str(float(value))
        elif data_types[field] == "date":
            row[field] = parse_and_format_date(value)
    return row


def parse_and_format_date(value):
    date_formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(value, date_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            pass
    raise ValueError(f"Invalid date format: {value}")


def ensure_uniqueness(row, unique_values, data_type, fieldnames):
    for field in fieldnames:
        if field not in unique_values:
            unique_values[field] = set()
        if row[field] in unique_values[field]:
            if data_type == "timeseries" and field == fieldnames[0]:
                raise ValueError(
                    "Duplicate timestamp found in the generated time-series data."
                )
            else:
                row[field] += "_" + str(len(unique_values[field]) + 1)
        unique_values[field].add(row[field])
    return row


def sort_timeseries_data(data, fieldnames):
    timestamp_field = fieldnames[0]
    data.sort(key=lambda x: x[timestamp_field])
    return data
