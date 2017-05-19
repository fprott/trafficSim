
import numpy


class Shedule:



    def __init__(self,time_step,x_init,v_init,a_init,goals,current_time):
        #self.__init__()
        self.time_step=time_step
        self.x_now=x_init;
        self.v_now=v_init;
        self.a_now=a_init;
        self.gaols=goals;
        self.nr_cars=len(self.x_now);
        self.current_time=current_time;
        self.stop=0;
        self.goalreached = [0]*self.nr_cars;



    def nextstep(self,a):


        self.a_now = a;
        for i in range(0,self.nr_cars):
            self.x_now[i]=self.x_now[i]+self.v_now[i]*self.time_step+0.5*self.a_now[i]*self.time_step*self.time_step;
            self.v_now[i]=self.v_now[i]+self.a_now[i]*self.time_step;
        self.current_time=self.current_time+self.time_step;


    def goal_reached(self):
        for i in range(0, self.nr_cars):
            if x_now[i] >= self.goals[i]:
                self.goalreached[i]=1;          'car i has reached goal'



    def checkcollision(self):             'check for car collisions and set self.stop to 1 in case of collisions'
            # work in progress


#time_step,x_init,v_init,a_init,gaols,current_time
#Test
sh= Shedule(1,[0,0,0],[0,0,0],[0,0,0],[14,0,20],0)

#print (sh.x_now)
#sh.nextstep([2,0,4])
#print (sh.x_now)
#sh.nextstep([2,0,4])
#print (sh.x_now)
#sh.nextstep([2,0,4])
#print (sh.x_now)
#sh.nextstep([2,0,4])
#print (sh.x_now)
#print(sh.stop)

#








