songs=[]
def add_song():
    title=input("enter title:")
    artist_name=input("enter artist name:")
    genres=set()
    n=int(input("enter how many geres you have?: "))
    for i in range(n):
        gen=input(f"Enter genre {i+1}: ")
        genres.add(gen)
    song={
        "title":title,
        "artist_name":artist_name,
        "genres":genres
    }
    songs.append(song)
    print("song successfully added")
def display_all_songs():
    if not songs:
        print("not songs found")
    else:
        print("songs list")
        for s in songs:
           print(f"Title:{s['title']},Artist_name:{s['artist_name']},Genres:{','.join(s['genres'])}")
def search_song_by_title():
    name=input(f"enter the title of song: ")
    found=False
    for s in songs:
        if name.lower()in s['title'].lower():
         print(f"found-->title: {s['title']} , artist_name: {['artist_name']} , genres:z{','.join(s['genres'])}") 
         found=True
         break
    if not found:
            print("X song not found") 
while True:
    print("1. add_song()")
    print("2. display_all_songs()")
    print("3. search_song_by_title()")
    print("4. exit")
    choice=int(input("chose an option:  "))
    if choice==1:
        add_song()
    elif choice==2:
        display_all_songs()
    elif choice==3:
        search_song_by_title()
    elif choice==4:
        print("exiting program")
    else:
        print("invalid choice try again")
      