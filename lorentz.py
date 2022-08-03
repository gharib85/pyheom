#Lorentz
#also know as Meier Tannor decomposition
#ref https://aip.scitation.org/doi/10.1063/1.4870035  (see eq 10)
#dr.gharib85@gmail.com
#https://github.com/gharib85



class Lorentz:
    def __init__(self, p,g,s):
        self.p     = float(p)
        self.g = float(g)
        self.s = float(s)
        self.name = 'Lorentzn'
        self.poles = self.get_poles()

    def get_poles(self):
        p= self.p   
        g=  self.g 
        s= self.s
        if s==0:
            return [[g,p,2,0]]
        elif g==0:
            return [[complex(0,s),p,2,0]]
        else:
            return [[complex(g,s),complex(0, p/(4*s*g)),1,0],[complex(g,-s),complex(0,- p/(4*s*g)),1,0]]
        
    def spectrum(self, omega):
        p=self.p
        g=self.g
        s=self.s
        return p*omega/(((omega+s)**2+g**2)*((omega-s)**2+g**2))

#TODO
# instesd od accepting 3 number Lorentz(1,2,3)=> array lorentz([[11,12,13],[21,22,23],..[n1,n2,n3]]) n*3
# so can take para of fitting as matrix use it easily 
# i impplented it  to Mathematica (compare Matsubara and Pade ,fast convergence Pade)
