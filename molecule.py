import particle
import numpy as np

class Molecule:
	'''Stores information about a Molecule consisting of two particles'''

	def __init__(self, P1_position, P2_position, P1_mass, P2_mass, k_spring, equilibrium_length):
		'''Create diatomic molecule with positions of both particles, their masses, a spring constant, and equilibrium length'''
		self.p1 = particle.Particle(P1_position, P1_mass)
		self.p2 = particle.Particle(P2_position, P2_mass)
		self.k  = k_spring
		self.L0 = equilibrium_length

	def get_disp1(self):
		'''Returns a vector of the displacement from partcile 1 to partcile 2'''
		return (self.p1.pos[0] - self.p2.pos[0], self.p1.pos[1] - self.p2.pos[1])

	def get_force(self):
		''' Returns a vector of the force on particle 1'''
		dist = np.linalg.norm(self.get_disp1())
		return self.k*(dist-self.L0)*(self.p2.pos-self.p1.pos)/dist
		#return (-self.k*self.get_disp1()[0] - self.L0, -self.k*self.get_disp1()[1] - self.L0)