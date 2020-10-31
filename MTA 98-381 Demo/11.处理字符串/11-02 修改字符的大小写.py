song = 'do you hear the people sing? Singing the song of angry man'

#以下函数不会改变字符串本身
#首字母大写 打印 Do you hear the people sing? singing the song of angry man
print(song.capitalize())
#所有单词首字母大写 打印 Do You Hear The People Sing? Singing The Song Of Angry Man
print(song.title())
#全部转换为大写 打印 DO YOU HEAR THE PEOPLE SING? SINGING THE SONG OF ANGRY MAN
print(song.upper())
#全部转换为小写 打印 do you hear the people sing? singing the song of angry man
print(song.lower())

newsong = song.title()
#大小写互换
result = ''
for i in newsong:
    if i.upper()==i:
        i=i.lower()
    else:
        i=i.upper()
    result+=i
#打印 dO yOU hEAR tHE pEOPLE sING? sINGING tHE sONG oF aNGRY mAN
print(result)