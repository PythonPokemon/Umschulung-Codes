from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line

class EntitySymbol(Widget):
    def __init__(self, name, attributes, **kwargs):
        super(EntitySymbol, self).__init__(**kwargs)
        self.add_entity_symbol()
        self.add_widget(Label(text=name, pos=(self.x, self.top), size=self.size, font_size=18))
        for attribute in attributes:
            self.add_widget(Label(text=attribute, font_size=14))

    def add_entity_symbol(self):
        with self.canvas:
            Color(0.7, 0.7, 1, 0.7)  # Helle Blaue Farbe mit Transparenz
            Rectangle(pos=self.pos, size=self.size)
            Color(0, 0, 0, 1)  # Schwarze Farbe
            Line(rectangle=(self.x, self.y, self.width, self.height))

class RelationshipSymbol(Widget):
    def __init__(self, name, cardinality, **kwargs):
        super(RelationshipSymbol, self).__init__(**kwargs)
        self.add_relationship_symbol()
        self.add_widget(Label(text=name, pos=(self.x, self.top), size=self.size, font_size=18))
        self.add_widget(Label(text=cardinality, font_size=14))

    def add_relationship_symbol(self):
        with self.canvas:
            Color(1, 0.7, 0.7, 0.7)  # Helle Rote Farbe mit Transparenz
            Rectangle(pos=self.pos, size=self.size)
            Color(0, 0, 0, 1)  # Schwarze Farbe
            Line(rectangle=(self.x, self.y, self.width, self.height))

class AttributeSymbol(Widget):
    def __init__(self, name, **kwargs):
        super(AttributeSymbol, self).__init__(**kwargs)
        self.add_attribute_symbol()
        self.add_widget(Label(text=name, pos=(self.x, self.top), size=self.size, font_size=14))

    def add_attribute_symbol(self):
        with self.canvas:
            Color(0.7, 1, 0.7, 0.7)  # Helle Grüne Farbe mit Transparenz
            Rectangle(pos=self.pos, size=self.size)
            Color(0, 0, 0, 1)  # Schwarze Farbe
            Line(rectangle=(self.x, self.y, self.width, self.height))

class ERDiagram(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        entity_attributes = ["Attribute 1", "Attribute 2", "Attribute 3"]
        entity = EntitySymbol(name="Entity", attributes=entity_attributes, size_hint=(None, None), size=(150, 100))

        relationship = RelationshipSymbol(name="Relationship", cardinality="1 : 1", size_hint=(None, None), size=(150, 150))

        attribute1 = AttributeSymbol(name="Attribute 4", size_hint=(None, None), size=(100, 50))
        attribute2 = AttributeSymbol(name="Attribute 5", size_hint=(None, None), size=(100, 50))

        layout.add_widget(entity)
        layout.add_widget(relationship)
        layout.add_widget(attribute1)
        layout.add_widget(attribute2)

        return layout

if __name__ == '__main__':
    ERDiagram().run()
