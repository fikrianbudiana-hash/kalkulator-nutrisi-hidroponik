import streamlit as st

st.set_page_config(page_title="Kalkulator Nutrisi Hidroponik", layout="centered")

st.title("🌱 Kalkulator Nutrisi Hidroponik")
st.write("Versi digital dari Excel KALKULATOR NUTRISI HIDROPONIIK")

# ======================
# DATA DARI EXCEL
# ======================
pupuk = [
    {"nama": "MEROKE CALNIT", "berat": 1000, "harga": 22000, "kebutuhan_10L": 950},
    {"nama": "MEROKE FLEX G", "berat": 1000, "harga": 60000, "kebutuhan_10L": 1200},
    {"nama": "MEROKE MAG-S", "berat": 1000, "harga": 19000, "kebutuhan_10L": 460},
    {"nama": "MEROKE MAP", "berat": 500, "harga": 23000, "kebutuhan_10L": 60},
    {"nama": "MEROKE VITAFLEX", "berat": 100, "harga": 25000, "kebutuhan_10L": 4},
]

# ======================
# INPUT USER
# ======================
n_liter = st.number_input("Masukkan jumlah larutan (liter)", min_value=1.0, value=10.0, step=1.0)

if st.button("Hitung Nutrisi"):
    total_biaya = 0

    st.subheader("📊 Hasil Perhitungan")

    for p in pupuk:
        kebutuhan_per_liter = p["kebutuhan_10L"] / 10
        harga_per_liter = p["harga"] / 10
        dipakai_kali = p["berat"] / p["kebutuhan_10L"]

        n_gram = kebutuhan_per_liter * n_liter
        biaya = harga_per_liter * n_liter

        total_biaya += biaya

        st.markdown(f"""
        **{p['nama']}**
        - Kebutuhan per liter: `{kebutuhan_per_liter:.2f} g`
        - Bisa dipakai: `{dipakai_kali:.2f} kali`
        - Untuk {n_liter} L: `{n_gram:.2f} g`
        - Biaya: `Rp {biaya:,.0f}`
        """)

    st.success(f"💰 Total Biaya: Rp {total_biaya:,.0f}")



   