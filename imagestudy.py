from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# im = Image.open("pp.jpg").convert('L')

# im = im.resize((168,105), Image.ANTIALIAS)
# im = np.array(im)

# im = Image.fromarray(im, mode='L')
# im = im.rotate(30)
# im.show()

# s = np.random.uniform(0,255,30000).reshape(100,100,3).astype(np.uint8)
# img = Image.fromarray(s).convert('RGB')
# img.show()

# im = Image.open('pp.jpg').convert('RGB')
# r,g,b = im.split()
# im = Image.merge('RGB', (b,g,r))
# im.show()

# im = Image.open('pp.jpg')
# im = im.transpose(Image.FLIP_LEFT_RIGHT)
# im = im.transpose(Image.FLIP_TOP_BOTTOM)
# im.show()

# im = Image.open('pp.jpg')
# out = im.point(lambda i: i*2)
# out.show()

# im = Image.open('pp.jpg')
# source = im.split()
# R,G,B = 0,1,2
# mask = source[R].point(lambda i: i<100 and 255)
# out = source[G].point(lambda i:i*0.7)
# source[G].paste(out, None, mask)
# im = Image.merge(im.mode, source)
# im.show()

# im = Image.open('water_GIF3.gif')
# im.seek(8)
# im.show()

# x = np.arange(1,11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x,y,"ob")
# plt.show()

# x = np.arange(0, 10, 0.1)
# print x

# x,y = [5,8,10],[12,16,6]
# plt.bar(x,y,align='center')
# plt.show()

# x = np.arange(0,  3  * np.pi,  0.1) 
# y_sin = np.sin(x) 
# y_cos = np.cos(x)  
# plt.subplot(2,  1,  1)  
# plt.plot(x, y_sin) 
# plt.title('Sine')  
# plt.subplot(2,  1,  2) 
# plt.plot(x, y_cos) 
# plt.title('Cosine')  
# plt.show()

# img = plt.imread('pp.jpg')
# plt.imshow(img)
# x = np.arange(1,10000)
# plt.plot(x, x, label='linear')
# plt.show()

# im = Image.open("pps.jpg")
# im = np.array(im)
# for i in range(104):
#     for j in range(167):
#         s = im[i+1][j+1] - im[i][j]
#         s2 = s.dot(s)
#         im[i][j] = [0,0,0] if s2==0 else im[i][j]
# im = Image.fromarray(im)
# im.show()

# x = np.arange(3)
# y = x.dot(x)
# print y

# im = Image.open("pps.jpg")
# im = np.array(im)
# for i in range(104):
#     for j in range(167):
#         s = im[i][j]
#         im[i][j] = [0,0,0] if s[0] == 255 and s[1] == 255 and s[2] == 255 else im[i][j]
# im = Image.fromarray(im)
# im.show()

# im = Image.open("tts.jpg")
# im = np.array(im)
# for i in range(104):
#     for j in range(167):
#         s = im[i][j]
#         im[i][j] = [255,0,0] if s[0] == 255 and s[1] == 255 and s[2] == 255 else im[i][j]
# im = Image.fromarray(im)
# im = im.point(lambda i: i==255 and 200)
# im.show()

# im = Image.open("tt.jpg")
# im = im.resize((168,105), Image.ANTIALIAS)
# im.save("tts.jpg")

# im = Image.open("tt.jpg")
# size = im.size
# im = np.array(im, dtype='uint32')
# out = np.zeros((size[1],size[0],3), dtype='uint8')
# nextpoint = np.array([0,1], dtype='uint32')
# backcolor = np.array([255,255,255], dtype='uint32')
# selectcolor = np.array([200,50,50], dtype='uint32')
# selectcolor2 = np.array([200,50,50], dtype='uint8')

# box_lefttop = np.array([0,0], dtype='uint8')
# box_rightbottom = np.array([0,0], dtype='uint8')
# box_lefttop_bool = False
# box_rightbottom_bool = False

# def checksamecolor(i,j,color):
#     item = im[i][j]
#     diff = item - color
#     s = int(diff.dot(diff) ** 0.5 / 3)
#     return True if s <= 25 else False

# def checkaround(i,j):
#     if checksamecolor(i,j,selectcolor):
#         out[i][j] = selectcolor2
#         im[i][j] = backcolor

#         if checksamecolor(i+1,j,selectcolor) and nextpoint[0] != (i+1):
#             return np.array([i+1,j], dtype='uint32')
#     return np.array([0,1], dtype='uint32')


# for i in range(0,size[1]-1):
#     for j in range(nextpoint[1],size[0]):
#         nextpoint = checkaround(i,j)

# out = Image.fromarray(out)
# out.show()

# backcolor = np.array([255,255,255], dtype='uint32')
# selectcolor = np.array([200,50,50], dtype='uint32')
# s = int(np.dot(backcolor, selectcolor)** 0.5 / 3)
# print s



im = Image.open("tt1.jpg")
size = im.size
im = np.array(im, dtype='uint32')
out = np.zeros((size[1],size[0],3), dtype='uint8')
nextpoint = np.array([0,1], dtype='uint32')
backcolor = np.array([255,255,255], dtype='uint32')
selectcolor = np.array([200,50,50], dtype='uint32')
selectcolor2 = np.array([200,50,50], dtype='uint8')

box_lefttop = np.array([0,0], dtype='uint32')
box_rightbottom = np.array([0,0], dtype='uint32')
box_lefttop_bool = False
box_rightbottom_bool = False

def checksamecolor(i,j,color):
    item = im[i][j]
    diff = item - color
    s = int(diff.dot(diff) ** 0.5 / 3)
    return True if s <= 25 else False

def checkaround(i,j):
    if checksamecolor(i,j,selectcolor):
        return True
    return False

for i in range(0,size[1]):
    if not box_lefttop_bool:
        for j in range(0,size[0]):
            if checkaround(i,j):
                box_lefttop_bool = True
                box_lefttop = np.array([i,j], dtype='uint32')
                break

iterrow = 2
itercol = 2
while not box_rightbottom_bool:
    iterrowold = iterrow
    itercolold = itercol
    for ii in range(itercol):
        if checkaround(box_lefttop[0] + iterrow - 1, box_lefttop[1] + ii):
            iterrow = iterrow + 1
            break

    for ii in range(iterrow):
        if checkaround(box_lefttop[0] + ii, box_lefttop[1] + itercol - 1):
            itercol = itercol + 1
            break
    if iterrowold == iterrow and itercolold == itercol:
        box_rightbottom_bool = True
        box_rightbottom = np.array([box_lefttop[0] + iterrow - 1, box_lefttop[1] + itercol - 1], dtype='uint32')

for i in range(box_lefttop[0],box_rightbottom[0]):
    for j in range(box_lefttop[1],box_rightbottom[1]):
        if checkaround(i,j):
            out[i][j] = selectcolor2

out = Image.fromarray(out)
out.show()