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

def read_valid(lines):
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records

def average_by_city(records):
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        total[city] = total.get(city, 0.0) + temperature
        count[city] = count.get(city, 0) + 1

    return {
        city: round(total[city] / count[city], 1)
        for city in total
    }
