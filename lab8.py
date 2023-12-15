from PIL import Image

class GifSplitter:
    def __init__(self):
        self.path = None
        self.images = []

    def split_gif(self, path):
        self.path = path
        img = Image.open(self.path)

        frames = img.n_frames
        for i in range(frames):
            img.seek(i)
            img_save = img.copy()
            img_save.save(f"{self.path[:-11]}/frames/frame_{i}.png")
            self.images.append(img_save)


gif_path = "C:/Users/Admin/Downloads/lab8/Gosling.gif"

splitter = GifSplitter()

splitter.split_gif(gif_path)
