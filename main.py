"""
🔍 MYSTERY DETECTIVE BOT 🔍
Sebuah game investigasi interaktif
Pecahkan misteri dengan mengumpulkan bukti dan mewawancarai tersangka
"""

print("=" * 70)
print("🔍 SELAMAT DATANG DI MYSTERY DETECTIVE BOT 🔍".center(70))
print("=" * 70)
print()

# ===== AWAL CERITA =====
print()
# ===== INISIALISASI TRACKING =====
bukti_diperiksa = []
tersangka_diwawancara = []

def display_menu():
    """Menampilkan menu pilihan investigasi"""
    print()
    print("=" * 75)
    print("🔎 APA YANG INGIN ANDA LAKUKAN SELANJUTNYA?".center(75))
    print("=" * 75)
    print()
    print("1. 🔍 Periksa BUKTI FISIK")
    print("2. 🎤 Wawancara TERSANGKA")
    print("3. 🎯 Tentukan PELAKU (jika sudah ada cukup bukti)")
    print()
    
    # Tampilkan progress
    print(f"Progress Investigasi:")
    print(f"  📋 Bukti yang diperiksa: {len(bukti_diperiksa)}/4")
    print(f"  👥 Tersangka yang diwawancara: {len(tersangka_diwawancara)}/3")
    print()

# ===== AWAL CERITA =====
print("=" * 75)
print("🔍 MYSTERY DETECTIVE BOT - KASUS PEMBERIAN OBAT BERLEBIH 🔍".center(75))
print("=" * 75)
print()
print("⏰ Tanggal: Selasa, 15 Januari 2024, pukul 21:30")
print("📍 Lokasi: Rumah Sakit Pribadi Kelas VIP, Wing Khusus")
print()
print("Seorang pasien bernama JAKARTA HUTOMO (64 tahun, pengusaha kaya) ditemukan")
print("dalam kondisi TIDAK SADARKAN DIRI setelah diberikan obat penenang berlebihan.")
print()
print("Korban masuk rumah sakit untuk operasi jantung yang dijadwalkan.")
print("Sebelum operasi, dia diberikan pre-medication oleh perawat.")
print("TAPI DOSISNYA JAUH LEBIH BESAR DARI YANG SEHARUSNYA!")
print("🕵️ Anda mewawancarai IKO...")
print("🚨 KASUS: Pemberian Obat Secara Tidak Sengaja atau SABOTASE MEDIS?")
print()
print("Korban dalam kondisi kritis. Dokter menyelamatkan nyawanya.")
print("Sekarang, Anda ditugaskan MENEMUKAN SIAPA yang mengatur dosis mematikan itu.")
print()
print("=" * 75)

print("👤 LATAR BELAKANG KORBAN:")
print("-" * 75)
print()
print("💡 Bukti: Informasi tentang hutang Tuan Hartono yang tersembunyi")
print("Jakarta Hutomo: Pengusaha sukses, pemilik beberapa perusahaan properti.")
print("Status Keluarga: Cerai dari istri pertama, sekarang menikah lagi.")
print()
print("Ia memiliki hutang bisnis BESAR akibat proyek properti yang gagal.")
print("Total hutang: Rp500 juta kepada investor (dengan bunga tinggi).")
print("Kesehatan: Penyakit jantung kronis, memerlukan operasi segera.")
print()
print("📌 CATATAN PENTING: Keluarganya menunggu operasi ini dengan antusias.")
print("    (Mungkin karena penghidupan tergantung pada hartanya)")
print()

print("=" * 75)
print()

print("👥 PROFIL 3 TERSANGKA UTAMA:")
print("-" * 75)
print()

print("1️⃣ GUNAWAN (30 tahun) - Asisten Pribadi Jakarta")
print("   • Bekerja 5 tahun dengan loyalitas tinggi")
print("   • Mengantar Jakarta ke rumah sakit pagi hari")
print("   • Terakhir dilihat membawa tas medis Jakarta ke ruang persiapan operasi")
print("   • Dilihat berbicara dengan perawat sebelum pemberian obat")
print("   • 💰 Gaji: Rp5 juta/bulan (upah standar)")
print()
print("   Alibi: 'Saya membantu Jakarta sampai masuk ke ruang operasi.'")
print("         'Setelah itu saya menunggu di ruang keluarga.'")
print()

