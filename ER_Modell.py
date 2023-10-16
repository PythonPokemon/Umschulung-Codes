from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


Base = declarative_base()

class Inhaber(Base):
    __tablename__ = 'Inhaber'

    InhaberID = Column(Integer, primary_key=True)
    Name = Column(String)
    Vorname = Column(String)

    konten = relationship("Konto", back_populates="inhaber")

class Typ(Base):
    __tablename__ = 'Typ'

    TypID = Column(Integer, primary_key=True)
    Typ = Column(String)

    konten = relationship("Konto", back_populates="typ")

class Konto(Base):
    __tablename__ = 'Konto'

    KontoID = Column(Integer, primary_key=True)
    InhaberID = Column(Integer, ForeignKey('Inhaber.InhaberID'))
    Eröffnungsdatum = Column(Date)
    Kontostand = Column(Integer)
    TypID = Column(Integer, ForeignKey('Typ.TypID'))

    inhaber = relationship("Inhaber", back_populates="konten")
    typ = relationship("Typ", back_populates="konten")

# Erstellen einer SQLite-Datenbank und Verbindung
engine = create_engine('sqlite:///bank.db', echo=True)
Base.metadata.create_all(engine)

# Erstellen einer Session
Session = sessionmaker(bind=engine)
session = Session()

class BankApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.output_label = Label(text="Konto-Datenbank")
        self.add_button = Button(text="Konto hinzufügen")
        self.add_button.bind(on_release=self.add_konto)
        layout.add_widget(self.output_label)
        layout.add_widget(self.add_button)
        return layout

    def add_konto(self, instance):
        # Hier können Sie Logik zum Hinzufügen von Konten zur Datenbank hinzufügen
        pass

if __name__ == '__main__':
    BankApp().run()