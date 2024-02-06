def replace_placeholders_in_locator(locator: tuple[str, str], replacement: list or str) -> tuple[str, str]:
    if isinstance(replacement, list):
        for item in replacement:
            locator = (locator[0], locator[1].replace('{}', str(item)))
    else:
        locator = (locator[0], locator[1].replace('{}', str(replacement)))

    return locator
