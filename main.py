from daftarkota import daftarkota
from greedy import Greedy
def main():
	#List Kota
	kota = set(['Cilegon', 'Tangerang', 'Jakarta', 'Bogor',
		'Cikampek', 'Bekasi', 'Bandung', 'Cirebon', 'Cimahi', 'Cianjur', 'Garut', 'Sumedang', 'Subang', 'Tasikmalaya',	
		'Purwokerto', 'Magelang', 'Semarang', 'Jogja', 'Surabaya',
		'Malang'])

	#adjacency list city in Java
	jarak = {		
        'Cilegon' : {'Tanggerang' : 84},
		'Tanggerang' : {'Jakarta' : 35, 'Cilegon' : 84},
		'Jakarta' : {'Bogor' : 54, 'Cikampek' : 76, 'Bekasi' : 50, 'Tanggerang' : 35},
		'Bekasi' : {'Cikampek' : 41, 'Jakarta' : 50},
		'Cikampek' : {'Bandung' : 80, 'Cirebon' : 146, 'Jakarta' : 76, 'Bekasi' : 41},
		'Bogor' : {'Bandung' : 182, 'Jakarta' : 54},
		'Bandung' : {'Tasikmalaya' : 124, 'Cimahi' : 14, 'Cianjur' : 67, 'Garut' : 71, 'Sumedang' : 76, 'Subang': 54, 'Cikampek' : 80, 'Bogor' : 182},
		'Tasikmalaya' : {'Purwokerto' : 144, 'Bandung' : 124, 'Garut' : 53},
		'Cimahi' : {'Bandung' : 14},
		'Cianjur' : {'Bandung' : 67},
		'Garut' : {'Bandung' : 71, 'Tasikmalaya' : 53},
		'Sumedang' : {'Bandung' : 76},
		'Subang' : {'Bandung' : 54},
		'Purwokerto' : {'Magelang' : 145, 'Tasikmalaya' : 144},
		'Magelang' : {'Semarang' : 72, 'Jogja' : 53, 'Surabaya' : 339, 'Purwokerto' : 145},
		'Cirebon' : {'Tegal' : 88, 'Cikampek' : 146},
		'Tegal' : {'Semarang' : 160, 'Cirebon' : 88},
		'Semarang' : {'Jogja' : 129, 'Surabaya' : 348, 'Magelang' : 72, 'Tegal' : 160},
		'Jogja' : {'Surabaya' : 324, 'Magelang' : 53, 'Semarang' : 129},
		'Surabaya' : {'Malang' : 94, 'Magelang' : 339, 'Semarang' : 348, 'Jogja' : 324},		
		'Malang' : {'Surabaya' : 94}
	}

	finish = ' '
	daftarkota(kota)
	start = input('Kota Anda Sekarang : ').strip()
	start = start.lower()
	start = ''.join(start[0].upper() + start[1:])
	if start not in kota:
		print('\n Kota Yang Anda Masukkan Salah')
		
    
	finish = input('Kota Tujuan Anda : ')
	path = Greedy(jarak, start, finish)
	print('Kota Asal = ',start)
	if (path):
		print('Urutan Kota Berdasar Algoritma Greedy : ', end='')
		for i in path:
			print(i, end='>')

	else:
		print('Tidak Ditemukan Jalan')
	

if __name__ == '__main__':
	main()
