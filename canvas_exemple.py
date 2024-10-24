from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget

Builder.load_file("canvas_exemple.kv")

# ******************************************* CANVASFORMS ******************************************************


class CanvasForms(StencilView):
    pass

# *********************************************** CANVASLINE ****************************************************


class CanvasLine(Widget):
    pass

# ********************************************* CANVAS_LINE_FORMS ************************************************


class CanvasLineForms(StencilView):  # Permet de supprimer un élément qui sort du champ (Stencil)
    pass

# **************************************************************************************************************
