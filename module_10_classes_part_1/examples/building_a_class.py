# building a class from scratch - the thinking process
# students can read class examples all day but freeze when they have to write one
# this walks through HOW to think about it, not just the final answer


# === STEP 1: WHAT ARE YOU MODELING? ===
# start with the real-world thing. what IS it? what does it HAVE? what does it DO?
#
# let's say: a playlist
#
# what does a playlist HAVE? (these become attributes)
#   - a name
#   - a list of songs
#
# what does a playlist DO? (these become methods)
#   - add a song
#   - remove a song
#   - show all songs
#   - count the songs


# === STEP 2: WRITE THE SKELETON ===
# class name (PascalCase), __init__ with the attributes, pass for methods
print("=== Step 2: Skeleton ===")


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []  # starts empty - each playlist gets its own list

    def add_song(self, song):
        pass

    def remove_song(self, song):
        pass

    def show_songs(self):
        pass

    def count(self):
        pass


# even this works - you can create objects and call methods, they just don't do anything yet
p = Playlist("Road Trip")
p.add_song("Bohemian Rhapsody")  # does nothing yet but doesn't crash
print(f"Created playlist: {p.name}")
print(f"Songs: {p.songs}")  # still empty
print()


# === STEP 3: FILL IN THE METHODS ONE AT A TIME ===
# don't try to write everything at once. get one method working, test it, move on.
print("=== Step 3: Finished Class ===")


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f"Added '{song}' to {self.name}")
        else:
            print(f"'{song}' is already in {self.name}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed '{song}' from {self.name}")
        else:
            print(f"'{song}' not found in {self.name}")

    def show_songs(self):
        if not self.songs:
            print(f"{self.name} is empty")
        else:
            print(f"\n{self.name}:")
            for i, song in enumerate(self.songs, 1):
                print(f"  {i}. {song}")

    def count(self):
        return len(self.songs)


# test it
rock = Playlist("Rock Classics")
rock.add_song("Bohemian Rhapsody")
rock.add_song("Stairway to Heaven")
rock.add_song("Hotel California")
rock.add_song("Bohemian Rhapsody")  # duplicate - should be caught
rock.show_songs()
print(f"Total: {rock.count()} songs")
print()

# the key insight: rock and chill are completely independent objects
chill = Playlist("Chill Vibes")
chill.add_song("Weightless")
chill.add_song("Sunset Lover")
chill.show_songs()
print(f"Total: {chill.count()} songs")
print()

rock.remove_song("Hotel California")
rock.remove_song("Yesterday")  # not in playlist
rock.show_songs()
print()


# === THE THINKING CHECKLIST ===
# when you need to build a class from scratch:
#
# 1. NAME IT — what real-world thing are you modeling? (PascalCase)
#
# 2. ATTRIBUTES — what data does each instance need?
#    → these go in __init__ with self.attribute = value
#    → ask: "if I create two of these, what's different between them?"
#
# 3. METHODS — what actions can this thing perform?
#    → always start with self as the first parameter
#    → ask: "what would I want to DO with this object?"
#
# 4. SKELETON FIRST — write the class with pass in every method
#    → make sure you can create objects without errors
#
# 5. ONE METHOD AT A TIME — fill in, test, repeat
#    → don't write 10 methods then try to debug them all at once
