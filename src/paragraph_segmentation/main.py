from wtpsplit import SaT


class ParagraphSegmentation:
    def __init__(self, model_name="sat-3l-sm", do_paragraph_segmentation=True):
        self.sat = SaT(model_name)

    def split_text(self, text, do_paragraph_segmentation=True):
        return self.sat.split(text, do_paragraph_segmentation)
