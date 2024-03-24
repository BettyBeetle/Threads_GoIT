import concurrent.futures
import sys
import os
import shutil
import glob



def get_path():
    if len(sys.argv) > 2:
        print(f"Error: wrong path, give a right path of folder to sort")
        sys.exit()
    else:
        folder_path = sys.argv[1]
        if os.path.exists(os.path.dirname(folder_path)) and os.path.isdir(folder_path):
            return folder_path
        print("Sorting out..")
  

img_ext = ["*.jpg", "*.png", "*.jpeg", "*.svg", "*.tiff"]
txt_ext = ["*.pdf", "*.txt", "*.doc", "*.docx", "*.txt", "*.xlsx", "*.pptx", "*.odp", "*.odg","*.ods", "*.odt" ]
audio_ext  = ["*.mp3", "*.ogg", "*.wav", "*.amr"]
video_ext = ["*.avi", "*.mp4", "*.mov", "*.mkv"]
arch_ext = ["*.zip", "*.gz", "*.tar"]


def create_folders():
    folder_names = ["_images", "_documents", "_audio", "_video", "_archives"]
    for folder_name in folder_names:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Creating folder {folder_name}")


def move_files(ext_list, source, destination):
    for ext in ext_list:
        for file in glob.glob(os.path.join(source, ext)):
            try:
                shutil.move(file, destination)
                print(f"Moved: {file} to folder: {destination}")
            except Exception as e:
                print(f"Error moving {file}: {e}")

def sort_files(folder):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for ext, dest in zip([img_ext, txt_ext, audio_ext, video_ext, arch_ext], ["_images", "_documents", "_audio", "_video", "_archives"]):
            futures.append(executor.submit(move_files, ext, folder, os.path.join(folder, dest)))
        for future in concurrent.futures.as_completed(futures):
            future.result()

def main():
    folder_path = get_path()
    os.chdir(folder_path)
    create_folders()
    sort_files(folder_path)

if __name__ == '__main__':
    main()