print("2️⃣ MIRA (28 tahun) - Istri Kedua Jakarta")
print("   • Menikah dengan Jakarta 2 tahun lalu (usia 26)")
print("   • Hubungan terkenal penuh pertengkaran tentang uang")
print("   • Tidak bekerja, sepenuhnya tergantung pada Jakarta")
print("   • Sering mengeluh tentang hutang Jakarta")
print("   • Nampak tenang saat Jakarta dibawa ke ICU")
print()
print("   Alibi: 'Saya di area istirahat untuk keluarga saat operasi dimulai.'")
print("         'Saya berdoa untuk kesehatan Jakarta.'")
print()

print("3️⃣ RIZKI (35 tahun) - Anak Kandung Jakarta (dari Istri Pertama)")
print("   • Bekerja sebagai dokter di rumah sakit yang sama")
print("   • Hubungan dengan ayah memburuk sejak ayah menikah Mira")
print("   • Ayah mengurangi pemberian uang mingguan untuk Rizki")
print("   • Rizki punya akses penuh ke sistem obat-obatan rumah sakit")
print("   • Diketahui menghadiri rapat briefing pre-operasi")
print()
print("   Alibi: 'Saya ada di ruang operasi sebagai konsultan. Saya pantau prosesnya.'")
print("         'Saya tidak pernah tinggalkan ruang operasi.'")
print()

print("=" * 75)
print("💡 Bukti PENTING: Serat kain biru ditemukan!")
    
