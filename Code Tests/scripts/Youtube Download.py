from pytube import YouTube
class YTDownload():
    def __init__(self):
        link = self.linkfill()
        self.yt = YouTube(link)
        self.divisoria = '-------------------------------------------------------'
        #Retornar uma lista com todas as versões do video
        self.lista_de_videos = self.yt.streams.all()

    def linkfill(self):
        print('Insira o link')
        link = input()
        link = link.strip()
        return link

    #isolado
    #progressivo = self.lista_de_videos.filter(progressive=True).all()
    #adaptivo = selflista_de_videos.filter(adaptive=True).all()
    #isolado

    def listagem(self):
        index = 0
        for video in self.lista_de_videos:
            print("[INDEX: {}] <VIDEO>: {}".format(index,video))
            index += 1
        print(self.divisoria)

    #????
    def escolha(self):
        index_vid = input('Qual video deseja baixar? ')
        return int(index_vid)

    def selecao(self, escolha):
        index = escolha
        video = self.lista_de_videos[index]
        return video

    def caminho(self):
        print('Onde deseja salvar?')
        caminho = input()
        caminho = caminho.strip()
        return caminho

    def downloadVideo(self, video):
        caminho = self.caminho()
        video.download(caminho)
    

yt = YTDownload()
    
yt.listagem()
index = yt.escolha()
video = yt.selecao(index)
yt.downloadVideo(video)