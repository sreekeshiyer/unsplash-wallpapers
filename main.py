from save_wallpapers import save_wallpapers
import os
directory = "C:\\Users\\zenon\\Pictures\\walls\\"


def change_dir_style(dir):

    new_dir = str(dir).replace("\\", "/")
    new_dir = new_dir.replace(":", "")
    return ('/'+new_dir)


print('Choose your option\n1.Store wallpapers in a folder (first time)\n2.Refresh my Collection(Deletes all contents inside the specified folder and adds wallpapers there)')
choice = int(input())
print('''
    New Wallpapers will be downloaded in - % s
    Do you wish to proceed? (y/n)
    ''' % directory)

choose_to_proceed = input()

if choose_to_proceed == 'y':
    if choice == 1:
        save_wallpapers(directory)
    elif choice == 2:
        cmd = "rm -rf "+change_dir_style(directory)+"*"
        os.system(cmd)
        save_wallpapers(directory)
else:
    print('Exiting')
