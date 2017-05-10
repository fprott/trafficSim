delta_t = 0.01

import math

class Fahrzeug_Model():
    def __init__(self,Lange,Breite,Geschwindigkeit,Kurswinkel,GPS_x,GPS_y,Lenkung,Gier_Rate,Beschleunigung):
        Lange_m = Lange;
        Breite_m = Breite;
        Geschwindigkeit_m_s = Geschwindigkeit;
        Kurswinkel_deg = Kurswinkel;
        GPS_X_m = GPS_x;
        GPS_Y_m = GPS_y;
        Lenkung_deg = Lenkung;
        Gier_Rate_deg_s = Gier_Rate;
        Beschleunigung_m_s2 = Beschleunigung;

    def Fahr_Situation_Rechnen(self):
        self.Geschwindigkeit_m_s = self.Geschwindigkeit_m_s + self.Beschleunigung_m_s2 * delta_t
        self.Kurswinkel_deg = self.Kurswinkel_deg + self.Gier_Rate_deg_s * delta_t

        self.GPS_Y_m = self.GPS_Y_m + self.Geschwindigkeit_m_s * math.cos(math.radians(self.Kurswinkel_deg)) * delta_t
        self.GPS_X_m = self.GPS_X_m - self.Geschwindigkeit_m_s * math.sin(math.radians(self.Kurswinkel_deg)) * delta_t

class Fahrzeug_Zeichnung():
    def __init__(self):
        super(Fahrzeug_Zeichnung, self).__init__(Fahrzeug_Model)
