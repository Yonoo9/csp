def parse_record(line):
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Запись должна содержать три поля")

    city = parts[0].strip()
    temp = parts[1].strip()
    date = parts[2].strip()

    if not city:
        raise ValueError("Город не может быть пустым")

    if not date:
        raise ValueError("Дата не может быть пустой")

    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }
