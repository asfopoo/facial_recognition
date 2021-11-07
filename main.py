import os
import shutil
import face_recognition


def compare(_folder):
    clean_face_place_path = "/Users/edwardnardo/hopkinsIntroPython/faceRecog/clean_faces"
    folder = _folder
    match = 0
    no_match = 0
    total = 0
    bad_attempt = 0

    for dir_name in os.listdir(f'{clean_face_place_path}/{folder}'):
        files = []
        known_image = ''
        known_encoding = ''
        for filename in os.listdir(f'{clean_face_place_path}/{folder}/{dir_name}'):
            files.append(filename)
        # get OOF image... frontal image
        # todo there may be more than one 00f
        for filename in files:
            if '00F' in filename:
                known_image = face_recognition.load_image_file(
                    f'{clean_face_place_path}/{folder}/{dir_name}/{filename}')
        for filename in files:
            unknown_image = face_recognition.load_image_file(f'{clean_face_place_path}/{folder}/{dir_name}/{filename}')
            try:
                known_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                results = face_recognition.compare_faces([known_encoding], unknown_encoding)
                if results[0]:
                    match += 1
                else:
                    no_match += 1
                    print(filename)
                total += 1
            except (IndexError, TypeError) as e:
                total += 1
                bad_attempt += 1
            # print(f'total = {total}')

    print(f'match = {match}')
    print(f'no-match = {no_match}')
    print(f'total = {total}')
    print(f'bad attempts = {bad_attempt}')


def preprocess():
    # sub dir to search
    folder = "multiracial"
    dirty_face_place_path = "/Users/edwardnardo/hopkinsIntroPython/faceRecog/face place"
    clean_face_place_path = "/Users/edwardnardo/hopkinsIntroPython/faceRecog/clean_faces"
    for filename in os.listdir(f'{dirty_face_place_path}/{folder}'):
        # grab first 6 chars
        first_chars = filename[0:6]
        try:
            os.mkdir(f'{clean_face_place_path}/{folder}/{first_chars}')
        except OSError:
            print("Creation of the directory failed")
        # copy file over
        shutil.copy(f'{dirty_face_place_path}/{folder}/{filename}', f'{clean_face_place_path}/{folder}/{first_chars}')


if __name__ == "__main__":
    # preprocess the dataset by seperating each indidvidual into their
    # own directory for better efficiency
    # preprocess()

    # folders to facially recognize
    # note: caucasian takes 3 times longer than the rest
    # I suggest doing them seperate
    folders = ["caucasian"]
    # folders = ["african-american", "asian", "hispanic", "multiracial"]
    for folder in folders:
        compare(folder)
