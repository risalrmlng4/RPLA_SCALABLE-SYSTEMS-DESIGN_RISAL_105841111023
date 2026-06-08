import time
# STUDI KASUS:
# Sistem Kasir Minimarket Berbasis Docker

beban_awal = {
    "Kasir A": 0,
    "Kasir B": 5,
    "Kasir C": 7
}

TOTAL_TRANSAKSI = 30

rr_baru = {
    "Kasir A": 0,
    "Kasir B": 0,
    "Kasir C": 0
}

lc_total = beban_awal.copy()

daftar_kasir = ["Kasir A", "Kasir B", "Kasir C"]
indeks_rr = 0

riwayat_log = []

# SIMULASI MASUKNYA TRANSAKSI BARU

for nomor_trx in range(1, TOTAL_TRANSAKSI + 1):

    # ROUND ROBIN
    kasir_rr = daftar_kasir[indeks_rr]
    rr_baru[kasir_rr] += 1

    indeks_rr = (indeks_rr + 1) % 3

    status_rr = (
        f"A:{beban_awal['Kasir A'] + rr_baru['Kasir A']}, "
        f"B:{beban_awal['Kasir B'] + rr_baru['Kasir B']}, "
        f"C:{beban_awal['Kasir C'] + rr_baru['Kasir C']}"
    )

    # LEAST CONNECTION
    kasir_lc = min(lc_total, key=lc_total.get)

    log_lc = kasir_lc

    lc_total[kasir_lc] += 1

    status_lc = (
        f"A:{lc_total['Kasir A']}, "
        f"B:{lc_total['Kasir B']}, "
        f"C:{lc_total['Kasir C']}"
    )

    # SIMPAN LOG
    riwayat_log.append(
        f"#{nomor_trx:02d} | "
        f"RR -> {kasir_rr:<8} ({status_rr:<18}) | "
        f"LC -> {log_lc:<8} ({status_lc:<18})"
    )

# DASHBOARD

print("\n" + "-" * 70)
print("        SIMULASI LOAD BALANCING SISTEM KASIR MINIMARKET")
print("                    BERBASIS DOCKER")
print("-" * 70)

print("\n🏪 Minimarket : r2 maju")
print("🐳 Infrastruktur : Docker Container")
print("🧾 Total Transaksi Baru :", TOTAL_TRANSAKSI)

print("\nContainer Docker yang Berjalan:")
print("--------------------------------")
print("kasir-a")
print("kasir-b")
print("kasir-c")

print("\nBeban Awal Tiap Container:")
print("--------------------------------")

for kasir, beban in beban_awal.items():
    print(f"{kasir:<8} : {beban} transaksi aktif")

# ROUND ROBIN

print("\n" + "-" * 70)
print("🚀 ALGORITMA ROUND ROBIN")
print("-" * 70)

print("\nDistribusi Transaksi Secara Bergiliran")

print("\nNama Kasir | Beban Awal | Transaksi Baru | Total Akhir")
print("------------------------------------------------------")

for kasir in daftar_kasir:
    total_rr = beban_awal[kasir] + rr_baru[kasir]

    print(
        f"{kasir:<10}| "
        f"{beban_awal[kasir]:<10}| "
        f"+{rr_baru[kasir]:<14}| "
        f"{total_rr}"
    )

print("\nKeterangan:")
print("Setiap transaksi dibagikan secara bergiliran")
print("ke setiap container Docker tanpa melihat")
print("jumlah transaksi aktif yang sedang diproses.")

# ==========================================================
# LEAST CONNECTION
# ==========================================================

print("\n" + "-" * 70)
print("🧠 ALGORITMA LEAST CONNECTION")
print("-" * 70)

print("\nDistribusi Berdasarkan Container Dengan Beban Terendah")

print("\nNama Kasir | Beban Awal | Transaksi Baru | Total Akhir")
print("------------------------------------------------------")

for kasir in daftar_kasir:

    trx_baru = lc_total[kasir] - beban_awal[kasir]

    print(
        f"{kasir:<10}| "
        f"{beban_awal[kasir]:<10}| "
        f"+{trx_baru:<14}| "
        f"{lc_total[kasir]}"
    )

print("\nKeterangan:")
print("Load balancer selalu memilih container")
print("yang memiliki jumlah transaksi aktif paling sedikit.")

# LOG TERAKHIR

print("\n" + "-" * 70)

print(
    f"[TRANSAKSI #{TOTAL_TRANSAKSI:02d}] "
    f"Round Robin -> {kasir_rr} | "
    f"Least Connection -> {log_lc}"
)

print("-" * 70)

# RIWAYAT DISTRIBUSI

print("\n" + "-" * 70)
print("              RIWAYAT DISTRIBUSI TRANSAKSI")
print("-" * 70)

print(
    f"{'TRX':<5} | "
    f"{'ROUND ROBIN':<34} | "
    f"{'LEAST CONNECTION':<34}"
)

print("-" * 85)

for log in riwayat_log:
    print(log)
    time.sleep(0.01)

print("-" * 75)

# KESIMPULAN

print("\n📊 HASIL EVALUASI")

total_rr_a = beban_awal["Kasir A"] + rr_baru["Kasir A"]
total_rr_b = beban_awal["Kasir B"] + rr_baru["Kasir B"]
total_rr_c = beban_awal["Kasir C"] + rr_baru["Kasir C"]

print("\nRound Robin:")
print(
    f"Kasir A={total_rr_a}, "
    f"Kasir B={total_rr_b}, "
    f"Kasir C={total_rr_c}"
)

print("\nLeast Connection:")
print(
    f"Kasir A={lc_total['Kasir A']}, "
    f"Kasir B={lc_total['Kasir B']}, "
    f"Kasir C={lc_total['Kasir C']}"
)

print("\nKesimpulan:")
print("Least Connection menghasilkan distribusi")
print("transaksi yang lebih seimbang dibandingkan")
print("Round Robin ketika beban awal container berbeda.")

print("\n✅ SIMULASI SELESAI")
print("Pengujian Load Balancing pada Sistem Kasir")
print("Minimarket Berbasis Docker berhasil dilakukan.")