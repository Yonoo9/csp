def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    time = parts[0]
    level = parts[1]
    message = parts[2]

    if level not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
        raise ValueError("Неизвестный уровень")

    if not time or not message.strip():
        raise ValueError("Нет времени или сообщения")

    return {
        "time": time,
        "level": level,
        "message": message
    }

def count_levels(lines: list[str]) -> dict:
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"

        if level not in counts:
            counts[level] = 0

        counts[level] += 1

    return counts
