song = 'Do you hear the people sing? Singing the song of angry man'

#查找子字符串第一次出现的索引 打印 23
print(song.find('sing'))
#没有找到 打印 -1
print(song.find('SIng'))
#打印 12 如果没找到则报异常
print(song.index('the'))
#子字符串的个数 打印 2
print(song.count('the'))

#替换空格为'_'
result = song.replace(' ','_')
#打印 Do_you_hear_the_people_sing?_Singing_the_song_of_angry_man
print(result)

#替换前5个空格为'_'
result = song.replace(' ','_',5)
#打印 Do_you_hear_the_people_sing? Singing the song of angry man
print(result)