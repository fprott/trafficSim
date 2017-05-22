delta_t = 0.01

import math
import pygame

class Fahrzeug_Model():
    def __init__(self, Lange, Breite, v, Kurswinkel, GPS_x, GPS_y, Lenkung, Gier_Rate, a, v_max, v_min, a_max, a_min,gier_rate_max,gier_rate_min):
        self.Parameter = [Lange, Breite]
        #self.Parameter_Lange_m = Lange
        #self.Parameter.Breite_m = Breite
        #self.Parameter=[self.Parameter_Lange_m,self.Paraeter]


        self.Eingabe = [a, Lenkung]
        self.Eingabe.Beschleunigung_m_s2 = a
        self.Eingabe.Lenkung_deg = Lenkung

        self.Situation = [v,self.Eingabe.Lenkung_deg*60/90,Kurswinkel,GPS_x,GPS_y]
        self.Situation.Geschwindigkeit_m_s = v
        self.Situation.Gier_Rate_deg_s = self.Eingabe.Lenkung_deg * 60/90
        self.Situation.Kurswinkel_deg = Kurswinkel
        self.Situation.GPS_X_m = GPS_x
        self.Situation.GPS_Y_m = GPS_y

        self.Beschrankung = [v_max, v_min, a_max, a_min, gier_rate_max, gier_rate_min]
        self.Beschrankung.Geschwindigkeit_max = v_max
        self.Beschrankung.Geschwindigkeit_min = v_min
        self.Beschrankung.Beschleunigung_max = a_max
        self.Beschrankung.Beschleunigung_min = a_min
        self.Beschrankung.Gier_Rate_max = gier_rate_max
        self.Beschrankung.Gier_Rate_min = gier_rate_min

    def Fahr_Situation_Rechnen(self,Beschleunigung_m_s2,Lenkung_deg):
        self.Eingabe.Beschleunigung_m_s2 = Beschleunigung_m_s2
        self.Eingabe.Lenkung_deg = Lenkung_deg

        if self.Eingabe.Beschleunigung_m_s2 > self.Beschrankung.Beschleunigung_max:
            self.Eingabe.Beschleunigung_m_s2 = self.Beschrankung.Beschleunigung_max
        elif self.Eingabe.Beschleunigung_m_s2 < self.Beschrankung.Beschleunigung_min:
            self.Eingabe.Beschleunigung_m_s2 = self.Beschrankung.Beschleunigung_min

        if self.Situation.Gier_Rate_deg_s > self.Beschrankung.Gier_Rate_max:
            self.Situation.Gier_Rate_deg_s = self.Beschrankung.Gier_Rate_max
        elif self.Situation.Gier_Rate_deg_s < self.Beschrankung.Gier_Rate_min:
            self.Situation.Gier_Rate_deg_s = self.Beschrankung.Gier_Rate_min

        self.Situation.Geschwindigkeit_m_s = self.Situation.Geschwindigkeit_m_s + self.Eingabe.Beschleunigung_m_s2 * delta_t
        self.Situation.Kurswinkel_deg = self.Situation.Kurswinkel_deg + self.Gier_Rate_deg_s * delta_t

        self.Situation.GPS_Y_m = self.Situation.GPS_Y_m + self.Geschwindigkeit_m_s * math.cos(math.radians(self.Situation.Kurswinkel_deg)) * delta_t
        self.Situation.GPS_X_m = self.Situation.GPS_X_m - self.Geschwindigkeit_m_s * math.sin(math.radians(self.Situation.Kurswinkel_deg)) * delta_t

        # class Fahrzeug_Zeichnung(Fahrzeug_Model):
        # def __init__(self):
        # super(Fahrzeug_Zeichnung, self).__init__(Fahrzeug_Model)