# ===== LOOP INVESTIGASI UTAMA =====
while True:
    display_menu()
    
    pilihan = input("Masukkan pilihan (1/2/3): ").strip()
    
    if pilihan == "1":
        # ===== CEK BUKTI =====
        daftar_bukti = [
            "Sepatu dengan lumpur basah (ukuran 42)",
            "Surat hutang piutang Rp500.000.000",
            "Botol obat penenang kosong bertanggal hari kejadian",
            "Catatan rencana transfer aset ke luar negeri"
        ]
        
        print()
        print("-" * 75)
        print("📋 BUKTI YANG TERSEDIA:")
        print("-" * 75)
        for i, bukti in enumerate(daftar_bukti, 1):
            status = "✅ SUDAH DIPERIKSA" if bukti in bukti_diperiksa else "⭕ BELUM DIPERIKSA"
            print(f"{i}. {bukti} [{status}]")
        print()
        
        pilih_bukti = input("Pilih bukti mana yang ingin diperiksa (1-4): ").strip()
        
        if pilih_bukti not in ["1", "2", "3", "4"]:
            print("⚠️ Pilihan tidak valid!")
            continue
        
        bukti_terpilih = daftar_bukti[int(pilih_bukti) - 1]
        
        if bukti_terpilih in bukti_diperiksa:
            print(f"\n✅ Bukti ini sudah Anda periksa sebelumnya.")
            print(f"📝 Ringkasan temuan tetap sama seperti sebelumnya.\n")
            continue
        
        print()
        print("-" * 75)
        print(f"🔎 PEMERIKSAAN BUKTI: {bukti_terpilih.upper()}")
        print("-" * 75)
        print()
        
        # Detail bukti
        if pilih_bukti == "1":
            print("📌 SEPATU DENGAN LUMPUR BASAH (Ukuran 42)")
            print()
            print("Tim forensik menemukan sepatu yang terselip di sudut tempat")
            print("penyimpanan obat-obatan darurat dekat ruang pre-operasi.")
            print()
            print("Temuan:")
            print("✓ Ukuran sepatu: 42 (ukuran standar pria)")
            print("✓ Lumpur segar tertanggal hari kejadian (malam hari)")
            print("✓ Merek: Brand internasional umum (dijual bebas)")
            print()
            print("Analisis:")
            print("• Gunawan: Ukuran sepatu 42 ✓ (COCOK)")
            print("• Mira: Wanita - tidak mungkin pakai ukuran 42")
            print("• Rizki: Tidak tahu ukuran sepatunya, tapi dia dokter...")
            print("         Dia sering masuk keluar area yang basah.")
            print()
            print("🤔 Kesimpulan: TIDAK DEFINITIF - Bisa siapa saja pria ukuran 42.")
            print()
            
        elif pilih_bukti == "2":
            print("📌 SURAT HUTANG PIUTANG RP500 JUTA")
            print()
            print("Ditemukan di laci meja Jakarta di kantor rumahnya.")
            print("Kontrak menunjukkan Jakarta berutang uang kepada investor tertentu.")
            print()
            print("Detail:")
            print("✓ Total utang: Rp500.000.000")
            print("✓ Bunga tinggi: 5% per bulan (MELANGGAR HUKUM)")
            print("✓ Pemberi utang: Kelompok investor yang dikenal keras")
            print("✓ Deadline pembayaran: 3 bulan (waktu saat kejadian)")
            print()
            print("Wawancara tambahan:")
            print("• Gunawan: Mengatakan dia tahu Jakarta 'punya masalah keuangan'")
            print("• Mira: 'Saya tahu, Jakarta sering mencemaskan hal itu.'")
            print("• Rizki: 'Saya tahu ayah berhutang. Dia pernah minta bantuan saya.'")
            print()
            print("🤔 Kesimpulan: SEMUA TAHU TENTANG HUTANG INI.")
            print("            MOTIVASI BISA UNTUK KETIGA-TIGANYA!")
            print()
            
        elif pilih_bukti == "3":
            print("📌 BOTOL OBAT PENENANG KOSONG BERTANGGAL HARI KEJADIAN")
            print()
            print("Botol kosong ditemukan di tempat sampah area pre-operasi.")
            print("Kemasan menunjukkan: OBAT PENENANG (Diazepam, dosis tinggi).")
            print()
            print("Detail Penting:")
            print("✓ Tanggal label: Hari yang sama dengan kejadian")
            print("✓ Isi botol: 20 tablet (dosis 10mg per tablet = 200mg total)")
            print("✓ Resep normal: 5-10mg per pasien (Hanya 1-2 tablet!)")
            print("✓ Dosis ditemukan: 20 tablet - FATAL untuk pre-medication!")
            print()
            print("Siapa yang punya akses:")
            print("• Gunawan: Tidak ada akses ke farmasi rumah sakit")
            print("• Mira: Tidak ada akses ke farmasi rumah sakit")
            print("• Rizki: DOKTER - Akses penuh ke semua obat! ✓✓✓")
            print()
            print("🤔 Kesimpulan: BUKTI PALING MENUNJUK KE RIZKI!")
            print("             Tapi seorang dokter punya alibi yang kuat di ruang operasi...")
            print()
            
        elif pilih_bukti == "4":
            print("📌 CATATAN RENCANA TRANSFER ASET KE LUAR NEGERI")
            print()
            print("Ditemukan di laptop Jakarta (password mudah ditebak).")
            print("Dokumen menunjukkan rencana transfer harta kekayaan.")
            print()
            print("Analisis Dokumen:")
            print("✓ Rencananya: Transfer Rp2 miliar ke rekening offshore")
            print("✓ Tujuan: Lolos dari penagih hutang")
            print("✓ Timeline: Dokumen dibuat 1 MINGGU SEBELUM KEJADIAN")
            print("✓ Penerima: Banyak nama - termasuk pemberian untuk 'asuransi'")
            print()
            print("Siapa yang tahu:")
            print("• Gunawan: Akses ke kapur kerja Jakarta? TIDAK")
            print("• Mira: ISTRI - Kemungkinan besar tahu atau ikut merencanakan")
            print("• Rizki: Kemungkinan tidak tahu, dia jarang ke kantor ayah")
            print()
            print("🤔 Kesimpulan: MENUNJUK MIRA - Dia ikut dalam rencana ini?")
            print("             Tapi ini bisnis internal, belum bukti pembunuhan...")
            print()
        
        bukti_diperiksa.append(bukti_terpilih)
        print("-" * 75)
        
    elif pilihan == "2":
        # ===== CEK TERSANGKA =====
        daftar_tersangka = [
            "Gunawan - Asisten Pribadi (30 tahun, bekerja 5 tahun)",
            "Mira - Istri Kedua (28 tahun, menikah 2 tahun)",
            "Rizki - Anak Kandung dari Istri Pertama (35 tahun, dokter)"
        ]
        
        print()
        print("-" * 75)
        print("👥 TERSANGKA YANG TERSEDIA:")
        print("-" * 75)
        for i, tersangka in enumerate(daftar_tersangka, 1):
            status = "✅ SUDAH DIWAWANCARA" if tersangka in tersangka_diwawancara else "⭕ BELUM DIWAWANCARA"
            print(f"{i}. {tersangka} [{status}]")
        print()
        
        pilih_tersangka = input("Pilih tersangka mana untuk diwawancara (1-3): ").strip()
        
        if pilih_tersangka not in ["1", "2", "3"]:
            print("⚠️ Pilihan tidak valid!")
            continue
        
        tersangka_terpilih = daftar_tersangka[int(pilih_tersangka) - 1]
        
        if tersangka_terpilih in tersangka_diwawancara:
            print(f"\n✅ Tersangka ini sudah Anda wawancara sebelumnya.")
            print(f"📝 Keterangannya tetap konsisten seperti sebelumnya.\n")
            continue
        
        print()
        print("-" * 75)
        print(f"🎤 WAWANCARA: {tersangka_terpilih.upper()}")
        print("-" * 75)
        print()
        
        # Detail wawancara dengan pilihan pertanyaan
        questions = [
            "Dimana Anda berada sebelum operasi dimulai?",
            "Apakah Anda punya akses ke obat-obatan rumah sakit?",
            "Apa hubungan Anda dengan korban akhir-akhir ini (motivasi)?",
            "Adakah saksi yang bisa menguatkan alibi Anda?",
            "Selesai wawancara"
        ]

        while True:
            print()
            print("Pilih pertanyaan yang ingin diajukan:")
            for i, q in enumerate(questions, 1):
                print(f"{i}. {q}")
            pilih_q = input("Masukkan nomor pertanyaan (1-5): ").strip()
            if pilih_q not in ["1", "2", "3", "4", "5"]:
                print("⚠️ Pilihan tidak valid!")
                continue
            if pilih_q == "5":
                print("✅ Wawancara selesai untuk tersangka ini.")
                break

            # Jawaban tersangka spesifik
            if pilih_tersangka == "1":  # Gunawan
                if pilih_q == "1":
                    print('A: "Saya menemani Jakarta sampai ruang persiapan. Setelah itu')
                    print('   saya menunggu di ruang keluarga sampai operasi dimulai."')
                elif pilih_q == "2":
                    print('A: "Saya bukan staf medis. Saya tidak punya akses ke farmasi.')
                    print('   Tidak mungkin saya ambil obat apapun."')
                elif pilih_q == "3":
                    print('A: "Saya hanya pegawai. Tidak punya motif finansial besar."')
                elif pilih_q == "4":
                    print('A: "Ada perawat yang lihat saya di ruang keluarga, dia bisa konfirmasi."')

            elif pilih_tersangka == "2":  # Mira
                if pilih_q == "1":
                    print('A: "Saya di ruang keluarga bersama keluarga lain. Saya tidak ke area medis."')
                elif pilih_q == "2":
                    print('A: "Saya bukan staf rumah sakit, saya tidak punya akses ke obat."')
                elif pilih_q == "3":
                    print('A: "Hubungan kami tegang. Saya butuh kepastian finansial dan takut kehilangan')
                    print('   kenyamanan hidup jika ayah saya hilang. Tapi saya tidak pernah ingin dia mati."')
                elif pilih_q == "4":
                    print('A: "Beberapa anggota keluarga melihat saya di ruang istirahat.')
                    print('   Mereka bisa jadi saksi alibi saya."')

            else:  # pilih_tersangka == "3", Rizki
                if pilih_q == "1":
                    print('A: "Saya berada di ruang operasi sejak briefing sampai selesai operasi."')
                elif pilih_q == "2":
                    print('A: "Sebagai dokter, saya punya akses ke obat. Semua penggunaan terekam di log."')
                elif pilih_q == "3":
                    print('A: "Hubungan kami profesional. Saya kecewa soal keputusan ayah,')
                    print('   tapi itu bukan alasan untuk mencelakakan dia."')
                elif pilih_q == "4":
                    print('A: "Banyak staff medis yang bisa mengkonfirmasi saya berada di ruang operasi."')

        tersangka_diwawancara.append(tersangka_terpilih)
        print("-" * 75)
        
    elif pilihan == "3":
        # ===== PILIH PELAKU =====
        
        # Cek apakah sudah cek minimal
        if len(bukti_diperiksa) < 1 or len(tersangka_diwawancara) < 1:
            print()
            print("⚠️ Anda belum mengumpulkan bukti yang cukup!")
            print("   Periksa minimal 1 bukti DAN 1 tersangka sebelum membuat keputusan.")
            print()
            continue
        
        print()
        print("=" * 75)
        print("🎯 FASE FINAL: TENTUKAN PELAKU KEJADIAN".center(75))
        print("=" * 75)
        print()
        
        print("📋 RINGKASAN INVESTIGASI ANDA:")
        print("-" * 75)
        print(f"Bukti yang diperiksa ({len(bukti_diperiksa)}/4):")
        for bukti in bukti_diperiksa:
            print(f"  ✓ {bukti}")
        print()
        print(f"Tersangka yang diwawancara ({len(tersangka_diwawancara)}/3):")
        for tersangka in tersangka_diwawancara:
            print(f"  ✓ {tersangka}")
        print()
        print("-" * 75)
        print()
        
        print("🕵️ BERDASARKAN INVESTIGASI ANDA, SIAPA PELAKUNYA?")
        print()
        print("1. Gunawan - Asisten Pribadi")
        print("2. Mira - Istri Kedua")
        print("3. Rizki - Anak Kandung")
        print()
        
        pilihan_akhir = input("Masukkan nomor tersangka (1/2/3): ").strip()
        
        print()
        print("=" * 75)
        print("🔎 HASIL INVESTIGASI AKHIR".center(75))
        print("=" * 75)
        print()
        
        # JAWABAN BENAR: RIZKI
        if pilihan_akhir == "3":
            print("✅ ANDA BENAR! RIZKI ADALAH PELAKUNYA!")
            print()
            print("BUKTI KRONOLOGIS:")
            print("-" * 75)
            print()
            print("1. AKSES: Sebagai dokter, Rizki punya akses penuh ke farmasi")
            print("   dan semua sistem obat-obatan rumah sakit.")
            print()
            print("2. MODUS OPERANDI: Rizki mengganti pre-medication yang normal")
            print("   dengan dosis berlebihan (20 tablet = 200mg alih-alih 5-10mg).")
            print()
            print("3. ALIBI SEMPURNA: Rizki berada di ruang operasi sepanjang waktu,")
            print("   sehingga tampak mustahil dia pelakunya. Padahal dia bisa")
            print("   menyuruh asisten farmasi untuk 'kesalahan' itu.")
            print()
            print("4. MOTIVASI JELAS:")
            print("   • Ayahnya mengurangi uang setelah menikah Mira")
            print("   • Hutang bisnis ayah membuat warisan berkurang")
            print("   • Asuransi jiwa: Rizki adalah penerima benefisiary utama")
            print("   • Sebagai dokter, dia tahu risiko pre-medication berlebihan")
            print("   • Dia percaya diri bisa 'menyelamatkan' ayahnya sendiri")
            print("     (membuat alibi sempurna)")
            print()
            print("5. PENEMUAN KRITIS:")
            print("   • Log farmasi menunjukkan Rizki ambil Diazepam singkat ")
            print("     sebelum operasi dimulai")
            print("   • Dia cerita 'profesional' tapi matanya menunjukkan")
            print("     emosi pribadi")
            print()
            print("=" * 75)
            print()
            print("🚨 KEPUTUSAN AKHIR:")
            print("   Rizki ditangkap dan diinterogasi intensif.")
            print("   Dia akhirnya mengaku setelah bukti ketahanan ledaknya dihadapkan.")
            print("   ALASAN: Mira (istri baru) 'merebut' ayahnya, dan Mira")
            print("   menjanjikan uang besar kepada Rizki agar melakukan ini.")
            print()
            print("🏆 KASUS TERPECAHKAN - ANDA LULUS SEBAGAI DETEKTIF KELAS A!")
            print()
            
        elif pilihan_akhir == "2":
            print("❌ ANDA SALAH! Tapi analisis Anda tidak sepenuhnya buruk...")
            print()
            print("Mira memang MEMILIKI MOTIVASI KUAT:")
            print("  • Dia butuh uang (bergantung pada Jakarta)")
            print("  • Ada rencana transfer aset (dia tahu tentang itu)")
            print("  • Hutang Jakarta membuatnya cemas")
            print()
            print("TAPI MASALAHNYA:")
            print("  ❌ Mira TIDAK memiliki akses ke farmasi rumah sakit")
            print("  ❌ Tidak ada bukti dia di ruang persiapan")
            print("  ❌ Perawat tidak melihatnya keluar dari ruang keluarga")
            print()
            print("PELAKU SEBENARNYA: RIZKI!")
            print()
            print("Rizki menggunakan alibi sempurna (berada di ruang operasi)")
            print("sambil sebenarnya dia mengatur agar asisten farmasi memberikan")
            print("dosis berlebihan. Mira adalah MITRA/PENDORONG, bukan pelaku!")
            print()
            print("❌ KASUS TIDAK SEPENUHNYA TERPECAHKAN")
            print("   Mira akan terus mengancam dan Rizki akan coba sterilkan bukti.")
            print()
            
        else:  # pilihan_akhir == "1"
            print("❌ ANDA SALAH! Gunawan adalah orang yang tidak bersalah.")
            print()
            print("ANALISIS KESALAHAN:")
            print("  • Gunawan TIDAK punya akses ke farmasi rumah sakit")
            print("  • Alibinya cukup kuat (dilihat di ruang keluarga oleh perawat lain)")
            print("  • Motivasinya tidak sejelas tersangka lain")
            print("  • Posisinya sebagai asisten, bukan keluarga (tidak dapat warisan)")
            print()
            print("PELAKU SEBENARNYA: RIZKI!")
            print()
            print("Sebagai dokter, Rizki punya:")
            print("  ✓ Akses penuh ke obat-obatan")
            print("  ✓ Pengetahuan medis untuk eksekusi sempurna")
            print("  ✓ Alibi kuat (di ruang operasi)")
            print("  ✓ Motivasi jelas (uang, warisan, asuransi)")
            print()
            print("Gunawan ditangkap dan dinterogasi lama tanpa alasan.")
            print("Penyelidikan dilanjutkan, seringkali mengarah ke dugaan salah.")
            print()
            print("❌ KASUS TIDAK TERPECAHKAN OPTIMAL")
            print("   Rizki terhindar untuk sementara.")
            print()
        
        print("=" * 75)
        print()
        
        # Tanyakan apakah ingin main lagi
        print()
        lagi = input("Ingin bermain kembali? (y/n): ").strip().lower()
        if lagi == "y":
            print()
            print("=" * 75)
            print("🔄 RESTARTING GAME...".center(75))
            print("=" * 75)
            print()
            break
        else:
            print()
            print("Terima kasih telah bermain Mystery Detective Bot!")
            print("=" * 75)
            break
    
    else:
        print("⚠️ Pilihan tidak valid! Masukkan 1, 2, atau 3.")
    print("💍 Anda memeriksa lemari besi...")