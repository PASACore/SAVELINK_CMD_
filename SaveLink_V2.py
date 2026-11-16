from pytubefix import YouTube
import subprocess
import os
import imageio_ffmpeg
os.system("")
# ---------------- ARAYÜZ ----------------
BASLIK = """
███████╗ █████╗ ██╗   ██╗███████╗██╗     ██╗███╗   ██╗██╗  ██╗
██╔════╝██╔══██╗██║   ██║██╔════╝██║     ██║████╗  ██║██║ ██╔╝
███████╗███████║██║   ██║█████╗  ██║     ██║██╔██╗ ██║█████╔╝ 
╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║     ██║██║╚██╗██║██╔═██╗ 
███████║██║  ██║ ╚████╔╝ ███████╗███████╗██║██║ ╚████║██║  ██╗
╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
------->>>>>>>| ▄︻デ══━一一 ᴍᴀᴅᴇ ɪɴ ᴛᴜʀᴋᴇʏ :D |<<<<<<<--------"""

LINK_SOR = """
╔===========================╗
╠--->>>>YOUTUBE LİNKİ<<<<---╣
╚===========================╝
『GİR』>:"""

YUKLENIYOR = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   VİDEO YÜKLENİYOR🔄           
 --->>>『%{}』<<<---          
          🌞              
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"""

YUKLENDI = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   VİDEO YÜKLENDİ✅      
 ->>『GÜLE GÜLE🫶🏻』<<-       
          🌞
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"""

YUKLENEMEDI = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  VİDEO YÜKLENEMEDİ❌      
 ->>『Tekrar Dene』<<-       
          🤬              
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"""

#--------Foksiyonlar-----------
def Video_İndirme():
    global VideoAd
    video = YouTube(link, on_progress_callback=Video_Yuzde)
    videoAd = video.title

    #İsim kontrol
    for x in '<>:"/\\|?*':
        videoAd = videoAd.replace(x, "_")

    # En iyi video ve sesi bul
    VideoBulma = video.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first()
    AudioBulma = video.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first()

    #Video Yükleme
    if VideoBulma and AudioBulma:
        VideoBulma.download(output_path=".", filename="{}+.mp4".format(videoAd))
        AudioBulma.download(output_path=".", filename="{}(Aduio)+.mp4".format(videoAd))
        
        raise Exception("Uygun video/ses bulunamadı")

def Video_Birleştirme():
    subprocess.run([
        imageio_ffmpeg.get_ffmpeg_exe(), "-y",
        "-i", "{}+.mp4".format(videoAd),
        "-i", "{}(Aduio)+.mp4".format(videoAd),
        "-c:v", "copy", "-c:a", "aac",
        "{}.mp4".format(videoAd)
    ], check=True)
    os.remove("{}(Aduio)+.mp4".format(videoAd))
    os.remove("{}+.mp4".format(videoAd))

def Video_Konum():
    print("Kaydedilen yer:", os.path.abspath("{}.mp4".format(videoAd)))

def Video_Yuzde(stream, chunk, bytes_remaining):
    yuzde = 100 - bytes_remaining * 100 / stream.filesize
    print("\033[6A" + YUKLENIYOR.format(round(yuzde)))

#-------ANA PROGRAM--------
print(BASLIK)
while True:
    try:
        link = input(LINK_SOR)
        print(YUKLENIYOR.format(0))
        Video_İndirme()
        Video_Birleştirme()
        print(YUKLENDI)
        Video_Konum()

    except Exception as Error:
        print("Hata:", Error)
        print(YUKLENEMEDI)
