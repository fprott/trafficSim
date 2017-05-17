delta_t = 0.01

import math
import pygame


class Fahrzeug_Model():
    def __init__(self, Lange, Breite, v, Kurswinkel, GPS_x, GPS_y, Lenkung, Gier_Rate, a, v_max, v_min, a_max, a_min):
        self.Beschleunigung_m_s2 = a
        self.Lange_m = Lange
        self.Breite_m = Breite
        self.Geschwindigkeit_m_s = v
        self.Kurswinkel_deg = Kurswinkel
        self.GPS_X_m = GPS_x
        self.GPS_Y_m = GPS_y
        self.Lenkung_deg = Lenkung
        self.Gier_Rate_deg_s = Gier_Rate
        self.Beschleunigung_m_s2 = a
        self.Geschwindigkeit_max = v_max
        self.Geschwindigkeit_min = v_min
        self.Beschleunigung_max = a_max
        self.Beschleunigung_min = a_min

    def Fahr_Situation_Rechnen(self,Beschleunigung_m_s2,Lenkung_deg):
        self.Geschwindigkeit_m_s = self.Geschwindigkeit_m_s + self.Beschleunigung_m_s2 * delta_t
        self.Kurswinkel_deg = self.Kurswinkel_deg + self.Gier_Rate_deg_s * delta_t

        self.GPS_Y_m = self.GPS_Y_m + self.Geschwindigkeit_m_s * math.cos(math.radians(self.Kurswinkel_deg)) * delta_t
        self.GPS_X_m = self.GPS_X_m - self.Geschwindigkeit_m_s * math.sin(math.radians(self.Kurswinkel_deg)) * delta_t

        # class Fahrzeug_Zeichnung(Fahrzeug_Model):
        # def __init__(self):
        # super(Fahrzeug_Zeichnung, self).__init__(Fahrzeug_Model)


