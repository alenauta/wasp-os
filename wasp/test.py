
import wasp



class rawImage():

	def __init__(self, image, x, y, width):
		self.image = image
		self.x = x
		self.y = y
		self.w = width

	def draw(self):
		display = wasp.watch.display

		with open(self.image, "rb") as f:
			src = f.read()

		h = (len(src)//4)//self.w
		offset = self.w*4

		for l in range(h):
			# print("line {}".format(l))
			for i in range(0,self.w*4,4):
				o = i + (offset*l)
				r = src[o]
				g = src[o+1]
				b = src[o+2]
				a = src[o+3]

				if a > 0:
					ba = bytearray()
					# _x = x+((i//4)%w)
					# _y = y+((i//4)//w)
					_x = self.x+(i//4)
					_y = self.y+l
					ba.append(r)
					ba.append(g)
					ba.append(b)
					display.set_window(_x,_y,self.w,h)
					display.write_data(ba)
					# print("writing a pixel with data {}{}{} at x:{} y:{}".format(r,g,b,_x,_y))
				# else:
				# 	print("{} is transparent".format(i//4))



# display = wasp.watch.display
# draw = wasp.watch.drawable
# display = wasp.watch.display
# set_window(x, y, width, height)