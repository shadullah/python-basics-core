import json 

fileName = 'youtube.txt'

def load_data():
    try:
        with open(fileName, 'r') as file:
            # return json.load(file)
            test =  json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    # finally:
    #     pass

def save_data_helper(videos):
    with open(fileName, 'w')as file:
         json.dump(videos,file)

def list_all_videos(videos):
    print("*" * 50)
    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} , Duration: {video['time']}")
    print("*" * 50)

def add_video(videos):
    name= input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to update: "))
    if 1<=index <= len(videos):
        name = input("Enter the new Name of the video: ")
        time = input("Enter the new time of the video: ")
        videos[index-1]={'name': name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to Delete: "))

    if 1<=index <= len(videos):
        del videos[index-1]
        print(videos)
        save_data_helper(videos)
    else:
        print("Invalid index selected")
    



def main():
    videos = load_data()
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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__ == '__main__':
    main()