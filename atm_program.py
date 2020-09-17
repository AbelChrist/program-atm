# 1. Periksa Pin
# 2. Ganti Pin
# 3. Cek Saldo
# 4. Debet / Withdraw
# 5. Simpan / Deposit
# 6. Keluar
# 7. Cetak ringkasan transaksi

import random
import datetime
from atm_card import ATMCard1, ATMCard2

while True:
	print("1. Mandiri\n2. BCA\n")
	kartu = int(input("Pilih Kartu: "))
	if kartu == 1:
		atm = ATMCard1(id)
		break
	elif kartu ==2:
		atm = ATMCard2(id)
		break
while True:
	id = int(input("Masukkan Pin Anda: "))
	trial = 0

	while (id != int(atm.checkPin()) and trial < 3):
		id = int(input("Pin anda salah. Silahkan Masukkan lagi: "))	
		trial += 1

		if trial == 3:
			print("Error. Silahkan ambil kartu dan coba lagi!")
			exit()

	while True:
		print("Selamat datang di ATM Progate")
		print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")
		selectmenu = int(input("\nSilahkan pilih menu: "))
	
		if selectmenu == 1:
			print("\nSaldo anda sekarang: Rp. "+str(atm.checkBalance()) + "\n")
		
		elif selectmenu == 2:
			nominal = float(input("Masukkan nominal saldo: "))
			verify_withdraw = input("Anda akan melakukan debit dengan nominal berikut? y/n \nRp. "+ str(nominal)+ "\nKonfirmasi: ")

			if verify_withdraw == "y":
				print("Saldo awal anda adalah: Rp. "+str(atm.checkBalance())+ "\n")
			else:
				break
			if nominal < atm.checkBalance():
				atm.withdrawBalance(nominal)
				print("Transaksi debit berhasil!")
				print("Saldo sisa sekarang: Rp. "+ str(atm.checkBalance())+ "\n")
			else:
				print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
				print("Silahkan lakukan penambahan nominal saldo\n")
		
		elif selectmenu == 3:
			nominal = float(input("Masukkan nominal saldo: "))
			verify_deposit = input("Anda akan melakukan penyimpanan dengan nominal berikut? y/n \nRp."+ str(nominal)+ "\nKonfirmasi: ")

			if verify_deposit == "y":
				atm.depositBalance(nominal)
				print("Tansaksi deposit berhasil!\n")
				print("Saldo anda sekarang adalah Rp. "+ str(atm.checkBalance())+ "\n")
			else:
				break
		
		elif selectmenu == 4:
			verify_pin = int(input("Masukkan pin lama anda: "))
			trial = 0
			while verify_pin != int(atm.checkPin()):
				verify_pin = int(input("Pin anda salah, silahkan masukkan pin lama anda: "))
				trial += 1
				if trial == 3:
					print("Error. Silahkan ambil kartu dan coba lagi!")
					exit()
			while True:
				updated_pin = int(input("Silahkan masukkan pin baru: "))
			
				if updated_pin == int(atm.checkPin()):
					print("Pin baru tidak bisa sama dengan pin lama!")
					continue

				verify_newpin = int(input("Konfirmasi ulang pin baru anda: "))
				if updated_pin != verify_newpin:
					print("Pin konfirmasi tidak cocok!")
					continue

				break

			atm.changePin(updated_pin)
			print("Pin berhasil diganti!")
			break
		
		elif selectmenu == 5:
			print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
			print("No. record: ", random.randint(100000, 1000000))
			dateNow = datetime.datetime.now()
			print("Tanggal", dateNow.strftime("%d/%m/%Y %X"))
			print("Saldo akhir: Rp.", atm.checkBalance())
			print("Terima kasih telah menggunakan ATM Progate!")
			exit()
		
		else:
			print("Error. Maaf, menu tidak tersedia")
















