import os
import re
import glob
import shutil
def main():
     pathz = []
     path1 = input("What is the first file path you want to use:\n")
     pathz.append(path1)
     path2 = input("What is the second file path you want to use:\n")
     pathz.append(path2)
     
     text = input("Do you want to remove square brackets? Y/N\n")
     if text == 'Y' or text == 'y':
          for path in pathz:
               files = os.listdir(path)
               pattern = r'\[[^\]]*\] '
               pattern2 = r' \[[^\]]*\]'
               pattern3 = r'\[[^\]]*\]'
               for name in files:
                    #print(name)
                    new_name = re.sub(pattern, r'', name)
                    new_name2 = re.sub(pattern2,r'',new_name)
                    new_name3 = re.sub(pattern3,r'',new_name2)
                    
                    #print(new_name)
                    os.rename(os.path.join(path,name), os.path.join(path,new_name))
                    os.rename(os.path.join(path,new_name),os.path.join(path,new_name2))
                    os.rename(os.path.join(path,new_name2),os.path.join(path,new_name3))
     elif text == 'N' or text =='n':
          pass
     #for i in range(26):
          #if i < 14
     condition2 = input("Do you want to move the files? Y/N\n")
     if condition2 == 'Y' or condition2 == 'y':
          if len(pathz) == 1:
               pass

          for path in pathz:
               files = os.listdir(path)
               for name in files:     
               
                    for i in range(25,-1,-1):
                         letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                         Cletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
               
                    
                         if name[0] == letters[i] or name[0] == Cletters[i]:
                         
                                   if i > 13:
                                        targetpath = pathz[1]
                                        if os.path.join(targetpath,name) == os.path.join(path, name):
                                             continue
                                        else:
                                             shutil.move(os.path.join(path, name),targetpath)
                              
                                   else:
                                        targetpath = pathz[0]
                                        if os.path.join(targetpath,name) == os.path.join(path,name):
                                             continue
                                        else:
                                             shutil.move(os.path.join(path, name),targetpath)
     if condition2 == 'n' or condition2 == 'N':
          pass
                   
if __name__ == '__main__':
     main()
     
