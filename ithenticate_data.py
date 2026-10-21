"""
iThenticate / Turnitin Master Pattern Database
Contains exact patterns, match categories, and color palettes derived from official Turnitin / iThenticate reports.
"""

# The authentic iThenticate / Turnitin color scheme
ITHENTICATE_COLORS = [
    {"source_num": 1, "color": "#ec4899", "bg": "rgba(244, 114, 182, 0.14)", "name": "kantorku.id", "type": "Internet"},
    {"source_num": 2, "color": "#3b82f6", "bg": "rgba(96, 165, 250, 0.14)", "name": "repository.ar-raniry.ac.id", "type": "Internet"},
    {"source_num": 3, "color": "#10b981", "bg": "rgba(52, 211, 153, 0.14)", "name": "www.bareksa.com", "type": "Internet"},
    {"source_num": 4, "color": "#a855f7", "bg": "rgba(192, 132, 252, 0.14)", "name": "www.coursehero.com", "type": "Internet"},
    {"source_num": 5, "color": "#ef4444", "bg": "rgba(248, 113, 113, 0.14)", "name": "core.ac.uk", "type": "Internet"},
    {"source_num": 6, "color": "#0ea5e9", "bg": "rgba(56, 189, 248, 0.14)", "name": "ejournal.iaifa.ac.id", "type": "Internet"},
    {"source_num": 7, "color": "#14b8a6", "bg": "rgba(45, 212, 191, 0.14)", "name": "jurnal.umitra.ac.id", "type": "Internet"},
    {"source_num": 8, "color": "#8b5cf6", "bg": "rgba(167, 139, 250, 0.14)", "name": "pkm.lpkd.or.id", "type": "Internet"},
    {"source_num": 9, "color": "#f43f5e", "bg": "rgba(251, 113, 133, 0.14)", "name": "repository-uniswa.github.io", "type": "Internet"},
    {"source_num": 10, "color": "#2563eb", "bg": "rgba(147, 197, 253, 0.14)", "name": "storage.kopertis6.or.id", "type": "Internet"},
    {"source_num": 11, "color": "#10b981", "bg": "rgba(110, 231, 183, 0.14)", "name": "Salma Elsa Widyadhana, Muhammad Arifin. 'Implementasi Sistem SIGEMAS'", "type": "Publication"},
    {"source_num": 12, "color": "#6366f1", "bg": "rgba(165, 180, 252, 0.14)", "name": "journal.nurulfikri.ac.id", "type": "Internet"},
    {"source_num": 13, "color": "#f97316", "bg": "rgba(251, 146, 60, 0.14)", "name": "vdocuments.site", "type": "Internet"},
    {"source_num": 14, "color": "#0ea5e9", "bg": "rgba(125, 211, 252, 0.14)", "name": "www.scribd.com", "type": "Internet"},
    {"source_num": 15, "color": "#10b981", "bg": "rgba(110, 231, 183, 0.14)", "name": "adoc.pub", "type": "Internet"},
    {"source_num": 16, "color": "#a855f7", "bg": "rgba(192, 132, 252, 0.14)", "name": "clubchanani.com", "type": "Internet"},
    {"source_num": 17, "color": "#ec4899", "bg": "rgba(244, 114, 182, 0.14)", "name": "geograf.id", "type": "Internet"},
    {"source_num": 18, "color": "#3b82f6", "bg": "rgba(147, 197, 253, 0.14)", "name": "Maela, Siti Nur. 'Manajemen Keuangan Pondok Pesantren Berbasis Aplikasi CAR...'", "type": "Publication"},
]

# Exact phrases flagged in iThenticate for this proposal
AUTHENTIC_LIDM_MATCHES = [
    {
        "source_num": 10,
        "phrase": "PROPOSAL LOMBA INOVASI DIGITAL MAHASISWA (LIDM)",
        "source_name": "storage.kopertis6.or.id"
    },
    {
        "source_num": 4,
        "phrase": "Transformasi digital dalam administrasi sekolah menjadi aspek krusial untuk meningkatkan efisiensi dan transparansi",
        "source_name": "www.coursehero.com"
    },
    {
        "source_num": 7,
        "phrase": "memangkas waktu pelaporan data hingga hitungan detik, mengurangi penggunaan kertas",
        "source_name": "jurnal.umitra.ac.id"
    },
    {
        "source_num": 2,
        "phrase": "Perkembangan teknologi informasi dan komunikasi di abad ke-21 telah memicu disrupsi di berbagai sektor, termasuk dunia pendidikan",
        "source_name": "repository.ar-raniry.ac.id"
    },
    {
        "source_num": 8,
        "phrase": "UNESCO menekankan bahwa teknologi merupakan pilar utama dalam menjamin inklusivitas dan kualitas pendidikan",
        "source_name": "pkm.lpkd.or.id"
    },
    {
        "source_num": 3,
        "phrase": "efektivitas manajemen sekolah sangat bergantung pada kemampuan literasi digital",
        "source_name": "www.bareksa.com"
    },
    {
        "source_num": 6,
        "phrase": "pengambilan keputusan berbasis data (data-driven decision making)",
        "source_name": "ejournal.iaifa.ac.id"
    },
    {
        "source_num": 13,
        "phrase": "SIGAP (Sistem Jurnal Digital & Analisis Performa Murid)",
        "source_name": "vdocuments.site"
    },
    {
        "source_num": 5,
        "phrase": "Pengembangan SIGAP dilakukan dengan menggunakan metode ADDIE (Analysis, Design, Development, Implementation, Evaluation)",
        "source_name": "core.ac.uk"
    },
    {
        "source_num": 14,
        "phrase": "merencanakan dan menciptakan pembelajaran secara sistematis melalui lima langkah utama: analisis, desain, pengembangan, implementasi, dan evaluasi",
        "source_name": "www.scribd.com"
    },
    {
        "source_num": 11,
        "phrase": "mengintegrasikan pelaporan kehadiran, materi ajar, dan pemantauan perkembangan murid secara real-time",
        "source_name": "Salma Elsa Widyadhana, Muhammad Arifin. 'Implementasi Sistem SIGEMAS'"
    },
    {
        "source_num": 15,
        "phrase": "bahasa pemrograman PHP sebagai server-side scripting utama untuk membangun logika sistem yang dinamis, didukung oleh MySQL sebagai basis data",
        "source_name": "adoc.pub"
    },
    {
        "source_num": 16,
        "phrase": "waktu muat (loading time) pada server hosting",
        "source_name": "clubchanani.com"
    },
    {
        "source_num": 1,
        "phrase": "memakan waktu berjam-jam, kini dapat diselesaikan dalam hitungan detik dalam bentuk file PDF/Excel",
        "source_name": "kantorku.id"
    },
    {
        "source_num": 9,
        "phrase": "berdasarkan demonstrasi alur kerja di lapangan",
        "source_name": "repository-uniswa.github.io"
    },
    {
        "source_num": 12,
        "phrase": "pimpinan sekolah dalam mengambil keputusan berbasis data",
        "source_name": "journal.nurulfikri.ac.id"
    },
    {
        "source_num": 17,
        "phrase": "Memperkuat komunikasi dan kolaborasi antara guru, orang tua, dan sekolah",
        "source_name": "geograf.id"
    },
    {
        "source_num": 18,
        "phrase": "lebih akuntabel, efisien, dan berbasis data sebagai upaya akselerasi digitalisasi di sektor pendidikan",
        "source_name": "Maela, Siti Nur. 'Manajemen Keuangan Pondok Pesantren Berbasis Aplikasi CAR...'"
    }
]
