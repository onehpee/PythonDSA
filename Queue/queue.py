from collections import deque

class Queue:
    
    def __init__(self):
        self.line = deque()
    
    def enqueue(self, val):
        self.line.appendleft(val)
        
    def dequeue(self):
        return self.line.pop()
    
    def is_empty(self):
        return len(self.line)==0
    
    def size(self):
        return len(self.line)
    

longLine = Queue()

longLine.enqueue(9)
longLine.enqueue(10)
longLine.enqueue(11)
longLine.enqueue(12)

longLine.size()
longLine.dequeue()
print(longLine.line)


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        


       
Playlist = []

Playlist.insert(0,Song("Drake", "HYFR"))
Playlist.insert(0,Song("Nicki Minaj", "Seeing Green"))
Playlist.insert(0,Song("50 Cent", "Candy Shop"))
Playlist.insert(0,Song("Rihanna", "Work"))

Playlist.pop()

for obj in Playlist:
    print(obj.title, obj.artist)