# 4. Validate an IP Address format.

# Problem: Check if a string is a valid IPv4 address (four numbers separated by dots, 0-255).


def is_valid_ip(ip_str):
    parts = ip_str.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
    return True

print(is_valid_ip("192.168.1.1")) # Output: True