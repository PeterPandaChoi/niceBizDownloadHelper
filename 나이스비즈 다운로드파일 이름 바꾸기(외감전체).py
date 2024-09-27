import os
import shutil
import fnmatch

#현재 폴더의 경로
filePath = os.getcwd()
#현재 프로그램의 이름(사용자가 이름을 바꿨을 경우를 위한)
thisProgramName=os.path.basename(__file__)
#현재 폴더에 있는 파일들을 리스트로 저장
file_names = os.listdir(filePath)
#그 리스트에서 현재 프로그램을 뺌
file_names.remove(thisProgramName)

#'정리'라는 폴더가 없으면 만들고, 있다면 리스트에서 '정리'를 빼서 버그 제거
if not (os.path.isdir('.\정리')):
  os.makedirs('정리') 
else:
  file_names.remove('정리')
category=''


print("\n____________________파일을 아래와 같이 변경____________________\n")
for file in file_names:
  #1 파일의 이름을 출력해주고
  print(file)

  #2 해당하는 경우에 변경을 해주도록 카테고리를 설정
  if fnmatch.fnmatch(file,'*(0)*'):
    category='외감_재무상태_'
    print('변경->'+category+file+'\n')
    shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+"산출_재무상태_"+file.replace("[NICE BizLINE]","").replace("(산업합산 재무제표)",""))
  elif fnmatch.fnmatch(file,'*(1)*'):
    category='외감_손익계산_'
    print('변경->'+category+file+'\n')
    shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+"산출_손익계산_"+file.replace("[NICE BizLINE]","").replace("(산업합산 재무제표)",""))
  elif fnmatch.fnmatch(file,'*(2)*'):
    category='외감_이익잉여_'
    print('변경->'+category+file+'\n')
    shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+"산출_이익잉여_"+file.replace("[NICE BizLINE]","").replace("(산업합산 재무제표)",""))
  elif fnmatch.fnmatch(file,'*(3)*'):
    category='외감_현금흐름_'
    print('변경->'+category+file+'\n')
    shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+"산출_현금흐름_"+file.replace("[NICE BizLINE]","").replace("(산업합산 재무제표)",""))
  elif fnmatch.fnmatch(file,'*(4)*'):
    category='외감_제조원가_'
    print('변경->'+category+file+'\n')
    shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+"산출_제조원가_"+file.replace("[NICE BizLINE]","").replace("(산업합산 재무제표)",""))

  elif fnmatch.fnmatch(file,'*(5)*'):
    category='전체_재무상태_'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*(6)*'):
    category='전체_손익계산_'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*(7)*'):
    category='전체_이익잉여_'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*(8)*'):
    category='전체_현금흐름_'
    print('변경->'+category+file+'\n')
  elif fnmatch.fnmatch(file,'*(9)*'):
    category='전체_제조원가_'
    print('변경->'+category+file+'\n')
  else:
    category=''
    print(' ---> 변경되지않음')

  #3 마지막으로 정리 폴더에 파일을 카피해주면 끝!
  shutil.copyfile(filePath+'/'+file, filePath+'/정리/'+category+file.replace("[NICE BizLINE]","").replace("(산업합산 재무제표)",""))


print("\n____________________파일을 위 와 같 이 변경____________________\n")