
def polyInput(x):
	end = False
	while(end == False):
		degree = int(input("Masukkan suku: "))
		if(degree == -999):
			end = True
			print("Input end")
		elif(degree < 0 and degree != -999):
			print("Suku tidak ada")
		elif(degree > 99):
			print("Suku tidak ada")
		else:
			coef = int(input("Masukkan koefisien: "))
			#arrayInput(p2, degree, coef)
			x[degree] = coef
	
def polyPrint(x):
	first = True
	for i in range (99,-1,-1):
		if(x[i] != 0):
			if(first == True):
				print(str(x[i])+'x^'+str(i),end='')
				first = False			
			else:	
				if(i != 0):
					if(x[i] > 0):
						print('+'+ str(x[i])+'x^'+str(i),end='')
					else :
						print(str(x[i])+'x^'+str(i),end='')
				else:
					if(x[i] > 0):
						print('+'+ str(x[i]),end='')
					else :		
						print(str(x[i]),end='')
	print( )

def polyOperation(w,x,y,z):
	if (z == '+'):
		for i in range(100):
			y[i] = w[i] + x[i]
	elif (z == '-'):
		for i in range(100):
			y[i] = w[i] - x[i]
			
def polyDerivative(x,y):
	for i in range(1,100):
		y[i-1] = x[i]*i
	
	
p1 = [0 for x in range(100)]
p2 = [0 for x in range(100)]

print("Masukkan data untuk Polinom 1:")
polyInput(p1)	
print("Masukkan data Untuk Polinom 2:")
polyInput(p2)
#UI Menu

end = False
while(end == False):
	print("""Daftar Command:
0.Mengakihiri Program
1.Print Polinom 1 dan Polinom 2
2.Menjumlahkan Polinom 1 dan Polinom 2
3.Mengurangi Polinom 1 dan Polinom 2
4. Membuat Turunan dari Polinom 1 dan Polinom 2""")
	command = int(input("Pilih Command yang ingin dikerjakan:"))
	print()
	if(command == 0):
		end = True
		print("Program berakhir")
	elif(command == 1):
		print("Mencetak nilai polinom 1 dan 2")
		print("Polinom 1:")
		polyPrint(p1)
		print("Polinom 2:")
		polyPrint(p2)
	elif(command == 2):
		p3 = [0 for x in range(100)]
		print("Menjumlahkan polinom 1 dan 2")
		polyOperation(p1,p2,p3,'+')
		print("Hasil : ")
		polyPrint(p3)
	elif(command == 3):
		p3 = [0 for x in range(100)]
		print("Mengurangkan polinom 1 dan 2")
		polyOperation(p1,p2,p3,'-')
		print("Hasil : ")
		polyPrint(p3)
	elif(command == 4):
		pa = [0 for x in range(100)]
		pb = [0 for x in range(100)]
		print("Menurunkan polinom 1 dan 2")
		polyDerivative(p1, pa)
		print("Turunan Polinom 1: ")
		polyPrint(pa)
		polyDerivative(p2, pb)
		print("Turunan Polinom 2: ")
		polyPrint(pb)


