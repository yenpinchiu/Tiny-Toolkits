import os
import shutil

photo_dict = {}

for subdir, dirs, files in os.walk('./'):
    for file in files:
        if file not in photo_dict or os.path.getsize(subdir+"/"+file) not in photo_dict[file]:
            shutil.copy(subdir+"/"+file,"./photo/"+file)
            if file not in photo_dict:
                photo_dict.update({file:[]})
            photo_dict[file].append(os.path.getsize(subdir+"/"+file))
        
