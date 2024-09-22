from video import Video
import re
from services import write_to_json, read_from_json

class Menu:
    def __init__(self) -> None:
        self.videos: list(Video) = read_from_json()
        # [
        #     Video("Prey Eh Kert", "sin sisamuth", "Rattanak", 110, "mp4"),
        #     Video("Pel Del Trov Yum", "sin sisamuth", "Rattanak", 110, "mp4"),
        #     Video("Luoch Sneh Luoch Tuk", "sin sisamuth", "Rattanak", 110, "mp4"),
        # ]


    def create_video(self):
        print("Please input info:")
        print("Video #%d" %(len(self.videos)+1))
        title = input("Title:")
        singer = input("Singer:")
        uploader = input("Uploader:")
        length = input("Length:")
        type = input("Type:")
    
        self.videos.append(Video(title, singer, uploader, length, type))
        write_to_json(self.videos)
        print("A video is added to the list\n")

    def video_lists(self):
        print("\n======================================================")
        print("| No  | Title               | Singer          | Uploader | Length   | Type    |")
        print("======================================================")
        for idx, video in enumerate(self.videos):
            print("| {:<3} | {:<20} | {:<15} | {:<8} | {:<8} | {:<7} |".format(
                idx + 1, video.title, video.singer, video.uploader, video.length, video.type
            ))
        print("======================================================\n")
        
    def search(self):
        while True:
            s = input("Input title:")
            foundedVideo: list(Video) = []
            for vid in self.videos:
                if re.search(s, vid.title.lower()) or re.search(s, vid.singer.lower()):
                    foundedVideo.append(vid)

            if len(foundedVideo) > 0:
                for idx, vid in enumerate(foundedVideo):
                    print("%d. %s by %s" %(idx, vid.title, vid.singer))
                break
            else:
                print("0 video found. Try again")
                continue
            

menu = Menu()

while True:
    print("============ Menu ================")
    print("1. Search")
    print("2. View all videos")
    print("3. Add a new video")
    print("4. Quit\n")

    option: int = int(input("Choose an option:"))

    match option:
        case 1:
            menu.search()
            continue
        case 2:
            menu.video_lists()
            continue
        case 3:
            menu.create_video()
            continue
        case 4:
            break
        case _:
            print("Incorrect Input please choose the right one!")
            continue