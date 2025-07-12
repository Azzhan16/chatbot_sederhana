
import streamlit as st

st.title("Chatbox Perayaan 17 Agustus")

# Data pertanyaan dan jawaban dengan keyword
qa_data = [
    {"keywords": ["perayaan", "17 agustus"], "answer": "Perayaan 17 Agustus adalah hari kemerdekaan Republik Indonesia yang diperingati setiap tahun."},
    {"keywords": ["kegiatan", "lomba"], "answer": "Biasanya ada upacara bendera, lomba-lomba seperti balap karung, makan kerupuk, dan berbagai acara hiburan."},
    {"keywords": ["penting", "memperingati"], "answer": "Untuk mengenang jasa para pahlawan dan menumbuhkan rasa cinta tanah air."},
    {"keywords": ["di mana", "perayaan"], "answer": "Perayaan dilakukan di seluruh Indonesia, mulai dari sekolah, kantor, hingga lingkungan masyarakat."},
    {"keywords": ["proklamasi", "kemerdekaan"], "answer": "Kemerdekaan Indonesia diproklamasikan oleh Ir. Soekarno dan Drs. Mohammad Hatta."},
    {"keywords": ["makna", "lomba"], "answer": "Lomba-lomba melambangkan semangat kebersamaan, kerja sama, dan kegembiraan dalam memperingati kemerdekaan."},
    {"keywords": ["warna", "bendera"], "answer": "Bendera Indonesia berwarna merah dan putih."},
    {"keywords": ["upacara", "17 agustus"], "answer": "Upacara bendera memperingati Hari Kemerdekaan Republik Indonesia."},
    {"keywords": ["lagu", "upacara"], "answer": "Lagu Indonesia Raya dinyanyikan saat upacara bendera."},
    {"keywords": ["arti", "merah", "putih"], "answer": "Merah melambangkan keberanian, putih melambangkan kesucian."},
    {"keywords": ["kapan", "proklamasi"], "answer": "Proklamasi dibacakan pada tanggal 17 Agustus 1945."},
    {"keywords": ["di mana", "proklamasi"], "answer": "Proklamasi dibacakan di Jalan Pegangsaan Timur No. 56, Jakarta."},
    {"keywords": ["lomba", "populer"], "answer": "Lomba balap karung, makan kerupuk, panjat pinang, tarik tambang, dan lomba kelereng."},
    {"keywords": ["siapa", "lomba"], "answer": "Lomba diikuti oleh anak-anak, remaja, dan orang dewasa di lingkungan masyarakat."}
]

# Riwayat chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Fungsi pencarian jawaban berdasarkan keyword
def find_answer(question):
    question_lower = question.lower()
    for item in qa_data:
        if all(keyword in question_lower for keyword in item["keywords"]):
            return item["answer"]
    return "Maaf, pertanyaan belum tersedia dalam database."

# Input pertanyaan
user_question = st.text_input("Tulis pertanyaan tentang 17 Agustus:")

if st.button("Kirim"):
    answer = find_answer(user_question)
    st.session_state.chat_history.append((user_question, answer))

# Tampilkan riwayat chat
for q, a in st.session_state.chat_history:
    st.markdown(f"**Anda:** {q}")
    st.markdown(f"**Chatbox:** {a}")