import pymongo 
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://hexaalif2020:hexaalif2020@laz-pharma.wtlmz.mongodb.net/")

db = client['ytmanager']

video_collection = db["ytCollection"]
print(video_collection)

def list_all_videos():
    for video in video_collection.find({}):
        print(f"Id: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video():
    name= input("Enter video name: ")
    time = input("Enter video time: ")
    video_collection.insert_one({"name":name, "time":time})

def update_video():
    index = (input("Enter the number of the video to update: "))
    name = input("Enter the new Name of the video: ")
    time = input("Enter the new time of the video: ")
    video_collection.update_one(
        {'_id': ObjectId(index)},
        {'$set': {"name":name, "time":time}}
    )

def delete_video():
    index = (input("Enter the number of the video to Delete: "))
    video_collection.delete_one({"_id": ObjectId(index)})


def main():
    while True:
        print("\n Youtube Manager || choose an option")
        print("1. List all youtube videos")
        print("2. add a youtube video")
        print("3. update a youtube video")
        print("4. delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

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

if __name__ == "__main__":
    main()