song = 'do you hear the people sing? Singing the song of angry man'
#按照指定字符串分割 默认空格
#打印 ['do', 'you', 'hear', 'the', 'people', 'sing?', 'Singing', 'the', 'song', 'of', 'angry', 'man'] 
print(song.split())
#打印 ['do you hear the people ', 'ing? Singing the ', 'ong of angry man']
print(song.split('s'))

new_song = song.split()
#join函数将字符串列表按照指定字符串进行拼接
new_str='-'.join(new_song)
#打印 do-you-hear-the-people-sing?-Singing-the-song-of-angry-man
print(new_str)

#打印 ab
print('a'+'b')
#打印 aaaaa
print('a'*5)

new_song=song.split()
#自定义拼接字符串
result=''
for i in new_song:
    result += i
    result += ' '
#打印 do you hear the people sing? Singing the song of angry man
print(result)
