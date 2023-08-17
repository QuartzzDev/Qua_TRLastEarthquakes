import requests
import time

print("Quartzz Son Depremler\n Bütün Bilgiler Boğaziçi Üniversitesi Rektörlüğü’ne ait olup, Boğaziçi Üniversitesi Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü Bölgesel Deprem-Tsunami İzleme Ve Değerlendirme Merkezi'nin Kendi Sitesinden Temin Edilmektedir .")

while True:
    url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
    response = requests.get(url)
    content = response.text

    start_index = content.find("<pre>") + len("<pre>")
    end_index = content.find("</pre>", start_index)
    deprem_data = content[start_index:end_index].strip()

    first_line = deprem_data.split('\n')[6]

    print(first_line)
    time.sleep(10)
