is_playing: bool = True

while is_playing:
    print("Jam duke luajtur...")
    answer = input("deshiron te luash perseri? (po/jo)")
    if (answer != "po"):
        is_playing = False
        exit()

