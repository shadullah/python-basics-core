import sqlite3

con = sqlite3.connect('utube_videos.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id integer PRIMARY KEY,
        name text not null,
        time text not null
    )
''')

def list_all_videos():
    cursor.execute("select * from videos")
    print("*" * 50)
    for row in cursor.fetchall():
        print(row)
        # print(f"{index}. {video['name']} , Duration: {video['time']}")
    print("*" * 50)

def add_video():
    name= input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute("insert into videos(name, time) values (?, ?)", (name, time))
    con.commit()

def update_video():
    list_all_videos()
    index = int(input("Enter the number of the video to update: "))
    name = input("Enter the new Name of the video: ")
    time = input("Enter the new time of the video: ")
    cursor.execute("update videos SET name = ?, time =? where id = ?", (name, time,index))
    con.commit()


def delete_video():
    list_all_videos()
    index = int(input("Enter the number of the video to Delete: "))
    cursor.execute("delete from videos where id = ?", (index,))
    con.commit()

def main():
    while True:
        print("\n Youtube Manager || choose an option")
        print("1. List all youtube videos")
        print("2. add a youtube video")
        print("3. update a youtube video")
        print("4. delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice") 
    con.close()

if __name__ == "__main__":
    main()