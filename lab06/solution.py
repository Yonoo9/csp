def count_by_extension(paths):
    result = {}

    for path in paths:
        filename = path.split("/")[-1]
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        result[extension] = result.get(extension, 0) + 1

    return result


def deepest_path(paths):
    if not paths:
        return ""

    return min(paths, key=lambda path: (-path.count("/"), path))


def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    index = 0

    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1

    if index == 0:
        return f"{n_bytes} Б"

    return f"{size:.1f} {units[index]}"
